import scib
import scanpy as sc
import pandas as pd
import sys

condition_key = 'embryo_id'
label_key = 'celltype'
adata_path = f'/home/icb/jonas.flor/gastrulation_atlas/scvi/training/model_1M_final/recon/{sys.argv[1]}'

adata_int = sc.read_h5ad(f'{adata_path}/integrated_adata.h5ad')

scib_metrics = pd.DataFrame(
    data={'n_obs': [adata_int.n_obs], 'n_cells': ['1M'], 'n_genes': [sys.argv[1]], 'n_layers': [2], 'n_hidden': [2048], 'metric': ['iLISI_integrated']}
)
scib_metrics['value'] = scib.me.ilisi_graph(adata_int, batch_key=condition_key, type_='embed')

scib_metrics.to_csv(f'{adata_path}/metrics/metrics_iLISI_integrated.csv')
