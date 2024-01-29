for d in gastrulation invito exvito
do
    for g in 10k all
    do
        for i in integrated unintegrated
        do
            sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/otfm_push_${d}_${g}_${i}_elbo_w.cmd
            sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/otfm_push_${d}_${g}_${i}_elbo.cmd
        done
    done
done