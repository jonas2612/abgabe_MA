#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/data/bash_messages/outputs_atlas_normalization
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/data/bash_messages/errors_atlas_normalization
#SBATCH -J atlas_normalization
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=300G # total memory in MB
#SBATCH -t 2-00:00:00 # format dd-hh:mm:ss
#SBATCH --nice=100000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate atlas_pca
python /home/icb/jonas.flor/gastrulation_atlas/data/atlas_normalization.py

#path="$(grep -i -E 'error|killed' /home/icb/jonas.flor/gastrulation_atlas/data/bash_messages/errors_atlas_normalization)"
#if [ -z "$path" ]
#then
#    sbatch /home/icb/jonas.flor/gastrulation_atlas/data/atlas_pca.cmd
#else
#    echo "Error produced"
#fi
