import scanpy as sc

adata = sc.read('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/atlas_umap/gastrulation_atlas.h5ad')

sc.pp.normalize_total(adata)

adata.write('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/atlas_umap/gastrulation_atlas.h5ad')