import scvi
import scanpy as sc
import numpy as np
import pandas as pd
import anndata as ad
import sys

condition_key = 'embryo_id'
label_key = 'cellcluster_moscot'
adata_path = f'/home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/{sys.argv[1]}'
metrics_path = f'/home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/{sys.argv[1]}/metrics'
n_obs=500000

if sys.argv[1]=='5':
    n_layers=5
elif sys.argv[1]=='15':
    n_layers=15
elif sys.argv[1]=='20':
    n_layers=20

adata = sc.read_h5ad(f'/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/training/adata_500k.h5ad')
neighbors = adata.uns['neighbors']
obsp = adata.obsp
highly_variable = adata.var_names

adata = ad.concat([
    sc.read_h5ad('/lustre/groups/ml01/workspace/monge_velo/data/mouse_gastrulation_atlas/training/validation.h5ad'),
    adata
])
var = adata.var #otherwise not subsetted to hgv genes

scvi.model.SCVI.setup_anndata(adata, batch_key=condition_key)
vae = scvi.model.SCVI(
    adata,
    n_layers=n_layers,
    n_hidden=1024,
    n_latent=50,
    use_layer_norm="both",
    use_batch_norm="none"
)
vae.train(check_val_every_n_epoch=1, max_epochs=500, early_stopping=False, train_size=n_obs/adata.n_obs, validation_size=None, shuffle_set_split=False)
vae.save(adata_path, overwrite=True)

adata = adata[100000:]
adata.var = var
adata.uns['neighbors'] = neighbors
adata.obsp = obsp

adata.write(f'{adata_path}/unintegrated_adata.h5ad')
del adata

#training metrics
pd.DataFrame(
    np.concatenate([vae.history['train_loss_epoch'], vae.history['validation_loss']], axis=1), columns=['train_loss', 'val_loss']
).to_csv(
    f'{metrics_path}/loss.csv'
)

pd.DataFrame(
    np.concatenate([vae.history['elbo_train'], vae.history['elbo_validation']], axis=1), columns=['train_elbo', 'val_elbo']
).to_csv(
    f'{metrics_path}/elbo.csv'
)

pd.DataFrame(
    np.concatenate([vae.history['reconstruction_loss_train'], vae.history['reconstruction_loss_validation']], axis=1), columns=['train_recon_loss', 'val_recon_loss']
).to_csv(
    f'{metrics_path}/reconstr_loss.csv'
)



