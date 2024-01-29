#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/pca/bash_messages/outputs_pca
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/pca/bash_messages/errors_pca
#SBATCH -J pca_comp
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=300G # total memory in GB
#SBATCH --cpus-per-task=30
#SBATCH -t 03-00:00:00 # format dd-hh:mm:ss
#SBATCH --nice=1000000  # adjusts scheduling priority

source $HOME/.bashrc

mamba activate atlas_pca
python /home/icb/jonas.flor/gastrulation_atlas/pca/pca.py
