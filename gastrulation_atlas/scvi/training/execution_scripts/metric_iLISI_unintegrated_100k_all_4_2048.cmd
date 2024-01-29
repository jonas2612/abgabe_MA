#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/outputs_metr_iLISI_un_100k_all_4_2048
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/errors_metr_iLISI_un_100k_all_4_2048
#SBATCH -J metr_iLISI_un_100k_all_4_2048
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=150G
#SBATCH -t 1-12:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/training/metric_iLISI_unintegrated.py 100k all_genes 4 2048 

echo "Done!"
                        