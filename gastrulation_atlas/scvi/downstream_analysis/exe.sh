for d in gastrulation invito exvito
do
    for g in 10k all
    do
        for i in integrated unintegrated
        do
            sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/downstream_analysis/analysis_${d}_${g}_${i}.cmd
            sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/downstream_analysis/analysis_${d}_${g}_${i}_w.cmd
        done
    done
done