import scanpy as sc
import cloudpickle

adata = sc.read('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas.h5ad')
sc.pp.normalize_total(adata)
sc.pp.log1p(adata, chunked=True, chunk_size=10000)
sc.pp.highly_variable_genes(adata, n_top_genes=2500)
sc.pp.scale(adata)

with open('X.pkl', mode='wb') as file:
   cloudpickle.dump(adata.X, file)