import scanpy as sc

adata = sc.read_h5ad('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/paper_umap/gastrulation_atlas_paper_pca.h5ad', backed='r')

sc.pp.neighbors(adata, n_neighbors=50)

adata.write('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/paper_umap/gastrulation_atlas_paper_neighbor.h5ad')