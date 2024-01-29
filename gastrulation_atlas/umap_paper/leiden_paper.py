import scanpy as sc

adata = sc.read_h5ad('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/paper_umap/gastrulation_atlas_paper_neighbor.h5ad', backed='r')

sc.tl.leiden(adata)

adata = sc.read_h5ad('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/paper_umap/gastrulation_atlas_paper_leiden.h5ad')