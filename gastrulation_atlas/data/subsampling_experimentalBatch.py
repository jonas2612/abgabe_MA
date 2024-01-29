import scanpy as sc

adata = sc.read('/lustre/groups/ml01/workspace/monge_velo/data/adata_JAX_dataset_12.h5ad')
adata_tmp1 = adata[adata.obs["experimental_batch"]!='run_22']