import cloudpickle
import scanpy as sc

adata = sc.read('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas.h5ad')
with open('/home/icb/jonas.flor/ALT_gastrulation_atlas/pca/pca.pkl', mode='rb') as file:
   pca = cloudpickle.load(file)
adata.obsm['X_pca'] = pca[0]

sc.pp.neighbors(adata)

adata.write('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas.h5ad')
