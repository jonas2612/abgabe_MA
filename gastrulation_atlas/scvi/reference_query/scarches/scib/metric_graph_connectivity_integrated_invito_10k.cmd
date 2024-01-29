#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/scib/bash_messages/outputs_metr_gr_con_in_inv_10k
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/scib/bash_messages/errors_metr_gr_con_in_inv_10k
#SBATCH -J metr_gr_con_in_inv_10k
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=150G
#SBATCH -t 1-12:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/scib/metric_graph_connectivity_integrated.py invito 10k_genes

echo "Done!"
