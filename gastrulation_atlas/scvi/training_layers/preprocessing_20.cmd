#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/bash_messages/outputs_prep_20
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/bash_messages/errors_prep_20
#SBATCH -J prep_20
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=100G # total memory in MB
#SBATCH -t 0-04:00:00 # format dd-hh:mm:ss
#SBATCH --nice=100000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate rapids_singlecell
python /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/preprocessing.py 20

path="$(grep -i 'error' /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/bash_messages/errors_prep_20)"
if [ -z "$path" ]
then
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/metrics_20_1.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/metrics_20_2.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training_layers/metrics_20_3.cmd
    echo "Done!"
else
    echo "Error produced"
fi
