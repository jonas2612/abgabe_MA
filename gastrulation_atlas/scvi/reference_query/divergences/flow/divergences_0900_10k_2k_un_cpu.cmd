#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergences/flow/bash_messages/outputs_cpu_test
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergences/flow/bash_messages/errors_cpu_test
#SBATCH -J cpu_test
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=60G # total memory in MB
#SBATCH --exclude supergpu[02-03,05-09]
#SBATCH -t 2-00:00:00 # format dd-hh:mm:ss
#SBATCH --nice=1000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate moscot_flow_3
python /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/divergences/flow/divergence_0900_5k.py 10k 2k_genes unintegrated

