#!/bin/bash

cd /HDD/data/andrea/WMH/

#i'm assuming each row is a SNP here...
file1="stats.txt"

#one row per SNP, one column per IDP, no header
for file in b.txt p.txt;

do

paste -c