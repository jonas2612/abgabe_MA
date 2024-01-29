import scanpy as sc

adata = sc.read('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/gastrulation_atlas.h5ad', backed='r')

sc.pp.subsample(adata, n_obs=100000)

adata.write('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/training/validationset_gastrulation_atlas.h5ad')