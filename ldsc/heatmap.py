import os
import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.stats.multitest as sm

DIRECTORY = "/HDD/data/andrea/ld_score_regression/"
os.chdir(DIRECTORY)

# loading the data frame
df = pd.read_csv("summary.txt", sep="\t")

# let's rename the phenotypes
# because 21001 doesn't mean anything to me...

names = {
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

df = df.replace({"p2": names})

df["p1"] = df["p1"].apply(lambda x: x.replace("_", " "))
df["p1"] = df["p1"].apply(lambda x: x.replace("T2", "T2*"))

df["p1"] = df["p1"].replace({"lesion": "WMH Lesion count"}).replace({"volume": "WMH Volume"}).replace({"volume big40": "WMH Volume (Big40)"})

# pivot for correlations
cor = df.pivot(index="p1", columns="p2", values="rg")

# extracting p-values
pvals = df["p"]

# FDR correction
# first dimension is True/False for significance
corrected_pvals = sm.fdrcorrection(pvals)[0]

# let's add this info to the data frame
df["Significance"] = corrected_pvals

# the idea here is to change True to * and False to empty
# so we can just use this pivot as a label
df["sig"] = df["Significance"].apply(lambda x: "" if x == 0 else "*")

# almost same as previous pivot, but the values are the significance (boolean)
cpval = df.pivot(index="p1", columns="p2", values="sig")

# with annot parameter, we add the stars for significance
# fmt is needed to work with strings (would convert to numbers by default)
# (the way I did it, the star is just this character: *)
color = sns.color_palette("coolwarm_r", as_cmap=True)


fig = plt.figure()

# Create the axes in the figure
# ax = fig.subplots()

ax = sns.heatmap(cor, annot=cpval, fmt="", center=0, cmap=color, linecolor="black", linewidths=0.1)

ax.set_title("Estimated genetic correlation")

ax.hlines([10, 12], *ax.get_xlim())

ax.set(xlabel="Phenotypes", ylabel="Brain IDPs")
ax.title.set_weight('bold')

ax.xaxis.label.set_weight('bold')

ax.yaxis.label.set_weight('bold')

ax.xaxis.label.set_color('blue')
ax.yaxis.label.set_color('blue')

plt.show()
## I'm not currently using the following plot
# log10 transformation


df["log10p"] = sm.fdrcorrection(pvals)[1]
df["log10p"] = df["log10p"].apply(lambda x: -math.log10(x))

pval = df.pivot(index="p1", columns="p2", values="log10p")



fig = plt.figure()

# Create the axes in the figure
# ax = fig.subplots()

ax = sns.heatmap(pval, center=0, cmap=color, annot=cpval, fmt="", linecolor="black", linewidths=0.1)

ax.set_title("Estimated genetic correlation: -log10(p-value)")

ax.hlines([10, 12], *ax.get_xlim())

ax.set(xlabel="Phenotypes", ylabel="Brain IDPs")

ax.title.set_weight('bold')

ax.xaxis.label.set_weight('bold')

ax.yaxis.label.set_weight('bold')

ax.xaxis.label.set_color('blue')
ax.yaxis.label.set_color('blue')

plt.show()