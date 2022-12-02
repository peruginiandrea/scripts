import os
import re
import pandas as pd

####  PHENOTYPES  ############

DIRECTORY = "/HDD/data/andrea/phenotypes/"
os.chdir(DIRECTORY)

# to iterate over all files
list_dir = os.listdir(DIRECTORY)


for file in list_dir:
    if os.path.isfile(file) and file.startswith("variants_"):

        df = pd.read_csv(file, sep="\t")

        # removing NAs
        df.dropna(subset=["pval", "beta"], inplace=True)

        # removing low confidence variants
        df = df[df["low_confidence_variant"] == False]

        # adding a column for N
        df["N"] = df["n_complete_samples"]

        # extracting a short identifier from the file
        # e.g. '1558' instead of
        #'variants_1558.gwas.imputed_v3.both_sexes.tsv'
        # we can use this to write the polished tsv
        # this variable holds the full pattern "_1558."
        # match.group(1) returns the inner value "1558"
        match = re.search(r"_(\w+)\.", file)
        # ex. output "polished_1558.tsv"
        df.to_csv(f"polished_{match.group(1)}.tsv", sep="\t", index=False)

####  WMH  ########

"""
The GWAS summary statistics for WMH files follow a different format

stats.txt contains a header (chr rsid pos a1 a2 af info)


we also need the data from b.txt and p.txt
these files lack a header
each column represents an IDP, each row is for a SNP

additionally, we need to convert -log10(p) to p
and add an N column (unfortunately this info is not included)

!ALSO: just sadly realized the sep is a simple space and not a tab for these...
"""

DIRECTORY = "/HDD/data/andrea/WMH/"

os.chdir(DIRECTORY)


# reading the data

# no need for a loop this time since we are only working with 3
# files, which we'll treat slightly differently...
stats_df = pd.read_csv("stats.txt", sep=" ")
beta_df = pd.read_csv("b.txt", sep=" ", header=None)
p_df = pd.read_csv("p.txt", sep=" ", header=None)


# IDP_T2_FLAIR_BIANCA_WMH_volume original WMH IDP: total WMH volume
# LesionCount total number of WMH clusters
# respectively, 1st column and 9th column

####volume

# adding basic header for now
betas = [f"beta{i+1}" for i in range(11)]
pvals = [f"p{i+1}" for i in range(11)]
beta_df.columns = betas
p_df.columns = pvals

# we need to add an N column
# I got this number from "The following GWAS were carried out with the 8428 subject
# as described in the Elliott et al bioRxiv paper."
n_col = pd.Series([8428 for _ in range(stats_df.shape[0])], copy=False)


# convert p-values
p_df2 = p_df.apply(lambda x: 10 ** (-x))

# get first column
volume_beta = beta_df.filter(["beta1"], axis=1)
volume_p = p_df2.filter(["p1"], axis=1)

# stitching it up
volume_df = pd.concat([stats_df, volume_beta, volume_p], axis=1)

# adding missing proper column name for N (i.e. since it's a pd.Series,
# its header would be set to 0 automatically after my previous concat and it's immutable)
# so it must be added separately
volume_df["N"] = n_col

####lesion count

# get 9th column
lesion_beta = beta_df.filter(["beta9"], axis=1)
lesion_p = p_df2.filter(["p9"], axis=1)

# stitching it up
lesion_df = pd.concat([stats_df, lesion_beta, lesion_p], axis=1)

lesion_df["N"] = n_col

#fixing names (removing index from beta and p)
volume_df["beta"] = volume_df["beta1"]
volume_df.drop("beta1", axis=1)
volume_df["pval"] = volume_df["p1"]
volume_df.drop("p1", axis=1)


lesion_df["beta"] = lesion_df["beta9"]
lesion_df.drop("beta9", axis=1)
lesion_df["pval"] = lesion_df["p9"]
lesion_df.drop("p9", axis=1)

#polishing it up
volume_df.dropna(subset=["pval", "beta"], inplace=True)
volume_df.dropna(subset=["pval", "beta"], inplace=True)

# last but not least
volume_df.to_csv("volume.txt", sep="\t", index=False)
lesion_df.to_csv("lesion.txt", sep="\t", index=False)


### big40


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
