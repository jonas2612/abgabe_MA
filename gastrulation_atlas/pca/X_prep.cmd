#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/pca/bash_messages/outputs_X_prep
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/pca/bash_messages/errors_X_prep
#SBATCH -J X_prep
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=300G # total memory in MB
#SBATCH -t 01-00:00:00 # format dd-hh:mm:ss
#SBATCH --nice=100000  # adjusts scheduling priority

source $HOME/.bashrc

mamba activate atlas_moscot
python /home/icb/jonas.flor/gastrulation_atlas/pca/X_prep.py