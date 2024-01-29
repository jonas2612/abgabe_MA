import scanpy as sc
from moscot.problems.time import TemporalNeuralProblem
from ott.tools import sinkhorn_divergence
from ott.geometry import pointcloud
import numpy as np
import pandas as pd

import sys

adata = sc.read_h5ad(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/training/{sys.argv[1]}/{sys.argv[2]}/{sys.argv[3]}_adata.h5ad')

adata = adata[[x in [8.5, 12] for x in adata.obs.day]]

if sys.argv[3]=='integrated':
    sc.pp.neighbors(adata, use_rep='X_emb')
    divergence_ref = sinkhorn_divergence.sinkhorn_divergence(
              pointcloud.PointCloud, adata[adata.obs.day==8.5].obsm['X_emb'], adata[adata.obs.day==12].obsm['X_emb']
          ).divergence
elif sys.argv[3]=='unintegrated':
    sc.pp.neighbors(adata)
    divergence_ref = sinkhorn_divergence.sinkhorn_divergence(
              pointcloud.PointCloud, adata[adata.obs.day==8.5].obsm['X_pca'], adata[adata.obs.day==12].obsm['X_pca']
          ).divergence
else:
    raise NotImplementedError
sc.tl.umap(adata)
sc.pl.umap(adata, color='day', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_pca_85.png')

problem = TemporalNeuralProblem(adata=adata)
if sys.argv[3]=='integrated':
    problem = problem.prepare(time_key='day', joint_attr="X_emb")
elif sys.argv[3]=='unintegrated':
    problem = problem.prepare(time_key='day', joint_attr="X_pca")
else:
    raise NotImplementedError
problem.solve()

if sys.argv[3]=='integrated':
    adata_concat = sc.concat(
        [adata[adata.obs.day==8.5], adata[adata.obs.day==12]],
    )  
    adata_concat.obsm["X_new"] = np.concatenate(
        (np.array(problem[list(problem)[0]].solution.push(adata[adata.obs.day==8.5].obsm["X_emb"])), adata[adata.obs.day==12].obsm['X_emb']),
        axis=0
    )
elif sys.argv[3]=='unintegrated':
    adata_concat = sc.concat(
        [adata[adata.obs.day==8.5], adata[adata.obs.day==12]],
    )  
    adata_concat.obsm["X_new"] = np.concatenate(
        (np.array(problem[list(problem)[0]].solution.push(adata[adata.obs.day==8.5].obsm["X_pca"])), adata[adata.obs.day==12].obsm['X_pca']),
        axis=0
    )
del adata_concat.obsm['X_diffmap']
    
sc.pp.neighbors(adata_concat, use_rep='X_new')
sc.tl.umap(adata_concat)
sc.pl.umap(adata_concat, color='day', save=f'_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_pushed_85.png')

divergence = pd.DataFrame(
    data={'n_obs': [sys.argv[1]], 'n_genes': [sys.argv[2]], 'time': ['8.5, 12.0'],
          'divergence': [sinkhorn_divergence.sinkhorn_divergence(
              pointcloud.PointCloud, adata_concat[adata_concat.obs.day==8.5].obsm['X_new'], adata_concat[adata_concat.obs.day==12].obsm['X_new']
          ).divergence],
          'divergence_ref': [divergence_ref]
         }
).to_csv(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergence_results/moscot_not/divergence_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_85.csv')