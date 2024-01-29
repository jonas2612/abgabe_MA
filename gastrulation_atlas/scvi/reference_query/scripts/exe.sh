for d in exvito invito gast
do
    for g in 10k all
    do
        sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/spaces_seperation_1M_${g}_${d}.cmd
    done
done