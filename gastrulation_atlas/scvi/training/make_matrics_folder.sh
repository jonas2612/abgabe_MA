for o in 10k 100k 500k 1M
do
    for g in 2k_genes 10k_genes all_genes
    do
        for l in 1 2 4
        do
            for h in 128 256 512 1024 2048
            do
                mkdir /home/icb/jonas.flor/gastrulation_atlas/scvi/training/${o}/${g}/${l}/${h}/metrics
            done
        done
    done
done