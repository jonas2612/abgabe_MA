#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/scib/bash_messages/outputs_metr_nmi_in_exv_10k
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/scib/bash_messages/errors_metr_nmi_in_exv_10k
#SBATCH -J metr_nmi_in_exv_10k
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=150G
#SBATCH -t 3-00:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/scib/metric_nmi_integrated.py exvito 10k_genes

echo "Done!"
