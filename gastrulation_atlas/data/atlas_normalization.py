import scanpy as sc

adata = sc.read_h5ad('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/gastrulation_atlas.h5ad')

sc.pp.normalize_total(adata)
sc.pp.log1p(adata, chunked=True, chunk_size=8198)

adata.write('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/gastrulation_atlas_normalized.h5ad')