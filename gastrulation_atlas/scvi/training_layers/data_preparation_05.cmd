#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/bash_messages/outputs_data_prep_05
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/bash_messages/errors_data_prep_05
#SBATCH -J data_prep_05
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=100G # total memory in MB
#SBATCH -t 0-06:00:00 # format dd-hh:mm:ss
#SBATCH --nice=100000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/data_preparation.py 5 50000

path="$(grep -i 'error' /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/bash_messages/errors_data_prep_05)"
if [ -z "$path" ]
then
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/preprocessing_05.cmd
    echo "Done!"
else
    echo "Error produced"
fi
