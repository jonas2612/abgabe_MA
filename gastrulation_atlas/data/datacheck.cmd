#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/data/bash_messages/outputs_datacheck
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/data/bash_messages/errors_datacheck
#SBATCH -J datacheck
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=250G # total memory in MB
#SBATCH -t 0-01:30:00 # format dd-hh:mm:ss
#SBATCH --nice=100000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate atlas_pca
python /home/icb/jonas.flor/gastrulation_atlas/data/datacheck.py > datacheck.out
