#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergences/moscot_not/bash_messages/outputs_div_12_1M_2k_un
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergences/moscot_not/bash_messages/errors_div_12_1M_2k_un
#SBATCH -J div_12_1M_2k_un
#SBATCH -p gpu_p
#SBATCH --qos=gpu_normal
#SBATCH --gres=gpu:1
#SBATCH --mem=100G # total memory in MB
#SBATCH --exclude supergpu[02-03,05-09]
#SBATCH -t 1-00:00:00 # format dd-hh:mm:ss
#SBATCH --nice=100000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate moscot_divergence
python /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergences/moscot_not/divergence_12.py 1M 2k_genes unintegrated

