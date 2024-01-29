import scanpy as sc

base_path = '/home/icb/jonas.flor/gastrulation_atlas/scvi'
cells = ['100k', '10k', '500k', '1M']
genes = ['2k', '10k', 'all']

for c in cells:
    for g in genes:
        adata = sc.read_h5ad(f'{base_path}/training/{c}/{g}_genes/unintegrated_adata.h5ad')
        sc.tl.umap(adata)
        sc.pl.umap(adata, color='cellcluster_moscot', save=f'_{c}_{g}_un.png')
        adata = sc.read_h5ad(f'{base_path}/training/{c}/{g}_genes/integrated_adata.h5ad')
        sc.tl.umap(adata)
        sc.pl.umap(adata, color='cellcluster_moscot', save=f'_{c}_{g}_in.png')