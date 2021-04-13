# import pandas to work with data frames
import pandas as pd

# read csv into dataframe
df = pd.read_csv("data/heart.csv")

# get total number of records
print("Total number of records: ", df.shape[0])
# get total number of columns
print("Total number of columns: ", len(df.columns))

