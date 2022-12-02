#!/bin/bash
cd /HDD/data/andrea/phenotypes/

file1="variants.tsv"
name="variants_"
for namefile in *.both_sexes.tsv;
# to create a file in the proper format for ldsr
do
echo $namefile
VAR3="$name$namefile"
echo $VAR3
paste $file1 $namefile > $VAR3
sleep 1m
wait
done

for namefile in *.varorder.tsv;
# to create a file in the proper format for ldsr
do
echo $namefile
VAR3="$name$namefile"
echo $VAR3
paste $file1 $namefile > $VAR3
sleep 1m
wait
done