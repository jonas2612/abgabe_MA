#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/scvi/subsampling/bash_messages/outputs_subsampling_validation
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/scvi/subsampling/bash_messages/errors_subsampling_validation
#SBATCH -J validation_subsampling
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=300G # total memory in MB
#SBATCH -t 00-03:00:00 # format dd-hh:mm:ss
#SBATCH --nice=100000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate subsampling
python /home/icb/jonas.flor/gastrulation_atlas/scvi/subsampling/subsampling_validation.py

path="$(grep -i -E 'error|killed' /home/icb/jonas.flor/gastrulation_atlas/data/bash_messages/errors_subsampling_validation)"
if [ -z "$path" ]
then
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/subsampling/subsampling_script_10k.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/subsampling/subsampling_script_100k.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/subsampling/subsampling_script_500k.cmd
    sbatch /home/icb/jonas.flor/gastrulation_atlas/scvi/subsampling/subsampling_script_1M.cmd
    echo "Done!"
else
    echo "Error produced"
fi

