#pip3 install pandas
import os, glob
import pandas as pd

path = "./fixtures/"

filenames = glob.glob(os.path.join(path, "*.csv"))

# empty string to add files
res = []
for f in filenames:
    df = pd.read_csv(f, sep=',')
    # create a new column indicates origional name
    df['filename'] = f.split('/')[-1]
    res.append(df)

# use pandas to combine files
merged_df = pd.concat(res, ignore_index=True)
# export the table
merged_df.to_csv(path+"combined.csv", index = False)