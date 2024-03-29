#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergences/flow/bash_messages/outputs_div_09_100k_all_in
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergences/flow/bash_messages/errors_div_09_100k_all_in
#SBATCH -J div_09_100k_all_in
#SBATCH -p gpu_p
#SBATCH --qos=gpu_normal
#SBATCH --gres=gpu:1
#SBATCH --mem=60G # total memory in MB
#SBATCH --exclude supergpu[02-03,05-09]
#SBATCH -t 2-00:00:00 # format dd-hh:mm:ss
#SBATCH --nice=100000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate moscot_flow
python /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergences/flow/divergence_0900.py 100k all_genes integrated

