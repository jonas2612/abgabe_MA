#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/bash_messages/outputs_spaces_10k_all_in
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/bash_messages/errors_spaces_10k_all_in
#SBATCH -J spaces_10k_all_in
#SBATCH -p gpu_p
#SBATCH --qos=gpu_normal
#SBATCH --gres=gpu:1
#SBATCH --mem=150G # total memory in MB
#SBATCH --exclude supergpu[02-03,05-09]
#SBATCH -t 04:00:00 # format dd-hh:mm:ss
#SBATCH --nice=10000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/spaces_seperation.py invito 10k all_genes

path="$(grep -i 'error' /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/bash_messages/errors_spaces_10k_all_in)"
if [ -z "$path" ]
then
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/pca_10k_all_invito.cmd
else
    echo "Error produced"
fi
 