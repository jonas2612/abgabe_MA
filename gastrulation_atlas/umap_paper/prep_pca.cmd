#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/umap_paper/bash_messages/outputs_prep
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/umap_paper/bash_messages/errors_prep
#SBATCH -J prep
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=300G # total memory in MB
#SBATCH -t 2-00:00:00 # format dd-hh:mm:ss
#SBATCH --nice=100000  # adjusts scheduling priority
#SBATCH --dependency afterok:14319621


source $HOME/.bashrc

mamba activate subsampling
python /home/icb/jonas.flor/gastrulation_atlas/umap_paper/prep_pca.py

path="$(grep -i 'error|killed' /home/icb/jonas.flor/gastrulation_atlas/umap_paper/bash_messages/errors_prep)"
if [ -z "$path" ]
then
    sbatch /home/icb/jonas.flor/gastrulation_atlas/umap_paper/pca_paper.cmd
    echo "Done!"
else
    echo "Error produced"
fi
