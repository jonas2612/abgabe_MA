import scanpy as sc
import sys

adata = sc.read('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/gastrulation_atlas.h5ad', backed='r')
adata_val = sc.read('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/training/validationset_gastrulation_atlas.h5ad', backed='r')

adata = adata[[~x.isin(adata_val.obs.cell_id) for x in adata.obs.cell_id]]

sc.pp.subsample(adata, n_obs=sys.argv[1])
adata.write()