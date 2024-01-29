from ott.neural.flows.models import VelocityField
from ott.neural.flows.flows import UniformSampler, ConstantNoiseFlow
from ott.neural.flows.otfm import OTFlowMatching
from ott.solvers.linear import sinkhorn
from ott.tools import sinkhorn_divergence
from ott.geometry import pointcloud
from ott.neural.data.dataloaders import OTDataLoader

import optax
import scanpy as sc

import jax.numpy as jnp

import numpy as np
import pandas as pd
import sys

adata = sc.read_h5ad(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/{sys.argv[2]}/{sys.argv[3]}/{sys.argv[1]}/{sys.argv[1]}_adata.h5ad')

if sys.argv[1]=='gastrulation':
    early = 8.25
    late = 8.5
else:
    early = 8.5
    late = 8.75

if sys.argv[4]=='vae':
    sc.pp.neighbors(adata, use_rep='X_emb')
    divergence_ref = sinkhorn_divergence.sinkhorn_divergence(
              pointcloud.PointCloud, adata[adata.obs.day==early].obsm['X_emb'], adata[adata.obs.day==late].obsm['X_emb']
          ).divergence
elif sys.argv[4]=='pca':
    sc.pp.neighbors(adata)
    divergence_ref = sinkhorn_divergence.sinkhorn_divergence(
              pointcloud.PointCloud, adata[adata.obs.day==early].obsm['X_pca'], adata[adata.obs.day==late].obsm['X_pca']
          ).divergence
else:
    raise NotImplementedError
sc.tl.umap(adata)
sc.pl.umap(adata, color='day', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_{sys.argv[4]}_pre_day.png')
sc.pl.umap(adata, color='celltype', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_{sys.argv[4]}_pre_cell.png')

if sys.argv[4]=='vae':
    adata_loader = OTDataLoader(1024, source_lin=adata[adata.obs['day']==early].obsm['X_emb'], target_lin=adata[adata.obs['day']==late].obsm['X_emb'])
elif sys.argv[4]=='pca':
    adata_loader = OTDataLoader(1024, source_lin=adata[adata.obs['day']==early].obsm['X_pca'], target_lin=adata[adata.obs['day']==late].obsm['X_pca'])
else:
    raise NotImplementedError

neural_vf = VelocityField(
    output_dim=50,
    condition_dim=0,
    latent_embed_dim=256,
    n_frequencies=128
)
ot_solver = sinkhorn.Sinkhorn()
time_sampler = UniformSampler()
optimizer = optax.adam(learning_rate=1e-4)
fm = OTFlowMatching(
    neural_vf,
    input_dim=50,
    cond_dim=0,
    iterations=100000,
    valid_freq=2,
    ot_solver=ot_solver,
    flow=ConstantNoiseFlow(0.0),
    time_sampler=time_sampler,
    optimizer=optimizer
)
fm(adata_loader, adata_loader)

adata_concat = sc.concat(
    {'source': adata[adata.obs.day==early], 'source_push': adata[adata.obs.day==early], 'target': adata[adata.obs.day==late]},
    label='day_umap'
)
if sys.argv[4]=='vae':
    adata_concat.obsm["X_new"] = np.concatenate(
        (adata[adata.obs['day']==early].obsm['X_emb'],
         np.array(fm.transport(jnp.array(adata[adata.obs['day']==early].obsm['X_emb']), condition=None, forward=True)), 
         adata[adata.obs.day==late].obsm['X_emb']),
        axis=0
    )
elif sys.argv[4]=='pca':
    adata_concat.obsm["X_new"] = np.concatenate(
        (adata[adata.obs['day']==early].obsm['X_pca'], 
         np.array(fm.transport(jnp.array(adata[adata.obs['day']==early].obsm['X_pca']), condition=None, forward=True)), 
         adata[adata.obs.day==late].obsm['X_pca']),
        axis=0
    )
else:
    raise NotImplementedError
del adata_concat.obsm['X_diffmap']

sc.pp.neighbors(adata_concat, use_rep='X_new')
sc.tl.umap(adata_concat)
sc.pl.umap(adata_concat, color='day_umap', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_{sys.argv[4]}_after_all_day.png')
sc.pl.umap(adata_concat, color='celltype', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_{sys.argv[4]}_after_all_cell.png')

adata_con_2 = adata_concat[adata_concat.obs['day_umap']!='source'].copy()
sc.pp.neighbors(adata_con_2, use_rep='X_new')
sc.tl.umap(adata_con_2)
sc.pl.umap(adata_con_2, color='day_umap', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_{sys.argv[4]}_after_pushed_day.png')
sc.pl.umap(adata_con_2, color='celltype', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_{sys.argv[4]}_after_pushed_cell.png')

divergence = pd.DataFrame(
    data={'n_obs': [sys.argv[2]], 'n_genes': [sys.argv[3]], 'dataset': [sys.argv[1]], 'space': [sys.argv[4]],
          'divergence': [sinkhorn_divergence.sinkhorn_divergence(
              pointcloud.PointCloud,
              adata_concat[adata_concat.obs.day_umap=='09.00_push'].obsm['X_new'],
              adata_concat[adata_concat.obs.day_umap=='13.50'].obsm['X_new']
          ).divergence],
          'divergence_ref': [divergence_ref]
         }
).to_csv(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergence_results/scArches/divergence_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_{sys.argv[4]}.csv')
