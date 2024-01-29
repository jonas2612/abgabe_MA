#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/bash_messages/outputs_pca_1M_10k_ex
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/bash_messages/errors_pca_1M_10k_ex
#SBATCH -J pca_1M_10k_ex
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=100G # total memory in MB
#SBATCH -t 04:00:00 # format dd-hh:mm:ss
#SBATCH --nice=10000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/preprocessing.py exvito 1M 10k_genes 2 2048

sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/downstream_analysis/analysis_exvito_10k_integrated.cmd
sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/downstream_analysis/analysis_exvito_10k_integrated_w.cmd
sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/downstream_analysis/analysis_exvito_10k_unintegrated.cmd
sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/downstream_analysis/analysis_exvito_10k_unintegrated_w.cmd
for m in metric_ari_integrated metric_ASW_integrated metric_cLISI_integrated metric_graph_connectivity_integrated metric_hgv_overlap metric_iLISI_integrated metric_iso_labels_integrated metric_nmi_integrated metric_pcr_integrated metric_silhouette_batch_integrated  metric_silhouette_integrated metric_traject_conservation
do
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/scib/${m}_exvito_10k.cmd
done
