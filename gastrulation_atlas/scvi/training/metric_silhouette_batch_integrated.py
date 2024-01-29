import scib
import scanpy as sc
import pandas as pd
import sys

condition_key = 'embryo_id'
label_key = 'celltype'
adata_path = f'/home/icb/jonas.flor/gastrulation_atlas/scvi/training/{sys.argv[1]}/{sys.argv[2]}/{sys.argv[3]}/{sys.argv[4]}'

adata_int = sc.read_h5ad(f'{adata_path}/integrated_adata.h5ad')

scib_metrics = pd.DataFrame(
    data={'n_obs': [adata_int.n_obs], 'n_cells': [sys.argv[1]], 'n_genes': [sys.argv[2]], 'n_layers': [sys.argv[3]], 'n_hidden': [sys.argv[4]], 'metric': ['silhouette_batch_integrated']}
)
scib_metrics['value'] = scib.me.silhouette_batch(adata_int, batch_key=condition_key, label_key=label_key, embed='X_emb', return_all=True)[0]

scib_metrics.to_csv(f'{adata_path}/metrics/metrics_silhouette_batch_integrated.csv')
