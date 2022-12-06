import os
import pandas as pd
from PascalX import xscorer

DIR_PHEN = "/HDD/data/andrea/phenotypes/"
DIR_QSM = "/HDD/data/andrea/QSM_T2/"
DIR_WMH = "/HDD/data/andrea/WMH/"
DIR_WMH40 = "/HDD/data/andrea/WMH_BIG40/"



X = xscorer.zsum(leftTail=True, gpu=True)


X.load_refpanel("/SSD/home/hermione/reference_data/EUR.1KG.GRCh38", parallel=22, keepfile="/HDD/data/andrea/ref_panel/EUR_1KG_phase3_samples.tsv")

X.load_genome("/HDD/data/andrea/GRCh38_protein_coding.tsv")

## Loading GWAs

# I used:
# head -n 1 polished_2443.tsv | tr "\t" "\n" | awk '{print $0, "\t", NR-1}'
# to get a nicer formatting in order to find the corresponding column numbers
X.load_GWAS(f'{DIR_PHEN}polished_2443.tsv', name="Diabetes",
            rscol=5, pcol=35, bcol=32, a1col=4, a2col=3, header=True)

X.load_GWAS(f'{DIR_PHEN}polished_21001_irnt.tsv', name="BMI",
            rscol=5, pcol=35, bcol=32, a1col=4, a2col=3, header=True)

X.load_GWAS(f'{DIR_PHEN}polished_4079_irnt.tsv', name="Diastolic BP",
            rscol=5, pcol=35, bcol=32, a1col=4, a2col=3, header=True)

X.load_GWAS(f'{DIR_PHEN}polished_30740_irnt.tsv', name="Glc",
            rscol=5, pcol=35, bcol=32, a1col=4, a2col=3, header=True)

X.load_GWAS(f'{DIR_PHEN}polished_30760_irnt.tsv', name="HDL",
            rscol=5, pcol=35, bcol=32, a1col=4, a2col=3, header=True)

X.load_GWAS(f'{DIR_PHEN}polished_6150_4.tsv', name="Hypertension",
            rscol=5, pcol=35, bcol=32, a1col=4, a2col=3, header=True)

X.load_GWAS(f'{DIR_PHEN}polished_104910.tsv', name="Moderate physical activity",
            rscol=5, pcol=35, bcol=32, a1col=4, a2col=3, header=True)

######

X.load_GWAS(f'{DIR_QSM}QSM_Left_caudate.txt', name="QSM_Left_caudate", rscol=0, pcol=7, bcol=5, a1col=4, a2col=3, header=True)

# TODO: add missing GWASs

# to correct for sample overlapping
# let's get gcov_int from summary.txt
df = pd.read_csv("/HDD/data/andrea/ld_score_regression/summary.txt", sep="\t")

def get_stats(idp):
    return df.loc[df["p1"]==idp]


gcov_ints = {}

def get_gcov_int(idp, phen):
    return get_stats(idp).loc[get_stats(idp)["p2"]==phen]["gcov_int"].values[0]

phen_names = {"100270": "Coffee intake",
         "104910": "Moderate physical activity",
         "1160": "Sleep duration",
         "1239": "Smoking",
         "1558": "Alcohol intake",
         "21001_irnt": "BMI",
         "2443": "Diabetes",
         "30740_irnt": "Glc",
         "30760_irnt": "HDL",
         "30780_irnt": "LDL",
         "30870_irnt": "Triglycerides",
         "4079_irnt": "Diastolic BP",
             "4080_irnt": "Systolic BP",
             "6150_3": "Stroke",
             "6150_4": "Hypertension"}

def gcov_ints_update(idp, phen):
    gcov_ints.update({f"{idp}-{phen_names[phen]}": get_gcov_int(idp, phen)})





R = X.score_all(E_A='Diabetes',E_B='QSM_Left_caudate', parallel=8, pcorr=gcov_ints["leftcaudate_diabetes"])



# Create a dictionary of the GWAS phenotypes and IDPs to combine with each
phenotypes = {
    "QSM_Left_caudate": ["Diabetes", ...],
    ...
}

# TODO: complete dictionary

# Loop through all GWAS
for E_A, E_B_list in phenotypes.items():
    # Loop through the other phenotypes to combine with the current IDP
    for E_B in E_B_list:

        X.matchAlleles(E_A, E_B)
        X.jointlyRank(E_A, E_B)

        # Score
        R = X.score_all(E_A=E_A, E_B=E_B, parallel=8, pcorr=gcov_ints[f"{E_A}-{E_B}"])

        # Save results
        # TODO: Save results