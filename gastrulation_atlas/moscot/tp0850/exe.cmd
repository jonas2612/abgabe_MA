#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/moscot/bash_messages/outputs_0850
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/moscot/bash_messages/errors_0850
#SBATCH -J 8.5
#SBATCH -p gpu_p
#SBATCH --qos=gpu_normal
#SBATCH --gres=gpu:1
#SBATCH --mem=100G # total memory in MB
#SBATCH -t 03:00:00 # format dd-hh:mm:ss
#SBATCH --nice=10000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate atlas_moscot
python /home/icb/jonas.flor/gastrulation_atlas/moscot/tp0850/balanced.py