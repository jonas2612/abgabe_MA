import scib
import scanpy as sc
import pandas as pd
import sys

condition_key = 'batch'
label_key = 'celltype'
dataset_dict = {'gastrulation': 'gastrulation_ds', 'invito': 'invitro', 'exvito': 'exvitro'}

adata = sc.read_h5ad(f'/home/icb/jonas.flor/gastrulation_atlas/data/{dataset_dict[sys.argv[1]]}.h5ad')

scib_metrics = pd.DataFrame(
    data={'dataset': [sys.argv[1]], 'n_genes': [adata.n_vars], 'metric': ['pcr_unintegrated']}
)
scib_metrics['value'] = scib.me.pcr(adata, covariate=condition_key, recompute_pca=False)

scib_metrics.to_csv(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/scib/results/{sys.argv[1]}_pcr_unintegrated.csv')
