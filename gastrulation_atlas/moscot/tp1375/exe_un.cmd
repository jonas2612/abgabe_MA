#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/moscot/bash_messages/outputs_1375un
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/moscot/bash_messages/errors_1375un
#SBATCH -J 13.75
#SBATCH -p gpu_p
#SBATCH --qos=gpu_normal
#SBATCH --gres=gpu:1
#SBATCH --mem=150G # total memory in MB
#SBATCH -t 03:00:00 # format dd-hh:mm:ss
#SBATCH --nice=10000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate atlas_moscot
python /home/icb/jonas.flor/gastrulation_atlas/moscot/tp1375/unbalanced.py