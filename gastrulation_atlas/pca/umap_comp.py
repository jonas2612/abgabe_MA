import scanpy as sc
adata = sc.read("/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas_pca.h5ad")
sc.pp.neighbors(adata)
sc.tl.umap(adata)
adata.write("/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas_neighbors.h5ad")