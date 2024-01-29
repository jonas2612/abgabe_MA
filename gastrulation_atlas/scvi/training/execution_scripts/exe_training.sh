for o in 10k 500k
do
    for g in 2k 10k all
    do
        for l in 1 2 4
        do
            for h in 128 256 512 1024 2048
            do
                sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/training_${o}_${g}_${l}_${h}.cmd
            done
        done
    done
done
