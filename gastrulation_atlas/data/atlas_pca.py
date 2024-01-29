import numpy as np
import pandas as pd

import scanpy
import anndata as ad
import cloudpickle

import dask
import dask.array as da

from dask_ml.decomposition import IncrementalPCA
from multiprocessing.pool import ThreadPool
from scipy.sparse import csr_matrix

dask.config.set(pool=ThreadPool(1))

print("start read data")
data = ad.read_h5ad("/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/gastrulation_atlas_normalized.h5ad", backed='r').X
batch_size = 40429
print("end read data")

def read_X(data, pos):
    return data[pos:pos+batch_size, :].toarray()

print("process X")
X = da.concatenate([da.from_delayed(dask.delayed(read_X)(data, pos), (batch_size, data.shape[1]), dtype='f4') for pos in range(0, data.shape[0], batch_size)]).rechunk((8192, -1))
del data
#X = X.persist().rechunk((8192, -1))
print("process X finished")

dask.config.set(pool=ThreadPool(30))

print("compute pca")
n_comps = 50
pca = IncrementalPCA(n_components=n_comps, iterated_power=3)
pca = da.compute(pca.fit_transform(X))[0]
del X
print("compute pca ended")

adata = ad.read_h5ad("/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/gastrulation_atlas.h5ad")
adata.obsm['X_pca'] = pca
adata.write('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/gastrulation_atlas_pca.h5ad')