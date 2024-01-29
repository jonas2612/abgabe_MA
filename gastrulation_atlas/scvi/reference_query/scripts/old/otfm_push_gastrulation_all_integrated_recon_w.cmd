#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/bash_messages/outputs_gast_all_integrated_recon_w
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/bash_messages/errors_gast_all_integrated_recon_w
#SBATCH -J push_gast_all_integrated_recon_w
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=100G
#SBATCH -t 04:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate moscot_flow
python /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/otfm_push.py gastrulation all_genes integrated recon weighted
                    