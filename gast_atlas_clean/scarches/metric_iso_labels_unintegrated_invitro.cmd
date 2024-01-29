#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gast_atlas_clean/scarches/bash_messages/outputs_metr_iso_lab_un_inv
#SBATCH -e /home/icb/jonas.flor/gast_atlas_clean/scarches/bash_messages/errors_metr_iso_lab_un_inv
#SBATCH -J metr_iso_lab_un_inv
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=150G
#SBATCH -t 3-00:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gast_atlas_clean/scarches/metric_iso_labels_unintegrated.py invitro

echo "Done!"
