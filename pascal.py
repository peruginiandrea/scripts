import os
import pandas as pd
from PascalX import xscorer

DIR_PHEN = "/HDD/data/andrea/phenotypes/"
DIR_QSM = "/HDD/data/andrea/QSM_T2/"
DIR_WMH = "/HDD/data/andrea/WMH/"
DIR_WMH40 = "/HDD/data/andrea/WMH_BIG40/"



X = xscorer.zsum(leftTail=True, gpu=True)

## TODO: figure out why this doesn't work (and check the files)
## ! NOTE: I'm not sure if these are the correct files

X.load_refpanel("/SSD/scratch/hermione/ref_data/EUR.1KG.GRCh38", parallel=22)

X.load_genome("/SSD/scratch/hermione/ref_data/GRCh38_annotation.tsv")

os.chdir(DIR_PHEN)

list_dir = os.listdir(DIR_PHEN)

# for file in list_dir:
#     if os.path.isfile(file) and file.endswith(".tsv") and file.startswith("polished_"):

        # head -n 1 polished_104910.tsv | tr "\t" "\n" | awk '{print $0, "\t", NR-1}'
        # to get a nicer formatting in order to find the corresponding column numbers
        # X.load_genome(file, ccol=1, cid=5, )

# head -n 1 polished_2443.tsv | tr "\t" "\n" | awk '{print $0, "\t", NR-1}'
# to get a nicer formatting in order to find the corresponding column numbers
X.load_GWAS(f'{DIR_PHEN}polished_2443.tsv', name="Diabetes", rscol=5, pcol=35, bcol=32, a1col=4, a2col=3, header=True)


# i don't know why these files have an index column
# DONE remove index column
# TODO: verify that values obtained from ldsc are still correct!!



X.load_GWAS(f'{DIR_QSM}QSM_Left_caudate.txt', name="QSM_Left_caudate", rscol=0, pcol=7, bcol=5, a1col=4, a2col=3, header=True)


# to correct for sample overlapping
# let's get gcov_int from summary.txt
df = pd.read_csv("/HDD/data/andrea/ld_score_regression/summary.txt", sep="\t")

def get_stats(idp):
    return df.loc[df["p1"]==idp]

def get_gcov_int(idp, phen):
    return get_stats(idp).loc[get_stats(idp)["p2"]==phen]["gcov_int"].values[0]

gcov_ints = {}

gcov_ints.update({"leftcaudate_diabetes": get_gcov_int("QSM_Left_caudate", "2443")})

X.matchAlleles('Diabetes','QSM_Left_caudate')

X.jointlyRank('Diabetes','QSM_Left_caudate')

R = X.score_all(E_A='Diabetes',E_B='QSM_Left_caudate', parallel=8, pcorr=gcov_ints["leftcaudate_diabetes"])

