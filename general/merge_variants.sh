#!/bin/bash
cd /HDD/data/andrea/phenotypes/

## TODO: check if sleep is actually necessary

file1="variants.tsv"
name="variants_"
for namefile in *.both_sexes.tsv; do # to create a file in the proper format for ldsr
    echo $namefile
    VAR3="$name$namefile"
    echo $VAR3
    paste $file1 $namefile >$VAR3
    sleep 1m
    wait
done

for namefile in *.varorder.tsv; do # to create a file in the proper format for ldsr
    echo $namefile
    VAR3="$name$namefile"
    echo $VAR3
    paste $file1 $namefile >$VAR3
    sleep 1m
    wait
done
