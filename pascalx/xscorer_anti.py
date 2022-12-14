import pickle
import pandas as pd
from PascalX import xscorer

DIR_PHEN = "/HDD/data/andrea/phenotypes/"
DIR_QSM = "/HDD/data/andrea/QSM_T2/"
DIR_WMH = "/HDD/data/andrea/WMH/"
DIR_WMH40 = "/HDD/data/andrea/WMH_BIG40/"

# leftTail=True tests for anti-coherence
# we use this for negative correlations
X = xscorer.zsum(leftTail=True, gpu=True)


X.load_refpanel(
    "/SSD/home/hermione/reference_data/EUR.1KG.GRCh38",
    parallel=22,
    keepfile="/HDD/data/andrea/ref_panel/EUR_1KG_phase3_samples.tsv",
)

X.load_genome("/HDD/data/andrea/GRCh38_protein_coding.tsv")

# Loading GWAs

# I used:
# head -n 1 polished_2443.tsv | tr "\t" "\n" | awk '{print $0, "\t", NR-1}'
# to get a nicer formatting in order to find the corresponding column numbers





X.load_GWAS(
    f"{DIR_PHEN}polished_30760_irnt.tsv",
    name="HDL",
    rscol=5,
    pcol=35,
    bcol=32,
    a1col=4,
    a2col=3,
    header=True,
)







X.load_GWAS(
    f"{DIR_PHEN}polished_4080_irnt.tsv",
    name="Systolic BP",
    rscol=5,
    pcol=35,
    bcol=32,
    a1col=4,
    a2col=3,
    header=True,
)


######

X.load_GWAS(
    f"{DIR_QSM}QSM_Left_SN.txt",
    name="QSM_Left_SN",
    rscol=0,
    pcol=7,
    bcol=5,
    a1col=4,
    a2col=3,
    header=True,
)

X.load_GWAS(
    f"{DIR_QSM}QSM_Left_pallidum.txt",
    name="QSM_Left_pallidum",
    rscol=0,
    pcol=7,
    bcol=5,
    a1col=4,
    a2col=3,
    header=True,
)



X.load_GWAS(
    f"{DIR_QSM}QSM_Right_SN.txt",
    name="QSM_Right_SN",
    rscol=0,
    pcol=7,
    bcol=5,
    a1col=4,
    a2col=3,
    header=True,
)

X.load_GWAS(
    f"{DIR_QSM}QSM_Right_caudate.txt",
    name="QSM_Right_caudate",
    rscol=0,
    pcol=7,
    bcol=5,
    a1col=4,
    a2col=3,
    header=True,
)

X.load_GWAS(
    f"{DIR_QSM}QSM_Right_pallidum.txt",
    name="QSM_Right_pallidum",
    rscol=0,
    pcol=7,
    bcol=5,
    a1col=4,
    a2col=3,
    header=True,
)




# different format





# to correct for sample overlapping
# let's get gcov_int from summary.txt
df = pd.read_csv("/HDD/data/andrea/ld_score_regression/summary.txt", sep="\t")


def get_stats(idp):
    return df.loc[df["p1"] == idp]


gcov_ints = {}


def get_gcov_int(idp, phen):
    return get_stats(idp).loc[get_stats(idp)["p2"] == phen]["gcov_int"].values[0]


phen_names = {
    "100270": "Coffee intake",
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
    "6150_4": "Hypertension",
}

phen_id = {v: k for k, v in phen_names.items()}
# in the for loop below, gcov_ints is called with values from the names
# so we use its id to get the data from summary.txt for phenotypes


def gcov_ints_update(idp, phen):
    gcov_ints.update({f"{idp}-{phen}": get_gcov_int(idp, phen_id[phen])})


# Create a dictionary of the GWAS phenotypes and IDPs to combine with each

# I chose pairs that are significant in ldsc


phenotypes = {
    "QSM_Left_SN": [ "HDL"],
    "QSM_Left_pallidum": [
        "HDL",
    ],

    "QSM_Right_SN": [
        "HDL",
        "Systolic BP",
    ],
    "QSM_Right_caudate": ["HDL"],
    "QSM_Right_pallidum": [
        "HDL",
    ],
}



# Loop through all GWAS
for E_A, E_B_list in phenotypes.items():
    # Loop through the other phenotypes to combine with the current IDP
    for E_B in E_B_list:

        X.matchAlleles(E_A, E_B)
        X.jointlyRank(E_A, E_B)

        # Score
        gcov_ints_update(E_A, E_B)
        R = X.score_all(E_A=E_A, E_B=E_B, parallel=8, pcorr=gcov_ints[f"{E_A}-{E_B}"])

        # Save results
        X.save_scores(f"pascalx_score_{E_A}-{E_B}.txt")
        with open(f"pascalx_score_{E_A}-{E_B}.pickle", "wb") as f:
            pickle.dump(R, f)
