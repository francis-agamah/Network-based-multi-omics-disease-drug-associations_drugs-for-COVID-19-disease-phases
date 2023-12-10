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
#python multiXrank_full_drug_KG_only.py
#python multiXrank_full_drug_KG_and_DSOG_mild.py
#python multiXrank_full_drug_KG_and_DSOG_moderate.py
#python multiXrank_full_drug_KG_and_DSOG_severe.py

#KO Analysis
#python multiXrank_full_drug_KG_and_DSOG_mild_KO.py
#python multiXrank_full_drug_KG_and_DSOG_moderate_KO.py
#python multiXrank_full_drug_KG_and_DSOG_severe_KO.py

#validation analysis
#python multiXrank_full_drug_KG_and_DSOG_mild_validation.py
python multiXrank_full_drug_KG_and_DSOG_moderate_validation.py
python multiXrank_full_drug_KG_and_DSOG_severe_validation.py
