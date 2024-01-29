from pathlib import Path

import h5py
from scipy import sparse

import anndata as ad
from anndata._core.sparse_dataset import SparseDataset
from anndata.experimental import read_elem, write_elem


def read_everything_but_X(pth) -> ad.AnnData:
    attrs = ["obs", "var", "obsm", "varm", "obsp", "varp", "uns"]
    with h5py.File(pth) as f:
        adata = ad.AnnData(**{k: read_elem(f[k]) for k in attrs})
    return adata


def concat_on_disk(input_pths: list[Path], output_pth: Path):
    """
    Params
    ------
    input_pths
        Paths to h5ad files which will be concatenated
    output_pth
        File to write as a result
    """
    annotations = ad.concat([read_everything_but_X(pth) for pth in input_pths])

    annotations.write_h5ad(output_pth)
    n_variables = annotations.shape[1]
    
    del annotations

    with h5py.File(output_pth, "a") as target:
        dummy_X = sparse.csr_matrix((0, n_variables), dtype="float64")
        dummy_X.indptr = dummy_X.indptr.astype("int64") # Guarding against overflow for very large datasets

        write_elem(target, "X", dummy_X)
        mtx = SparseDataset(target["X"])
        for p in pths:
            with h5py.File(p, "r") as src:
                mtx.append(SparseDataset(src["X"]))

pths = ['/home/icb/jonas.flor/gastrulation_atlas/data/gast_data_12_ohne22.h5ad',
        '/home/icb/jonas.flor/gastrulation_atlas/data/gast_data_34_ohne22.h5ad']
concat_on_disk(pths, "/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas_without_22.h5ad")
