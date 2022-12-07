import pickle
import pandas as pd
from PascalX import xscorer

DIR_PHEN = "/HDD/data/andrea/phenotypes/"
DIR_QSM = "/HDD/data/andrea/QSM_T2/"
DIR_WMH = "/HDD/data/andrea/WMH/"
DIR_WMH40 = "/HDD/data/andrea/WMH_BIG40/"


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
    f"{DIR_PHEN}polished_2443.tsv",
    name="Diabetes",
    rscol=5,
    pcol=35,
    bcol=32,
    a1col=4,
    a2col=3,
    header=True,
)

X.load_GWAS(
    f"{DIR_PHEN}polished_21001_irnt.tsv",
    name="BMI",
    rscol=5,
    pcol=35,
    bcol=32,
    a1col=4,
    a2col=3,
    header=True,
)

X.load_GWAS(
    f"{DIR_PHEN}polished_4079_irnt.tsv",
    name="Diastolic BP",
    rscol=5,
    pcol=35,
    bcol=32,
    a1col=4,
    a2col=3,
    header=True,
)

X.load_GWAS(
    f"{DIR_PHEN}polished_30740_irnt.tsv",
    name="Glc",
    rscol=5,
    pcol=35,
    bcol=32,
    a1col=4,
    a2col=3,
    header=True,
)

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
    f"{DIR_PHEN}polished_6150_4.tsv",
    name="Hypertension",
    rscol=5,
    pcol=35,
    bcol=32,
    a1col=4,
    a2col=3,
    header=True,
)

X.load_GWAS(
    f"{DIR_PHEN}polished_104910.tsv",
    name="Moderate physical activity",
    rscol=5,
    pcol=35,
    bcol=32,
    a1col=4,
    a2col=3,
    header=True,
)

X.load_GWAS(
    f"{DIR_PHEN}polished_1239.tsv",
    name="Smoking",
    rscol=5,
    pcol=35,
    bcol=32,
    a1col=4,
    a2col=3,
    header=True,
)

X.load_GWAS(
    f"{DIR_PHEN}polished_6150_3.tsv",
    name="Stroke",
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
    f"{DIR_QSM}QSM_Left_caudate.txt",
    name="QSM_Left_caudate",
    rscol=0,
    pcol=7,
    bcol=5,
    a1col=4,
    a2col=3,
    header=True,
)

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
    f"{DIR_QSM}QSM_Left_putamen.txt",
    name="QSM_Left_putamen",
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

X.load_GWAS(
    f"{DIR_QSM}QSM_Right_putamen.txt",
    name="QSM_Right_putamen",
    rscol=0,
    pcol=7,
    bcol=5,
    a1col=4,
    a2col=3,
    header=True,
)

X.load_GWAS(
    f"{DIR_QSM}T2_WMH.txt",
    name="T2_WMH",
    rscol=0,
    pcol=7,
    bcol=5,
    a1col=4,
    a2col=3,
    header=True,
)

# different format
X.load_GWAS(
    f"{DIR_WMH}lesion.txt",
    name="lesion",
    rscol=1,
    pcol=11,
    bcol=10,
    a1col=4,
    a2col=3,
    header=True,
)
X.load_GWAS(
    f"{DIR_WMH}volume.txt",
    name="volume",
    rscol=1,
    pcol=11,
    bcol=10,
    a1col=4,
    a2col=3,
    header=True,
)

X.load_GWAS(
    f"{DIR_WMH40}volume_big40.txt",
    name="volume_big40",
    rscol=1,
    pcol=8,
    bcol=5,
    a1col=4,
    a2col=3,
    header=True,
)


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
# I also added certain pairs with "Moderate physical activity" when they were strongly correlated
# even if not significant

phenotypes = {
    "QSM_Left_caudate": ["BMI", "Diabetes", "Glc", "HDL"],
    "QSM_Left_SN": ["BMI", "HDL"],
    "QSM_Left_pallidum": ["Diabetes", "HDL", "Moderate physical activity"],
    "QSM_Left_putamen": ["BMI", "Diabetes"],
    "QSM_Right_SN": [
        "BMI",
        "Diabetes",
        "HDL",
        "Moderate physical activity",
        "Systolic BP",
    ],
    "QSM_Right_caudate": ["BMI", "Diabetes", "HDL"],
    "QSM_Right_pallidum": ["Diabetes", "HDL", "Moderate physical activity"],
    "QSM_Right_putamen": ["BMI", "Diabetes"],
    "T2_WMH": ["Hypertension"],
    "lesion": ["Hypertension"],
    "volume": ["Hypertension", "Moderate physical activity"],
    "volume_big40": [
        "Diastolic BP",
        "Hypertension",
        "Smoking",
        "Stroke",
        "Systolic BP",
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
        X.save_scores(f"../results/pascalx_score_{E_A}-{E_B}.txt")
        with open(f"../results/pascalx_score_{E_A}-{E_B}.pickle", "wb") as f:
            pickle.dump(R, f)
