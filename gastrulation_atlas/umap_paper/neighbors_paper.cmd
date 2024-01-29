#!/bin/bash


#SBATCH -o /home/icb/jonas.flor/gastrulation_atlas/umap_paper/bash_messages/outputs_neighbors
#SBATCH -e /home/icb/jonas.flor/gastrulation_atlas/umap_paper/bash_messages/errors_neighbors
#SBATCH -J neighbors
#SBATCH -p cpu_p
#SBATCH --qos=cpu_normal
#SBATCH --mem=300G # total memory in MB
#SBATCH -t 2-00:00:00 # format dd-hh:mm:ss
#SBATCH --nice=100000  # adjusts scheduling priority


source $HOME/.bashrc

mamba activate subsampling
python /home/icb/jonas.flor/gastrulation_atlas/umap_paper/neighbors_paper.py

path="$(grep -i 'error|killed' /home/icb/jonas.flor/gastrulation_atlas/umap_paper/bash_messages/errors_neighbors)"
if [ -z "$path" ]
then
    sbatch /home/icb/jonas.flor/gastrulation_atlas/umap_paper/leiden_paper.cmd
    echo "Done!"
else
    echo "Error produced"
fi