#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/subsampling/bash_messages/outputs_subsampling_100k
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/subsampling/bash_messages/errors_subsampling_100k
#SBATCH -J 100k_subsampling
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=300G # total memory in MB
#SBATCH -t 00-18:00:00 # format dd-hh:mm:ss
#SBATCH --nice=100000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate subsampling
python /home/icb/jonas.flor/gastrulation_atlas/scvi/subsampling/subsampling.py 100k

path="$(grep -i 'error|killed' /home/icb/jonas.flor/gastrulation_atlas/scvi/subsampling/bash_messages/errors_subsampling_100k)"
if [ -z "$path" ]
then
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/training_100k_all.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/training_100k_2k.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/training/training_100k_10k.cmd
    echo "Done!"
else
    echo "Error produced"
fi