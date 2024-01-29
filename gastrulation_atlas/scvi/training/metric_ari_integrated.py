import scib
import scanpy as sc
import pandas as pd
import sys

condition_key = 'embryo_id'
label_key = 'celltype'
adata_path = f'/home/icb/jonas.flor/gastrulation_atlas/scvi/training/{sys.argv[1]}/{sys.argv[2]}/{sys.argv[3]}/{sys.argv[4]}'

adata_int = sc.read_h5ad(f'{adata_path}/integrated_adata.h5ad')

scib_metrics = pd.DataFrame(
    data={'n_obs': [adata_int.n_obs], 'n_cells': [sys.argv[1]], 'n_genes': [sys.argv[2]], 'n_layers': [sys.argv[3]], 'n_hidden': [sys.argv[4]], 'metric': ['ari_integrated']}
)
scib.me.cluster_optimal_resolution(adata_int, label_key=label_key, cluster_key='Leiden')

scib_metrics['value'] = scib.me.ari(adata_int, cluster_key='Leiden', label_key=label_key)

scib_metrics.to_csv(f'{adata_path}/metrics/metrics_ari_integrated.csv')
