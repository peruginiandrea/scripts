
# Choices

## IDPs

- White Matter Hyperintensity (WMH):
    - total volume
    - lesion count (only available in older stats with a smaller sample)
- QSM and T2\* for WMH
- QSM for (left and right):
    +  Caudate
    + Putamen
    + Pallidum
    + Substantia Nigra
    + Amygdala

## Phenotypes

### Risk factors

- 6150_4 hypertension (diagnosed)
- Diastolic blood pressure, automated reading
  (4079_irnt)
- Systolic blood pressure, automated reading
  (4080_irnt)
- Glucose (mmol/L)
  (30740_irnt)
- Diabetes diagnosed by doctor (2443)
- HDL cholesterol (mmol/L)
  (30760_irnt)
- LDL direct (mmol/L)
  (30780_irnt)
- Triglycerides (mmol/L)
  (30870_irnt)
- Body mass index (BMI) (21001_irnt)
- Filtered coffee intake (100270)
- Current tobacco smoking (1239)
- Sleep duration (1160)
- Alcohol intake frequency (1558)
- Time spent doing moderate physical activity (104910)

### Diseases

- Vascular/heart problems diagnosed by doctor: Stroke (6150_3)

# Data used

## IDPs

- BIG40: https://open.win.ox.ac.uk/ukbiobank/big40/
    - WMH total volume:
        - IDP_T2_FLAIR_BIANCA_WMH_volume
        - file 1437

- All other IDPs from: https://www.fmrib.ox.ac.uk/ukbiobank/gwas_resources/index.html

## Phenotypes

https://docs.google.com/spreadsheets/d/1kvPoupSzsSFBNSztMzl04xMoSC3Kcx3CrjVf4yBmESU/edit#gid=227859291


# Project structure

1. QSM and T2\* IDPs are downloaded in two separate folders: discovery and replication
The files from both samples are merged into one file per IDP via *merge_samples.R*.

2. Pasting variants.tsv to phenotypes summary stats via *merge_variants.sh*.

3. Various files need to be reformatted/polished/modified before running the other scripts. So run *sanitize_phen.py* before continuing.

4. LDSC
    i. *munge.sh*
    ii. *ld_score_regression.sh*

5. Run *log_parser.py* to generate a summary.txt file for the next step.
5. Visualize results of LDSC with *heatmap.py*.

6. PascalX