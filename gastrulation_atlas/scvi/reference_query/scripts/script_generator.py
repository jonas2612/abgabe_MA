dict_ds = {'gastrulation': 'gast', 'invito': 'in', 'exvito': 'ex'}
dict_weight = {'weighted': '_w', 'unweighted':''}
for d in ['gastrulation', 'invito', 'exvito']:
    for g in ['10k', 'all']:
        for i in ['integrated', 'unintegrated']:
            for l in ['recon', 'elbo']:
                for w in ['weighted', 'unweighted']:
                    f=open(f'otfm_push_{d}_{g}_{i}_{l}{dict_weight[w]}.cmd', 'w+')
                    f.write(f'''#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/bash_messages/outputs_{dict_ds[d]}_{g}_{i}_{l}{dict_weight[w]}
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/bash_messages/errors_{dict_ds[d]}_{g}_{i}_{l}{dict_weight[w]}
#SBATCH -J push_{dict_ds[d]}_{g}_{i}_{l}{dict_weight[w]}
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=100G
#SBATCH -t 04:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate moscot_flow
python /home/icb/jonas.flor/gastrulation_atlas/scvi/reference_query/scripts/otfm_push.py {d} {g}_genes {i} {l} {w}
                    ''')
                    f.close()