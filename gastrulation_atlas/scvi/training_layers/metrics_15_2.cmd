#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/bash_messages/outputs_metr_15
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/bash_messages/errors_metr_15
#SBATCH -J metr_15
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=150G # total memory in MB
#SBATCH -t 3-00:00:00 # format dd-hh:mm:ss
#SBATCH --nice=100000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/metrics_2.py 15
echo "Done!"
