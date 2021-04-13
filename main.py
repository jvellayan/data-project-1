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

# get rid of a few useless columns
del df['Method']
del df['CouncilArea']
del df['Bedroom2']

# get total number of columns
print("New number of columns after adding and deleting columns: ", len(df.columns))

df.to_json("data/melb_data.json")