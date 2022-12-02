#! /bin/bash

# move to ldsc directory
cd /SSD/scratch/andrea/ldsc

source activate ldsc

##### munge data
# brain
# QSM_Left_Caudate
# ./munge_sumstats.py \
# --sumstats /HDD/data/andrea/QSM_T2/QSM_Left_Caudate.txt \
# --a1 a2 \
# --a2 a1 \
# --out qsm_l_caud \
# --chunksize 500000 \
# --merge-alleles /HDD/data/andrea/w_hm3.snplist


# phenotype
# diastolic blood pressure, 4079_irnt
./munge_sumstats.py \
--sumstats /HDD/data/andrea/phenotypes/variants_4079_irnt.gwas.imputed_v3.both_sexes.tsv \
--a1 alt \
--a2 ref \
--out 4079 \
--chunksize 500000 \
--merge-alleles /HDD/data/andrea/w_hm3.snplist


#### LD Score Regression
# ./ldsc.py \
# --rg qsm_l_caud.sumstats.gz,4079.sumstats.gz \
# --ref-ld-chr /HDD/data/andrea/eur_w_ld_chr/ \
# --w-ld-chr /HDD/data/andrea/eur_w_ld_chr/ \
# --out qsm_l_caud-4079