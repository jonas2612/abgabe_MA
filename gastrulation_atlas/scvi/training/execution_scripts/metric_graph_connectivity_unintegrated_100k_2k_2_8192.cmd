#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/outputs_metr_gr_con_un_100k_2k_2_8192
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/errors_metr_gr_con_un_100k_2k_2_8192
#SBATCH -J metr_gr_con_un_100k_2k_2_8192
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=150G
#SBATCH -t 1-12:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/training/metric_graph_connectivity_unintegrated.py 100k 2k_genes 2 8192 

echo "Done!"
                        