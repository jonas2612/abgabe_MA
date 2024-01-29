#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/outputs_prep_10k_2k_2_128
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/errors_prep_10k_2k_2_128
#SBATCH -J prep_10k_2k_2_128
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=150G
#SBATCH -t 15:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/training/preprocessing.py 10k 2k_genes 2 128 

path="$(grep -iE 'killed' /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/errors_prep_10k_2k_2_128)"
if [ -z "$path" ]
then                    
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_ari_integrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_ari_unintegrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_ASW_integrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_ASW_unintegrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_cLISI_integrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_cLISI_unintegrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_graph_connectivity_integrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_graph_connectivity_unintegrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_hgv_overlap_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_iLISI_integrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_iLISI_unintegrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_iso_labels_integrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_iso_labels_unintegrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_nmi_integrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_nmi_unintegrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_pcr_integrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_pcr_unintegrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_silhouette_batch_integrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_silhouette_batch_unintegrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_silhouette_integrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_silhouette_unintegrated_10k_2k_2_128.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_traject_conservation_10k_2k_2_128.cmd
    echo "Done!"
else
    echo "Error produced"
fi
                        
                        