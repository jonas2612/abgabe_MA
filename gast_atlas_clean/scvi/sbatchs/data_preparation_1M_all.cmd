#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gast_atlas_clean/scvi/bash_messages/outputs_data_prep_1M_all
#SBATCH -e /home/icb/jonas.flor/gast_atlas_clean/scvi/bash_messages/errors_data_prep_1M_all
#SBATCH -J data_prep_1M_all
#SBATCH -p cpu_p
#SBATCH --qos=cpu_long
#SBATCH --mem=150G
#SBATCH -t 1-00:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gast_atlas_clean/scvi/preparation.py 1M all_genes

path="$(grep -iE 'killed' /home/icb/jonas.flor/gast_atlas_clean/scvi/bash_messages/errors_data_prep_1M_all)"
if [ -z "$path" ]
then
    sbatch /home/icb/jonas.flor/gast_atlas_clean/scvi/sbatchs/preprocessing_1M_all.cmd
    echo "Done!"
else
    echo "Error produced"
fi
                        
                        