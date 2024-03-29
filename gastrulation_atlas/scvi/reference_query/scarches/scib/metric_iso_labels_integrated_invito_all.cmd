#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/scib/bash_messages/outputs_metr_iso_lab_in_inv_all
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/scib/bash_messages/errors_metr_iso_lab_in_inv_all
#SBATCH -J metr_iso_lab_in_inv_all
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=150G
#SBATCH -t 3-00:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/scib/metric_iso_labels_integrated.py invito all_genes

echo "Done!"
