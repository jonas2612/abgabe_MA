#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/outputs_metr_sil_bat_un_100k_10k_1_2048
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/errors_metr_sil_bat_un_100k_10k_1_2048
#SBATCH -J metr_sil_bat_un_100k_10k_1_2048
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=150G
#SBATCH -t 1-12:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/training/metric_silhouette_batch_unintegrated.py 100k 10k_genes 1 2048 

echo "Done!"
                        