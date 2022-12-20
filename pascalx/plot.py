from PascalX import genescorer
import matplotlib.pyplot as plt
import pandas as pd
import math
import glob

Scorer = genescorer.chi2sum()

Scorer = genescorer.chi2sum()
Scorer.load_refpanel(
     "/SSD/home/hermione/reference_data/EUR.1KG.GRCh38",
     parallel=22,
     keepfile="/HDD/data/andrea/ref_panel/EUR_1KG_phase3_samples.tsv",
 )
Scorer.load_genome("/HDD/data/andrea/GRCh38_protein_coding.tsv")

# Get a list of all .txt files starting with 'pascalx_score' in the '/SSD/scratch/andrea/scripts/' directory
txt_files = glob.glob('/SSD/scratch/andrea/scripts/pascalx_score*.txt')

# Get a list of all .txt files starting with 'pascalx_score' in the '/SSD/scratch/andrea/scripts/pascalx/' directory
txt_files += glob.glob('/SSD/scratch/andrea/scripts/pascalx/pascalx_score*.txt')



def plot(filepath):
    df = pd.read_csv(filepath, sep="\t", header=None)

    threshold = 0.05 / len(df)
    mask = df.iloc[:, 1] < threshold
    result = df.loc[mask, df.columns]

    result = result.sort_values(by=df.columns[1], ascending=True)

    log10_threshold = math.ceil(-math.log10(threshold))

    name = ' '.join(filepath.split('_')[2:]).replace('.txt', '').replace('-', '  —  ')

    top_10 = result[0].values[:10]
    print(top_10)

    # Create a new figure with a specific size
    fig = plt.figure(figsize=(12, 8))

    # Create the axes in the figure
    ax = fig.subplots()


    ax.set_title(name)
    ax.title.set_weight('bold')
    Scorer.load_scores(filepath)

    Scorer.plot_Manhattan(logsigThreshold=log10_threshold+3, sigLine=threshold)

    plt.show()


for file in txt_files:
    plot(file)
