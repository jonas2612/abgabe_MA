import scanpy as sc

adata = sc.read_h5ad('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/paper_umap/gastrulation_atlas_paper_leiden.h5ad', backed='r')

sc.tl.umap(adata, min_dist=0.1)
sc.pl.umap(adata, color='day' save='day.png')
sc.pl.umap(adata, color='cellcluster_moscot', save='cl_moscot.png')
sc.pl.umap(adata, color='cell_cluster', save='cl_org.png')

adata.write('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/paper_umap/gastrulation_atlas_paper_umap.h5ad')