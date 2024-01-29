#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/outputs_prep_1M_2k_4_4096
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/errors_prep_1M_2k_4_4096
#SBATCH -J prep_1M_2k_4_4096
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=150G
#SBATCH -t 15:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/training/preprocessing.py 1M 2k_genes 4 4096 

path="$(grep -iE 'killed' /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/errors_prep_1M_2k_4_4096)"
if [ -z "$path" ]
then                    
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_ari_integrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_ari_unintegrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_ASW_integrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_ASW_unintegrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_cLISI_integrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_cLISI_unintegrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_graph_connectivity_integrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_graph_connectivity_unintegrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_hgv_overlap_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_iLISI_integrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_iLISI_unintegrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_iso_labels_integrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_iso_labels_unintegrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_nmi_integrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_nmi_unintegrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_pcr_integrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_pcr_unintegrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_silhouette_batch_integrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_silhouette_batch_unintegrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_silhouette_integrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_silhouette_unintegrated_1M_2k_4_4096.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/metric_traject_conservation_1M_2k_4_4096.cmd
    echo "Done!"
else
    echo "Error produced"
fi
                        
                        