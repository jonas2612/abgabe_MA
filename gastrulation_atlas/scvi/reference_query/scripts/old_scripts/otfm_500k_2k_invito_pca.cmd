#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/bash_messages/outputs_otfm_500k_2k_in_pca
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/bash_messages/errors_otfm_500k_2k_in_pca
#SBATCH -J otfm_500k_2k_in_pca
#SBATCH -p gpu_p
#SBATCH --qos=gpu_normal
#SBATCH --gres=gpu:1
#SBATCH --mem=100G # total memory in MB
#SBATCH --exclude supergpu[02-03,05-09]
#SBATCH -t 08:00:00 # format dd-hh:mm:ss
#SBATCH --nice=10000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate moscot_flow
python /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/otfm.py invito 500k 2k_genes pca