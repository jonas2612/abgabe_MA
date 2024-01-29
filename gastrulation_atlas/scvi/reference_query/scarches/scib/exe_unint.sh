for m in metric_ari_unintegrated metric_ASW_unintegrated metric_cLISI_unintegrated metric_graph_connectivity_unintegrated metric_iLISI_unintegrated metric_iso_labels_unintegrated metric_nmi_unintegrated metric_pcr_unintegrated metric_silhouette_batch_unintegrated metric_silhouette_unintegrated
do
    for d in exvito invito gastrulation
    do
        sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scarches/scib/${m}_${d}_10k.cmd
    done
done