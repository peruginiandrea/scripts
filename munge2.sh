#!/bin/bash

# move to ldsc directory
cd /SSD/scratch/andrea/ldsc || exit #in case of error :-p

#preparing the environment (only at very beginning)
source activate ldsc

##### BRAIN #####################################

echo "Munging WMH BIG40 total volume IDP"

mkdir -p /HDD/data/andrea/munged/brain
./munge_sumstats.py \
	--sumstats /HDD/data/andrea/WMH_BIG40/volume_big40.txt \
	--a1 a2 \
	--a2 a1 \
	--out /HDD/data/andrea/munged/brain/volume_big40 \
	--chunksize 500000 \
	--merge-alleles /HDD/data/andrea/w_hm3.snplist


