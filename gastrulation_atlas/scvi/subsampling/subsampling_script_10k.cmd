#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/subsampling/bash_messages/outputs_subsampling_10k
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/subsampling/bash_messages/errors_subsampling_10k
#SBATCH -J 10k_subsampling
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=300G # total memory in MB
#SBATCH -t 0-01:00:00 # format dd-hh:mm:ss
#SBATCH --nice=100000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate subsampling
python /home/icb/jonas.flor/gastrulation_atlas/scvi/subsampling/subsampling.py 10k

path="$(grep -i 'error|killed' /home/icb/jonas.flor/gastrulation_atlas/scvi/subsampling/bash_messages/errors_subsampling_10k)"
if [ -z "$path" ]
then
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/training_10k_all.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/training_10k_2k.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/training_10k_10k.cmd
    echo "Done!"
else
    echo "Error produced"
fi