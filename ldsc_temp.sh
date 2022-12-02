#!/bin/bash

# move to ldsc directory
cd /SSD/scratch/andrea/ldsc

source activate ldsc

##### munge data



# phenotype
# diastolic blood pressure, 4079_irnt
./munge_sumstats.py \
--sumstats /HDD/data/andrea/phenotypes/variants_4079_irnt.gwas.imputed_v3.both_sexes.tsv \
--a1 alt \
--a2 ref \
--N n_complete_samples \
--out 4079 \
--chunksize 5000000 \
--merge-alleles /HDD/data/andrea/w_hm3.snplist


