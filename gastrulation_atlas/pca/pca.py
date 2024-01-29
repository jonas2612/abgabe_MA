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

data = ad.read_h5ad("/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas.h5ad", backed='r').X
batch_size = 40429

def read_X(data, pos):
    return data[pos:pos+batch_size, :].toarray()

X = da.concatenate([da.from_delayed(dask.delayed(read_X)(data, pos), (batch_size, data.shape[1]), dtype='f4') for pos in range(0, data.shape[0], batch_size)])
X.map_blocks(csr_matrix).persist().rechunk((8192, -1))

dask.config.set(pool=ThreadPool(30))

n_comps = 50
pca = IncrementalPCA(n_components=n_comps, iterated_power=3)
pca = da.compute(pca.fit_transform(X))

with open('/home/icb/jonas.flor/gastrulation_atlas/pca/pca.pkl', mode='wb') as file:
    cloudpickle.dump(pca, file)
