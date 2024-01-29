#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/bash_messages/outputs_pca_1M_10k_ex
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/bash_messages/errors_pca_1M_10k_ex
#SBATCH -J pca_1M_10k_ex
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=100G # total memory in MB
#SBATCH -t 04:00:00 # format dd-hh:mm:ss
#SBATCH --nice=10000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/pca_space.py exvito 1M 10k_genes

path="$(grep -i 'error' /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/bash_messages/errors_pca_1M_10k_ex)"
if [ -z "$path" ]
then
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/otfm_1M_10k_exvito_pca.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/otfm_1M_10k_exvito_vae.cmd
else
    echo "Error produced"
fi