#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/bash_messages/outputs_tr_05
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/bash_messages/errors_tr_05
#SBATCH -J tr_05
#SBATCH -p gpu_p
#SBATCH --qos=gpu_normal
#SBATCH --gres=gpu:1
#SBATCH --mem=150G # total memory in MB
#SBATCH -t 1-06:00:00 # format dd-hh:mm:ss
#SBATCH --nice=100000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/training.py 5

path="$(grep -i 'error' /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/bash_messages/errors_tr_05)"
if [ -z "$path" ]
then
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/data_preparation_05.cmd
    echo "Done!"
else
    echo "Error produced"
fi
