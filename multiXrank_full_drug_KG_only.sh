#!/bin/bash

#SBATCH --job-name='multiXrank_val'
#SBATCH --cpus-per-task=8
#SBATCH --mem=32GB
#SBATCH --output=multiXrank_full-%j-stdout.log
#SBATCH --error=multiXrank_full-%j-stderr.log
#SBATCH --time=96:00:00

echo "Submitting Slurm job"
wk=/cbio/users/francis_agamah/SOFT/multiXrank/
cd ${wk}

#module add R/4.2.0
#echo "module R/4.2.0 added"


module add python/3.9.0
echo "python module added"
python multiXrank_full_drug_KG_only.py
