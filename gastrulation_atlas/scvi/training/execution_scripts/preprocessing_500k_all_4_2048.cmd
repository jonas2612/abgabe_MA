#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/outputs_prep_500k_all_4_2048
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/errors_prep_500k_all_4_2048
#SBATCH -J prep_500k_all_4_2048
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=150G
#SBATCH -t 15:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/training/preprocessing.py 500k all_genes 4 2048 

path="$(grep -iE 'killed' /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/errors_prep_500k_all_4_2048)"
if [ -z "$path" ]
then                    
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_ari_integrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_ari_unintegrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_ASW_integrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_ASW_unintegrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_cLISI_integrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_cLISI_unintegrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_graph_connectivity_integrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_graph_connectivity_unintegrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_hgv_overlap_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_iLISI_integrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_iLISI_unintegrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_iso_labels_integrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_iso_labels_unintegrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_nmi_integrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_nmi_unintegrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_pcr_integrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_pcr_unintegrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_silhouette_batch_integrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_silhouette_batch_unintegrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_silhouette_integrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_silhouette_unintegrated_500k_all_4_2048.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_traject_conservation_500k_all_4_2048.cmd
    echo "Done!"
else
    echo "Error produced"
fi
                        
                        