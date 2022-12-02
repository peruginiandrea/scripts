#!/bin/bash

# move to ldsc directory
cd /SSD/scratch/andrea/ldsc || exit #in case of error :-p

#preparing the environment (only at very beginning)
source activate ldsc

output="/HDD/data/andrea/ld_score_regression/"
mkdir -p $output

for brain_file in /HDD/data/andrea/munged/brain/*.sumstats.gz; do
    for phenotype_file in /HDD/data/andrea/munged/phenotypes/*.sumstats.gz; do

        nopath_brain=${brain_file##*/}
        nopath_phen=${phenotype_file##*/}
        name_brain=${nopath_brain%.*.*}
        name_phen=${nopath_phen%.*.*}
        ### LD Score Regression
        ./ldsc.py \
            --rg ${brain_file},${phenotype_file} \
            --ref-ld-chr /HDD/data/andrea/eur_w_ld_chr/ \
            --w-ld-chr /HDD/data/andrea/eur_w_ld_chr/ \
            --out "${output}${name_brain}---${name_phen}"
    done
done