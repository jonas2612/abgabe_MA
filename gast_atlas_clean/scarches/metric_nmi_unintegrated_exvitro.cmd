#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gast_atlas_clean/scarches/bash_messages/outputs_metr_nmi_un_exv
#SBATCH -e /home/icb/jonas.flor/gast_atlas_clean/scarches/bash_messages/errors_metr_nmi_un_exv
#SBATCH -J metr_nmi_un_exv
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=150G
#SBATCH -t 3-00:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gast_atlas_clean/scarches/metric_nmi_unintegrated.py exvitro

echo "Done!"