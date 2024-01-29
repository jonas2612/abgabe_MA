import scanpy as sc
import sys

adata_path = f'/home/icb/jonas.flor/gastrulation_atlas/scvi/training/model_1M_final/recon/{sys.argv[1]}'

#unintegrated adata preprocessing
adata = sc.read_h5ad(f'{adata_path}/unintegrated_adata.h5ad')

sc.pp.normalize_total(adata)
sc.pp.log1p(adata)

adata.obs.day = [float(x[1:]) for x in adata.obs.day]
adata.obs.day[adata.obs.day == 0.] = 19

sc.pp.neighbors(adata, use_rep='X_pca')
adata.uns['iroot'] = adata.obs.index.get_loc(
    adata[(adata.obs.day == 8.5) & (adata.obs.celltype == 'Lateral plate and intermediate mesoderm')]
    .obs.first_valid_index()
)
sc.tl.dpt(adata)

adata.write(f'{adata_path}/unintegrated_adata.h5ad')
del adata


#integrated adata preprocessing
adata = sc.read_h5ad(f'{adata_path}/integrated_adata.h5ad')

sc.pp.normalize_total(adata)
sc.pp.log1p(adata)

adata.obs.day = [float(x[1:]) for x in adata.obs.day]
adata.obs.day[adata.obs.day == 0.] = 19

sc.pp.neighbors(adata, use_rep='X_emb')
adata.uns['iroot'] = adata.obs.index.get_loc(
    adata[(adata.obs.day == 8.5) & (adata.obs.celltype == 'Lateral plate and intermediate mesoderm')]
    .obs.first_valid_index()
)
sc.tl.dpt(adata)

adata.write(f'{adata_path}/integrated_adata.h5ad')
