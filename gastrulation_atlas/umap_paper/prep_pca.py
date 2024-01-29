import scanpy as sc

adata = sc.read_h5ad("/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/gastrulation_atlas_normalized.h5ad")

sc.pp.highly_variable_genes(
        adata,
        n_top_genes=2500,
        subset=True
    )

sc.pp.scale(adata)
adata.write("/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/paper_umap/gastrulation_atlas_scaled.h5ad")
