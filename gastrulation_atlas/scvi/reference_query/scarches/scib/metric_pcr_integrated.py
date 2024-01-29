import scib
import scanpy as sc
import pandas as pd
import sys

condition_key = 'batch'
label_key = 'celltype'
adata_int = sc.read_h5ad(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/1M/{sys.argv[2]}/2/2048/{sys.argv[1]}/{sys.argv[1]}_adata.h5ad')

scib_metrics = pd.DataFrame(
    data={'dataset': [sys.argv[1]], 'n_genes': [sys.argv[2]], 'metric': ['pcr_integrated']}
)
scib_metrics['value'] = scib.me.pcr(adata_int, covariate=condition_key, embed='X_emb', recompute_pca=False)

scib_metrics.to_csv(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/scib/results/{sys.argv[1]}_{sys.argv[2]}_pcr_integrated.csv')
