#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/outputs_metr_ari_in_100k_10k_1_512
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/errors_metr_ari_in_100k_10k_1_512
#SBATCH -J metr_ari_in_100k_10k_1_512
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=150G
#SBATCH -t 3-00:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/training/metric_ari_integrated.py 100k 10k_genes 1 512 

echo "Done!"
                        