import scib
import scanpy as sc
import pandas as pd
import sys

condition_key = 'batch'
label_key = 'celltype'
dataset_dict = {'gastrulation': 'gastrulation_ds', 'invito': 'invitro', 'exvito': 'exvitro'}

adata = sc.read_h5ad(f'/home/icb/jonas.flor/gastrulation_atlas/data/{dataset_dict[sys.argv[1]]}.h5ad')
adata_int = sc.read_h5ad(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/1M/{sys.argv[2]}/2/2048/{sys.argv[1]}/{sys.argv[1]}_adata.h5ad')

scib_metrics = pd.DataFrame(
    data={'dataset': [sys.argv[1]], 'n_genes': [sys.argv[2]], 'metric': ['traject_conservation']}
)
scib_metrics['value'] = scib.me.trajectory_conservation(adata, adata_int, label_key=label_key)

scib_metrics.to_csv(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/scib/results/{sys.argv[1]}_{sys.argv[2]}_traject_conservation.csv')
