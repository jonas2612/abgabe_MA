from typing import Dict

import scvi
import scanpy as sc
import pandas as pd
import numpy as np
import anndata as ad
from scipy.sparse import csr_matrix, vstack

import sys

def query_and_subsetting(query_vars: Dict, ref_model: str) -> ad.AnnData:
    query = sc.read_h5ad(query_vars['path'])
    query.obs['embryo_id'] = query.obs['batch']
    cells = query.uns['celltype_colors']
    days = query.uns['day_colors']
    batch = query.uns['batch_colors']
    del query.varm
    
    scvi.model.SCVI.prepare_query_anndata(query, ref_model)
    model = scvi.model.SCVI.load_query_data(
        query,
        ref_model,
        freeze_dropout = True,
        inplace_subset_query_vars=True
    )
    model.train(max_epochs=200, plan_kwargs=dict(weight_decay=0.0))
    model.save(query_vars['surgery_path'], overwrite=True)
    
    query_adata = ad.AnnData(model.get_normalized_expression())
    query_adata.obsm['X_emb'] = model.get_latent_representation()
    query_adata.obsm['X_umap'] = query.obsm['X_umap']
    
    query_adata.obs['day'] = query.obs.day
    query_adata.obs['celltype'] = query.obs.celltype
    query_adata.obs['batch'] = query.obs['batch']
    query_adata.uns['celltype_colors'] = cells
    query_adata.uns['day_colors'] = days
    query_adata.uns['batch_colors'] = batch
    return query_adata


dataset = sys.argv[1]
ref_path = f'/home/icb/jonas.flor/gastrulation_atlas/scvi/training/{sys.argv[2]}/{sys.argv[3]}/{sys.argv[4]}/{sys.argv[5]}'
    
if dataset=='gastrulation':
    gastrulation = {
        'path': f'/home/icb/jonas.flor/gastrulation_atlas/data/gastrulation_ds.h5ad',
        'save_path': f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/{sys.argv[2]}/{sys.argv[3]}/{sys.argv[4]}/{sys.argv[5]}/gastrulation/gastrulation_adata.h5ad',
        'surgery_path': f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/{sys.argv[2]}/{sys.argv[3]}/{sys.argv[4]}/{sys.argv[5]}/gastrulation'
    }
    query = query_and_subsetting(gastrulation, ref_path)
    query.X = csr_matrix(query.X)
    query.write(gastrulation['save_path'])
    
elif dataset=='invito':
    invito = {
        'path': f'/home/icb/jonas.flor/gastrulation_atlas/data/invitro.h5ad',
        'save_path': f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/{sys.argv[2]}/{sys.argv[3]}/{sys.argv[4]}/{sys.argv[5]}/invito/invito_adata.h5ad',
        'surgery_path': f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/{sys.argv[2]}/{sys.argv[3]}/{sys.argv[4]}/{sys.argv[5]}/invito'
    }
    query = query_and_subsetting(invito, ref_path)
    query.X = csr_matrix(query.X)
    query.write(invito['save_path'])
    
elif dataset=='exvito':
    exvito = {
        'path': f'/home/icb/jonas.flor/gastrulation_atlas/data/exvitro.h5ad',
        'save_path': f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/{sys.argv[2]}/{sys.argv[3]}/{sys.argv[4]}/{sys.argv[5]}/exvito/exvito_adata.h5ad',
        'surgery_path': f'/home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/{sys.argv[2]}/{sys.argv[3]}/{sys.argv[4]}/{sys.argv[5]}/exvito'
    }
    query = query_and_subsetting(exvito, ref_path)
    query.X = csr_matrix(query.X)
    query.write(exvito['save_path'])
