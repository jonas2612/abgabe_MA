#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/downstream_analysis/bash_messages/outputs_analysis_in_all_integrated_w
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/downstream_analysis/bash_messages/errors_analysis_in_all_integrated_w
#SBATCH -J analysis_in_all_integrated_w
#SBATCH -p gpu_p
#SBATCH --qos=gpu_normal
#SBATCH --gres=gpu:1
#SBATCH --mem=100G
#SBATCH -t 1-00:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate cellrank_new
python /home/icb/jonas.flor/gastrulation_atlas/scvi/downstream_analysis/script.py invito all_genes integrated weighted
                