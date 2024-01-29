from scanpy import read_h5ad
import numpy as np
import pandas as pd

data = ['1/2048', '1/4096', '1/8192', '2/1024', '2/2048', '2/4096', '2/8192']
genes = ['2k_genes', '10k_genes', 'all_genes']

vars = {}
for d in data:
	for g in genes:
		try:
			path = f'/home/icb/jonas.flor/gastrulaton_atlas/scvi/training/1M/{g}/{d}/integrated_adata.h5ad'
			print(path)
			adata = read_h5ad(path)
			vars[f'{g}/{d}'] = np.var(adata.obsm['X_emb'], axis=1)
		except FileNotFoundError:
			pass

pd.DataFrame(data=vars).to_csv('/home/icb/jonas.flor/gastrulation_atlas/scvi/training/variances_1M.csv')
