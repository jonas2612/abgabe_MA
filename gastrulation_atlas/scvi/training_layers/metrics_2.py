import scib
import scanpy as sc
import pandas as pd
import sys

condition_key = 'embryo_id'
label_key = 'celltype'

adata = sc.read_h5ad(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/{sys.argv[1]}/unintegrated_adata.h5ad')
adata_int = sc.read_h5ad(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/{sys.argv[1]}/integrated_adata.h5ad')

scib_metrics = pd.DataFrame(
    data={'n_obs': [adata.n_obs]}
)
scib_metrics['ASW_integrated'] = scib.me.isolated_labels_asw(adata_int, label_key=label_key, batch_key=condition_key, embed='X_emb')
scib_metrics['cLISI_unintegrated'] = scib.me.clisi_graph(adata, label_key=label_key, type_='full')
scib_metrics['cLISI_integrated'] = scib.me.clisi_graph(adata_int, label_key=label_key, type_='embed')
scib_metrics['iLISI_unintegrated'] = scib.me.ilisi_graph(adata, batch_key=condition_key, type_='full')
scib_metrics['iLISI_integrated'] = scib.me.ilisi_graph(adata_int, batch_key=condition_key, type_='embed')

scib_metrics.to_csv(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/{sys.argv[1]}/metrics/scib_metrics.csv')
