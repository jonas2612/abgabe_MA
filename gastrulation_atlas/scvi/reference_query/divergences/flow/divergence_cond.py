from ott.neural.flows.models import VelocityField
from ott.neural.flows.flows import ConstantNoiseFlow
from ott.neural.flows.samplers import sample_uniformly
from ott.neural.flows.otfm import OTFlowMatching
from ott.solvers.linear import sinkhorn
from ott.tools import sinkhorn_divergence
from ott.geometry import pointcloud
from ott.neural.data.dataloaders import OTDataLoader, ConditionalDataLoader

import optax
import scanpy as sc

import jax.numpy as jnp

import numpy as np
import pandas as pd

from ott.tools import sinkhorn_divergence
from ott.geometry import pointcloud

import anndata as ad
from fractions import Fraction
import cloudpickle

import sys

adata = sc.read_h5ad(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/training/{sys.argv[1]}/{sys.argv[2]}/{sys.argv[3]}/{sys.argv[4]}/{sys.argv[5]}_adata.h5ad')
day_sort=adata.obs.day.unique()
day_sort.sort()

if sys.argv[5]=='integrated':
    sc.pp.neighbors(adata, use_rep='X_emb')
    divergence_ref = sinkhorn_divergence.sinkhorn_divergence(
              pointcloud.PointCloud, adata[adata.obs.day==10.25].obsm['X_emb'], adata[adata.obs.day==10.5].obsm['X_emb']
          ).divergence
elif sys.argv[5]=='unintegrated':
    sc.pp.neighbors(adata)
    divergence_ref = sinkhorn_divergence.sinkhorn_divergence(
              pointcloud.PointCloud, adata[adata.obs.day==10.25].obsm['X_pca'], adata[adata.obs.day==10.5].obsm['X_pca']
          ).divergence
else:
    raise NotImplementedError
sc.tl.umap(adata)
sc.pl.umap(adata, color='day', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_{sys.argv[4]}_{sys.argv[5]}_pca_cond_day.png')
sc.pl.umap(adata, color='cellcluster_moscot', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_{sys.argv[4]}_{sys.argv[5]}_pca_cond_cell.png')

dataloaders = {}
if sys.argv[5]=='integrated':
    for day_ind in range(day_sort.shape[0]-1):
        dataloaders[day_sort[day_ind]] = OTDataLoader(
            1024, 
            source_lin=adata[adata.obs.day==day_sort[day_ind]].obsm['X_emb'], 
            target_lin=adata[adata.obs.day==day_sort[day_ind+1]].obsm['X_emb'], 
            source_conditions=np.expand_dims(adata[adata.obs.day==day_sort[day_ind]].obs.day.values, axis=1)
            )
elif sys.argv[5]=='unintegrated':
    for day_ind in range(day_sort.shape[0]-1):
        dataloaders[day_sort[day_ind]] = OTDataLoader(
            1024, 
            source_lin=adata[adata.obs.day==day_sort[day_ind]].obsm['X_pca'], 
            target_lin=adata[adata.obs.day==day_sort[day_ind+1]].obsm['X_pca'], 
            source_conditions=np.expand_dims(adata[adata.obs.day==day_sort[day_ind]].obs.day.values, axis=1)
            )
else:
    raise NotImplementedError
cond_prob = np.ones(day_sort.shape[0]-1)/(day_sort.shape[0]-1)
cond_prob[0] = 1-sum(cond_prob[1:])
adata_loader = ConditionalDataLoader(dataloaders, cond_prob)

neural_vf = VelocityField(
    output_dim=50,
    condition_dim=1,
    latent_embed_dim=256,
    n_frequencies=128
)
ot_solver = sinkhorn.Sinkhorn()
time_sampler = sample_uniformly
optimizer = optax.adam(learning_rate=1e-4)
fm = OTFlowMatching(
    neural_vf,
    input_dim=50,
    cond_dim=1,
    iterations=100000,
    valid_freq=1000,
    ot_solver=ot_solver,
    flow=ConstantNoiseFlow(0.0),
    time_sampler=time_sampler,
    optimizer=optimizer
)
fm(adata_loader, adata_loader)
with open(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergences/flow/{sys.argv[1]}/{sys.argv[2]}/{sys.argv[3]}/{sys.argv[4]}/{sys.argv[5]}_cond_model.pt', mode='wb') as file:
   cloudpickle.dump(fm, file)

adata_concat = sc.concat(
    {'10.25': adata[adata.obs.day==10.25], '10.25_push': adata[adata.obs.day==10.25], '10.50': adata[adata.obs.day==10.5]},
    label='day_umap'
)
if sys.argv[5]=='integrated':
    adata_concat.obsm["X_new"] = np.concatenate(
        (adata[adata.obs['day']==10.25].obsm['X_emb'],
         np.array(fm.transport(jnp.array(adata[adata.obs['day']==10.25].obsm['X_emb']), 
                               condition=np.expand_dims(adata[adata.obs.day==10.25].obs.day.values, axis=1), 
                               forward=True)
                  ), 
         adata[adata.obs.day==10.5].obsm['X_emb']),
        axis=0
    )
elif sys.argv[5]=='unintegrated':
    adata_concat.obsm["X_new"] = np.concatenate(
        (adata[adata.obs['day']==10.25].obsm['X_pca'],
         np.array(fm.transport(jnp.array(adata[adata.obs['day']==10.25].obsm['X_pca']), 
                               condition=np.expand_dims(adata[adata.obs.day==10.25].obs.day.values, axis=1), 
                               forward=True)
                  ), 
         adata[adata.obs.day==10.5].obsm['X_pca']),
        axis=0
    )
else:
    raise NotImplementedError
del adata_concat.obsm['X_diffmap']

sc.pp.neighbors(adata_concat, use_rep='X_new')
sc.tl.umap(adata_concat)
adata_concat.write(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergences/flow/{sys.argv[1]}/{sys.argv[2]}/{sys.argv[3]}/{sys.argv[4]}/{sys.argv[5]}_cond_adata.h5ad')
sc.pl.umap(adata_concat, color='day_umap', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_{sys.argv[4]}_{sys.argv[5]}_all_cond_day.png')
sc.pl.umap(adata_concat, color='cellcluster_moscot', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_{sys.argv[4]}_{sys.argv[5]}_all_cond_cell.png')

adata_con_2 = adata_concat[adata_concat.obs['day_umap']!='10.25'].copy()
sc.pp.neighbors(adata_con_2, use_rep='X_new')
sc.tl.umap(adata_con_2)
sc.pl.umap(adata_con_2, color='day_umap', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_{sys.argv[4]}_{sys.argv[5]}_pushed_cond_day.png')
sc.pl.umap(adata_con_2, color='cellcluster_moscot', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_{sys.argv[4]}_{sys.argv[5]}_pushed_cond_cell.png')

divergence = pd.DataFrame(
    data={'n_obs': [sys.argv[1]], 'n_genes': [sys.argv[2]], 'time': ['cond'], 'layers': [sys.argv[3]], 'hidden': [sys.argv[4]], 'integrated': [True if sys.argv[5]=="integrated" else False],
          'divergence': [sinkhorn_divergence.sinkhorn_divergence(
              pointcloud.PointCloud,
              adata_concat[adata_concat.obs.day_umap=='10.25_push'].obsm['X_new'],
              adata_concat[adata_concat.obs.day_umap=='10.50'].obsm['X_new']
          ).divergence],
          'divergence_ref': [divergence_ref]
         }
).to_csv(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergence_results/flow/divergence_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_{sys.argv[4]}_{sys.argv[5]}_cond.csv')
