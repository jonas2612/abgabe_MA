import scanpy as sc

X = sc.read_h5ad('/home/icb/jonas.flor/gastrulation_atlas/scvi/training/10k/2k_genes/integrated_adata.h5ad').X
print('X 10k cells, 2k genes')
print(X)
X = sc.read_h5ad('/home/icb/jonas.flor/gastrulation_atlas/scvi/training/10k/10k_genes/integrated_adata.h5ad').X
print('X 10k cells, 10k genes')
print(X)
X = sc.read_h5ad('/home/icb/jonas.flor/gastrulation_atlas/scvi/training/500k/2k_genes/integrated_adata.h5ad').X
print('X 500k cells, 2k genes')
print(X)
X = sc.read_h5ad('/home/icb/jonas.flor/gastrulation_atlas/scvi/training/500k/10k_genes/integrated_adata.h5ad').X
print('X 500k cells, 10k genes')
print(X)
X = sc.read_h5ad('/home/icb/jonas.flor/gastrulation_atlas/scvi/training/500k/all_genes/integrated_adata.h5ad').X
print('X 500k cells, all genes')
print(X)
