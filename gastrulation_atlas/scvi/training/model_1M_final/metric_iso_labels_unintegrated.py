import scib
import scanpy as sc
import pandas as pd
import sys

condition_key = 'embryo_id'
label_key = 'celltype'
adata_path = f'/home/icb/jonas.flor/gastrulation_atlas/scvi/training/model_1M_final/recon/{sys.argv[1]}'

adata = sc.read_h5ad(f'{adata_path}/unintegrated_adata.h5ad')

scib_metrics = pd.DataFrame(
    data={'n_obs': [adata.n_obs], 'n_cells': ['1M'], 'n_genes': [sys.argv[1]], 'n_layers': [2], 'n_hidden': [2048], 'metric': ['iso_label_f1_unintegrated']}
)
scib_metrics['value'] = scib.me.isolated_labels_f1(adata, batch_key=condition_key, label_key=label_key, embed=None)

scib_metrics.to_csv(f'{adata_path}/metrics/metrics_iso_labels_unintegrated.csv')
