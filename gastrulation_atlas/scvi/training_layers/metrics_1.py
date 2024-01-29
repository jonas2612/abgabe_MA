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
scib_metrics['hgv_overlap'] = scib.me.hvg_overlap(adata, adata_int, batch_key=condition_key)
scib_metrics['pcr_unintegrated'] = scib.me.pcr(adata, covariate=condition_key, recompute_pca=False)
scib_metrics['pcr_integrated'] = scib.me.pcr(adata_int, covariate=condition_key, embed='X_emb', recompute_pca=False)
scib_metrics['traject_conversation'] = scib.me.trajectory_conservation(adata, adata_int, label_key=label_key)
scib_metrics['graph_connectivity_unintegrated'] = scib.me.graph_connectivity(adata, label_key=label_key)
scib_metrics['graph_connectivity_integrated'] = scib.me.graph_connectivity(adata_int, label_key=label_key)
scib_metrics['silhouette_unintegrated'] = scib.me.silhouette(adata, label_key=label_key, embed='X_pca')
scib_metrics['silhouette_integrated'] = scib.me.silhouette(adata_int, label_key=label_key, embed='X_emb')
scib_metrics['silhouette_batch_unintegrated'] = scib.me.silhouette_batch(adata, batch_key=condition_key, label_key=label_key, embed='X_pca', return_all=True)[0]
scib_metrics['silhouette_batch_integrated'] = scib.me.silhouette_batch(adata_int, batch_key=condition_key, label_key=label_key, embed='X_emb', return_all=True)[0]
scib_metrics['ASW_unintegrated'] = scib.me.isolated_labels_asw(adata, label_key=label_key, batch_key=condition_key, embed='X_pca')
scib_metrics['iso_labels_unintegrated'] = scib.me.isolated_labels_f1(adata, batch_key=condition_key, label_key=label_key, embed=None)

scib_metrics.to_csv(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/{sys.argv[1]}/metrics/scib_metrics.csv')
