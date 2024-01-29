#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/outputs_metr_sil_bat_in_500k_2k_1_128
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/errors_metr_sil_bat_in_500k_2k_1_128
#SBATCH -J metr_sil_bat_in_500k_2k_1_128
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=150G
#SBATCH -t 1-12:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/training/metric_silhouette_batch_integrated.py 500k 2k_genes 1 128 

echo "Done!"
                        