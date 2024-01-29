#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/bash_messages/outputs_top_merge
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/bash_messages/errors_top_merge
#SBATCH -J top_merge
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=300G # total memory in MB
#SBATCH -t 12:00:00 # format dd-hh:mm:ss
#SBATCH --nice=100000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate scvi_pipeline
python /home/icb/jonas.flor/gastrulation_atlas/data_merge/top_merge.py