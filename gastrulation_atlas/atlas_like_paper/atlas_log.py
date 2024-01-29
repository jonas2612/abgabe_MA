import scanpy as sc

adata = sc.read('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/atlas_umap/gastrulation_atlas.h5ad')

sc.pp.log1p(adata, chunked=True, chunk_size=65536)

adata.write('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/atlas_umap/gastrulation_atlas.h5ad')