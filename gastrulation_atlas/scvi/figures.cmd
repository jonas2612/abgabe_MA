#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/bash_messages/outputs_figs
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/bash_messages/errors_figs
#SBATCH -J figs
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=50G # total memory in MB
#SBATCH -t 0-12:00:00 # format dd-hh:mm:ss
#SBATCH --nice=100000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate subsampling
python /home/icb/jonas.flor/gastrulation_atlas/scvi/figures.py
echo "Done!"
