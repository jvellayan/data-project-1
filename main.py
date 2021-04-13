# import pandas to work with data frames
import pandas as pd

# read csv into dataframe
df = pd.read_csv("data/melb_data.csv")

# get total number of records
print("Total number of records: ", df.shape[0])
# get total number of columns
print("Total number of columns: ", len(df.columns))

# add a column that lists price per room
df["Price per room"] = df["Price"]/df["Rooms"]

# add a column that lists price landsize
df["Price landsize"] = df["Price"]/df["Landsize"]

