#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/bash_messages/outputs_in_10k_unintegrated_recon
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/bash_messages/errors_in_10k_unintegrated_recon
#SBATCH -J push_in_10k_unintegrated_recon
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=100G
#SBATCH -t 04:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate moscot_flow
python /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/otfm_push.py invito 10k_genes unintegrated recon unweighted
                    