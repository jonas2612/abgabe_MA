#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/outputs_tr_10k_10k_2_2048
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/errors_tr_10k_10k_2_2048
#SBATCH -J tr_10k_10k_2_2048
#SBATCH -p gpu_p
#SBATCH --qos=gpu_normal
#SBATCH --gres=gpu:1
#SBATCH --mem=150G
#SBATCH --exclude supergpu[02-03,05-09]
#SBATCH -t 2-00:00:00
#SBATCH --nice=100000


source $HOME/.bashrc

mamba activate scvi
python /home/icb/jonas.flor/gastrulation_atlas/scvi/training/training.py 10k 10k_genes 2 2048 0.001

path="$(grep -iE 'killed' /home/icb/jonas.flor/gastrulation_atlas/scvi/training/bash_messages/errors_tr_10k_10k_2_2048)"
if [ -z "$path" ]
then
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/execution_scripts/data_preparation_10k_10k_2_2048.cmd
    echo "Done!"
else
    echo "Error produced"
fi
                        
                        