#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/outputs_metr_iso_lab_in_10k_10k_2_1024
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/errors_metr_iso_lab_in_10k_10k_2_1024
#SBATCH -J metr_iso_lab_in_10k_10k_2_1024
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=150G
#SBATCH -t 3-00:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/training/metric_iso_labels_integrated.py 10k 10k_genes 2 1024 

echo "Done!"
                        