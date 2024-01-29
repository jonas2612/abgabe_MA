#!/bin/bash

#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/atlas_like_paper/bash_messages/outputs_atlas_neighbors
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/atlas_like_paper/bash_messages/errors_atlas_neighbors
#SBATCH -J atlas_neighbors
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=300G # total memory in MB
#SBATCH -t 3-00:00:00 # format dd-hh:mm:ss
#SBATCH --nice=100000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate atlas_pca
python /home/icb/jonas.flor/gastrulation_atlas/atlas_like_paper/atlas_neighbors.py

path="$(grep -i -E 'error|killed' /home/icb/jonas.flor/gastrulation_atlas/atlas_like_paper/bash_messages/errors_neighbors)"
if [ -z "$path" ]
then
    sbatch /home/icb/jonas.flor/gastrulation_atlas/atlas_like_paper/09_atlas_umap.cmd
else
    echo "Error produced"
fi
