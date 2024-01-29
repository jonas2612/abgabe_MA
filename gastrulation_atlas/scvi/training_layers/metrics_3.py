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
scib_metrics['iso_labels_integrated'] = scib.me.isolated_labels_f1(adata_int, batch_key=condition_key, label_key=label_key, embed=None)

scib.me.cluster_optimal_resolution(adata, label_key=label_key, cluster_key='Leiden')
scib.me.cluster_optimal_resolution(adata_int, label_key=label_key, cluster_key='Leiden')

scib_metrics['ari_unintegrated'] = scib.me.ari(adata, cluster_key='Leiden', label_key=label_key)
scib_metrics['ari_integrated'] = scib.me.ari(adata_int, cluster_key='Leiden', label_key=label_key)
scib_metrics['nmi_unintegrated'] = scib.me.nmi(adata, cluster_key='Leiden', label_key=label_key)
scib_metrics['nmi_integrated'] = scib.me.nmi(adata_int, cluster_key='Leiden', label_key=label_key)

scib_metrics.to_csv(f'/home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/{sys.argv[1]}/metrics/scib_metrics.csv')
