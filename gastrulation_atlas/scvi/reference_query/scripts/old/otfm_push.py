import scanpy as sc
import numpy as np
import cloudpickle
import jax.numpy as jnp
import sys

adata = sc.read_h5ad(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/1M/{sys.argv[2]}/2/2048/{sys.argv[1]}/{sys.argv[1]}_adata.h5ad')

if sys.argv[5]=='weighted':
    end='_w'
else:
    end=''

if sys.argv[3]=='integrated':
    sc.pp.neighbors(adata, use_rep='X_emb')
else:
    sc.pp.neighbors(adata, use_rep='X_pca')
sc.tl.umap(adata)
sc.pl.umap(adata, color='day', save=f'_{sys.argv[1]}_1M_{sys.argv[2]}_2_2048_{sys.argv[3]}_{sys.argv[4]}{sys.argv[5]}_pca_cond_day.png')
sc.pl.umap(adata, color='celltype', save=f'_{sys.argv[1]}_1M_{sys.argv[2]}_2_2048_{sys.argv[3]}_{sys.argv[4]}{sys.argv[5]}_pca_cond_cell.png')

if sys.argv[4]=='recon':
    with open(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergences/flow/1M/{sys.argv[2]}/2/2048/{sys.argv[3]}_cond_model_{end}.pt', mode='rb') as file:
       fm = cloudpickle.load(file)
else:
    with open(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergences/flow/1M/{sys.argv[2]}/2/2048/{sys.argv[3]}_cond_model.pt', mode='rb') as file:
       fm = cloudpickle.load(file)


adata_concat = sc.concat({'old': adata, 'new': adata[adata.obs.day==8.5]},label='datasets')
adata_concat.obs.loc[adata_concat.obs.datasets=='new', 'day'] = 8.75

if sys.argv[3]=='integrated':
    adata_concat.obsm["X_new"] = np.concatenate(
        (adata.obsm['X_emb'],
         np.array(fm.transport(jnp.array(adata[adata.obs['day']==8.5].obsm['X_emb']), 
                               condition=np.expand_dims(adata[adata.obs.day==8.5].obs.day.values, axis=1), 
                               forward=True)
                  )),
        axis=0
    )
elif sys.argv[3]=='unintegrated':
    adata_concat.obsm["X_new"] = np.concatenate(
        (adata.obsm['X_pca'],
         np.array(fm.transport(jnp.array(adata[adata.obs['day']==8.5].obsm['X_pca']), 
                               condition=np.expand_dims(adata[adata.obs.day==8.5].obs.day.values, axis=1), 
                               forward=True)
                  )),
        axis=0
    )
else:
    raise NotImplementedError

sc.pp.neighbors(adata_concat, use_rep='X_new')
sc.tl.umap(adata_concat)
adata_concat.write(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/flow/cond_adata_{sys.argv[1]}_{sys.argv[2]}_{sys.argv[3]}_{sys.argv[4]}{sys.argv[5]}.h5ad')
sc.pl.umap(adata_concat, color='day', save=f'_{sys.argv[1]}_1M_{sys.argv[2]}_2_2048_{sys.argv[3]}_{sys.argv[4]}{sys.argv[5]}_all_cond_day.png')
sc.pl.umap(adata_concat, color='celltype', save=f'_{sys.argv[1]}_1M_{sys.argv[2]}_2_2048_{sys.argv[3]}_{sys.argv[4]}{sys.argv[5]}_all_cond_cell.png')
