from ott.neural.flows.models import VelocityField
from ott.neural.flows.flows import ConstantNoiseFlow
from ott.neural.flows.samplers import sample_uniformly
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
import cloudpickle
import sys
#TODO change import when model selected
adata = sc.read_h5ad(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/training/{sys.argv[1]}/{sys.argv[2]}/{sys.argv[3]}_adata.h5ad')

adata = adata[[x in [9.00, 13.5] for x in adata.obs.day]]

if sys.argv[3]=='integrated':
    sc.pp.neighbors(adata, use_rep='X_emb')
    divergence_ref = sinkhorn_divergence.sinkhorn_divergence(
              pointcloud.PointCloud, adata[adata.obs.day==9.00].obsm['X_emb'], adata[adata.obs.day==13.5].obsm['X_emb']
          ).divergence
elif sys.argv[3]=='unintegrated':
    sc.pp.neighbors(adata)
    divergence_ref = sinkhorn_divergence.sinkhorn_divergence(
              pointcloud.PointCloud, adata[adata.obs.day==9.00].obsm['X_pca'], adata[adata.obs.day==13.5].obsm['X_pca']
          ).divergence
else:
    raise NotImplementedError
sc.tl.umap(adata)
sc.pl.umap(adata, color='day', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_pca_0900_day.png')
sc.pl.umap(adata, color='cellcluster_moscot', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_pca_0900_cell.png')

if sys.argv[3]=='integrated':
    adata_loader = OTDataLoader(1024, source_lin=adata[adata.obs['day']==9.00].obsm['X_emb'], target_lin=adata[adata.obs['day']==13.5].obsm['X_emb'])
elif sys.argv[3]=='unintegrated':
    adata_loader = OTDataLoader(1024, source_lin=adata[adata.obs['day']==9.00].obsm['X_pca'], target_lin=adata[adata.obs['day']==13.5].obsm['X_pca'])
else:
    raise NotImplementedError

neural_vf = VelocityField(
    output_dim=50,
    condition_dim=0,
    latent_embed_dim=256,
    n_frequencies=128
)
ot_solver = sinkhorn.Sinkhorn()
time_sampler = sample_uniformly
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
#TODO adapt when model selected
with open(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergences/flow/{sys.argv[1]}/{sys.argv[2]}/{sys.argv[3]}_0900_model.pt', mode='wb') as file:
   cloudpickle.dump(fm, file)
#fm.save(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergences/flow/{sys.argv[1]}/{sys.argv[2]}/{sys.argv[3]}_0900_model.pt')

adata_concat = sc.concat(
    {'09.00': adata[adata.obs.day==9.00], '09.00_push': adata[adata.obs.day==9.00], '13.50': adata[adata.obs.day==13.5]},
    label='day_umap'
)
if sys.argv[3]=='integrated':
    adata_concat.obsm["X_new"] = np.concatenate(
        (adata[adata.obs['day']==9.00].obsm['X_emb'],
         np.array(fm.transport(jnp.array(adata[adata.obs['day']==9.00].obsm['X_emb']), condition=None, forward=True)), 
         adata[adata.obs.day==13.5].obsm['X_emb']),
        axis=0
    )
elif sys.argv[3]=='unintegrated':
    adata_concat.obsm["X_new"] = np.concatenate(
        (adata[adata.obs['day']==9.00].obsm['X_pca'], 
         np.array(fm.transport(jnp.array(adata[adata.obs['day']==9.00].obsm['X_pca']), condition=None, forward=True)), 
         adata[adata.obs.day==13.5].obsm['X_pca']),
        axis=0
    )
else:
    raise NotImplementedError
del adata_concat.obsm['X_diffmap']

sc.pp.neighbors(adata_concat, use_rep='X_new')
sc.tl.umap(adata_concat)
adata_concat.write(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergences/flow/{sys.argv[1]}/{sys.argv[2]}/{sys.argv[3]}_0900_adata.h5ad')
sc.pl.umap(adata_concat, color='day_umap', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_all_0900_day.png')
sc.pl.umap(adata_concat, color='cellcluster_moscot', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_all_0900_cell.png')

adata_con_2 = adata_concat[adata_concat.obs['day_umap']!='09.00'].copy()
sc.pp.neighbors(adata_con_2, use_rep='X_new')
sc.tl.umap(adata_con_2)
sc.pl.umap(adata_con_2, color='day_umap', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_pushed_0900_day.png')
sc.pl.umap(adata_con_2, color='cellcluster_moscot', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_pushed_0900_cell.png')

divergence = pd.DataFrame(
    data={'n_obs': [sys.argv[1]], 'n_genes': [sys.argv[2]], 'time': ['09.00, 13.50'],
          'divergence': [sinkhorn_divergence.sinkhorn_divergence(
              pointcloud.PointCloud,
              adata_concat[adata_concat.obs.day_umap=='09.00_push'].obsm['X_new'],
              adata_concat[adata_concat.obs.day_umap=='13.50'].obsm['X_new']
          ).divergence],
          'divergence_ref': [divergence_ref]
         }
).to_csv(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergence_results/flow/divergence_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_0900.csv')
