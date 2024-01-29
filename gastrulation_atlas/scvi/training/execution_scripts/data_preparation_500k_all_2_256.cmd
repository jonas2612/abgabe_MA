#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/outputs_data_prep_500k_all_2_256
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/errors_data_prep_500k_all_2_256
#SBATCH -J data_prep_500k_all_2_256
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=150G
#SBATCH -t 1-00:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/training/data_preparation.py 500k all_genes 2 256 

path="$(grep -iE 'killed' /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/errors_data_prep_500k_all_2_256)"
if [ -z "$path" ]
then
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/preprocessing_500k_all_2_256.cmd
    echo "Done!"
else
    echo "Error produced"
fi
                        
                        