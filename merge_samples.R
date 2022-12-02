setwd("/HDD/data/andrea/QSM_T2")

# actual filenames provided (for the ones we want)
files <- c(
    "0003", "0004", "0005", "0006", "0007", "0008", "0011",
    "0012", "0015", "0016", "0017", "0035"
)

# human readable filenames, in the same order as above, of course
# !IMPORTANT NOTE: every T2 actually means T2*
# (avoiding the star for simpler parsing)
names <- c(
    "QSM_Left_caudate", "QSM_Right_caudate", "QSM_Left_putamen",
    "QSM_Right_putamen", "QSM_Left_pallidum", "QSM_Right_pallidum",
    "QSM_Left_amygdala", "QSM_Right_amygdala", "QSM_Left_SN",
    "QSM_Right_SN", "QSM_WMH", "T2_WMH"
)

# we're going to merge both sample sets, discovery and replication

for (i in 1:length(files)) {
    gwas_rep <- read.table(paste0("repro/", files[i], ".txt"), header = TRUE)
    gwas_dis <- read.table(paste0("discov/", files[i], ".txt"), header = TRUE)

    print(paste("Reading data for", names[i], i))
    # remove missing values
    gwas_rep <- gwas_rep[complete.cases(gwas_rep), ]
    gwas_dis <- gwas_dis[complete.cases(gwas_dis), ]


    # remove duplicates for rsid column
    gwas_rep <- gwas_rep[!duplicated(gwas_rep$rsid), ]
    gwas_dis <- gwas_dis[!duplicated(gwas_dis$rsid), ]

    # keep only common rsid
    gwas <- merge(gwas_dis, gwas_rep, by = "rsid")



    # IVW (new beta and SE)
    weight_dis <- 1 / gwas$se.x^2
    weight_rep <- 1 / gwas$se.y^2

    beta <- (weight_rep * gwas$beta.y +
        weight_dis * gwas$beta.x) / (weight_rep +
        weight_dis)

    se <- 1 / sqrt(weight_dis + weight_rep)

    # add new beta and SE to merged dataframe

    gwas$beta <- beta
    gwas$se <- se

    # adding new p-value
    pval <- pchisq((gwas$beta / gwas$se)^2, df = 1, lower = FALSE)

    gwas$pval <- pval

    # add N column (known constant here)
    gwas$N <- rep(29579, length(gwas$beta))

    # remove unnecessary columns
    gwas <- subset(gwas, select = c(
        "rsid", "chr.x", "pos.x", "a1.x", "a2.x",
        "beta", "se", "pval", "N"
    ))

    names(gwas)[2] <- "chr"
    names(gwas)[3] <- "pos"
    names(gwas)[4] <- "a1"
    names(gwas)[5] <- "a2"

    print(paste("Writing", names[i], i))

    write.table(gwas, paste0(names[i], ".txt"), quote = FALSE, sep = "\t", row.names = FALSE)

    print(paste("Done writing", names[i], i))
}

print("Done!")