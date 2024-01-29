#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/outputs_data_prep_1M_2k_4_4096
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/errors_data_prep_1M_2k_4_4096
#SBATCH -J data_prep_1M_2k_4_4096
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=150G
#SBATCH -t 1-00:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/training/data_preparation.py 1M 2k_genes 4 4096 

path="$(grep -iE 'killed' /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/errors_data_prep_1M_2k_4_4096)"
if [ -z "$path" ]
then
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/preprocessing_1M_2k_4_4096.cmd
    echo "Done!"
else
    echo "Error produced"
fi
                        
                        