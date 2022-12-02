#!/bin/bash

# move to ldsc directory
cd /SSD/scratch/andrea/ldsc || exit #in case of error :-p

#preparing the environment (only at very beginning)
source activate ldsc

##### BRAIN #####################################

echo "Munging brain QSM_T2 IDPs"

mkdir -p /HDD/data/andrea/munged/brain

for file in /HDD/data/andrea/QSM_T2/*.txt; do
    #the following 2 lines are necessary to extract the *name*
    #and not the full path of the file
    #(for "out" parameter)
    #i.e. $file is /HDD/data/andrea/QSM_T2/QSM_Left_caudate.txt
    #while $name is just QSM_Left_caudate

    #removes path (but not extension, just yet...)
    nopath=${file##*/}
    #removes extension (i.e. ".txt")
    name=${nopath%.*}

    ./munge_sumstats.py \
        --sumstats "$file" \
        --a1 a2 \
        --a2 a1 \
        --out /HDD/data/andrea/munged/brain/"$name" \
        --chunksize 500000 \
        --merge-alleles /HDD/data/andrea/w_hm3.snplist

done

echo "Munging brain WMH IDPs"

mkdir -p /HDD/data/andrea/munged/brain

for file in /HDD/data/andrea/WMH/{volume,lesion}.txt; do

    nopath=${file##*/}
    name=${nopath%.*}

    ./munge_sumstats.py \
        --sumstats "$file" \
        --a1 a2 \
        --a2 a1 \
        --out /HDD/data/andrea/munged/brain/"$name" \
        --chunksize 500000 \
        --merge-alleles /HDD/data/andrea/w_hm3.snplist

done

echo "Munging WMH BIG40 total volume IDP"

./munge_sumstats.py \
	--sumstats /HDD/data/andrea/WMH_BIG40/volume_big40.txt \
	--a1 a2 \
	--a2 a1 \
	--out /HDD/data/andrea/munged/brain/volume_big40 \
	--chunksize 500000 \
	--merge-alleles /HDD/data/andrea/w_hm3.snplist

#### PHENOTYPES #################################

echo "Munging phenotypes"

mkdir -p /HDD/data/andrea/munged/phenotypes

for file in /HDD/data/andrea/phenotypes/polished_*.tsv; do
    nopath=${file##*/}
    name=${nopath%.*}
    ./munge_sumstats.py \
        --sumstats "$file" \
        --a1 alt \
        --a2 ref \
        --out /HDD/data/andrea/munged/phenotypes/"$name" \
        --chunksize 500000 \
        --merge-alleles /HDD/data/andrea/w_hm3.snplist
done
