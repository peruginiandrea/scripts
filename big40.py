import os
import pandas as pd

# reading total volume from BIG40 dataset
# https://open.win.ox.ac.uk/ukbiobank/big40/
# IDP_T2_FLAIR_BIANCA_WMH_volume
# file 1437


DIRECTORY = "/HDD/data/andrea/WMH_BIG40"
os.chdir(DIRECTORY)

df = pd.read_csv("1437.txt", sep=" ")

df.dropna(subset=["pval(-log10)", "beta"], inplace=True)

# convert p-values

df["pval"] = df["pval(-log10)"].apply(lambda x: 10 ** (-x))

# add N column

n_col = pd.Series([32114 for _ in range(df.shape[0])], copy=False)

df["N"] = n_col

# ready for export

df.to_csv("volume_big40.txt", sep="\t", index=False)

