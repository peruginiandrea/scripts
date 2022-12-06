import os
import re
import pandas as pd

DIRECTORY = "/HDD/data/andrea/ld_score_regression/"
os.chdir(DIRECTORY)

list_dir = os.listdir(DIRECTORY)

# returns a match for the line containing "Summary"
def get_summary(line):
    return re.search(r"Summary", line)


# returns a match for every non-whitespace character
def extract_data(line):
    return re.findall(r"\S+", line)


# saves a new .txt file with the data frame from each log
def save_results(data, name):
    df = pd.DataFrame([data])
    df.columns = [
        "p1",
        "p2",
        "rg",
        "se",
        "z",
        "p",
        "h2_obs",
        "h2_obs_se",
        "h2_int",
        "h2_int_se",
        "gcov_int",
        "gcov_int_se",
    ]

    df.to_csv(f"{name}.txt", sep="\t", index=False)
    print(f"{name} saved")


data_line = ""
for file in list_dir:
    if os.path.isfile(file) and file.endswith(".log"):
        with open(file, "r") as f:
            print(f"Reading log file: {file}")

            lines = f.readlines()

            for i, line in enumerate(lines):
                if get_summary(line):
                    print(f"Summary at line {i}")
                    data_line = lines[i + 2]
                    break
            print(extract_data(data_line))
            save_results(extract_data(data_line), file)

print("Done!")

### grouping all results in one single file
list_dir = os.listdir(DIRECTORY)
df_list = []
for file in list_dir:
    if os.path.isfile(file) and file.endswith(".txt") and file != "summary.txt":
        df = pd.read_csv(file, sep="\t")

        # removing unnecessary file paths and extensions, to make it more readable
        df["p1"] = df["p1"].apply(lambda x: x.rsplit("/", 1)[1])
        df["p1"] = df["p1"].apply(lambda x: x.split(".", 1)[0])

        df["p2"] = df["p2"].apply(lambda x: x.rsplit("/", 1)[1])
        df["p2"] = df["p2"].apply(lambda x: x.split(".", 1)[0])

        df["p2"] = df["p2"].apply(lambda x: x.rsplit("polished_", 1)[1])
        df_list.append(df)


df = pd.concat(df_list, axis=0)
print(df)
df.to_csv("summary.txt", sep="\t", index=False)
print("All done!")
