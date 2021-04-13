# import pandas to work with data frames
import pandas as pd
# import requests and io to handle getting data from a url
import requests
import io

# get csv from url
url = 'https://raw.githubusercontent.com/jvellayan/data-project-1/main/data/melb_data.csv'

# reading the downloaded content
download = requests.get(url).content

# convert to dataframe
df = pd.read_csv(io.StringIO(download.decode('utf-8')))

# get total number of records
print("Total number of records: ", df.shape[0])
# get total number of columns
print("Total number of columns: ", len(df.columns))
# get the total number of NAs
print("Total number of NA: ", df.isna().sum().sum())

# get column type information
print("Column Type: ")
print(df.info())
# more stats
print("Count, mean, std, min, max and distribution stats for each column: ")
with pd.option_context('display.max_columns', 40):
    print(df.describe(include='all'))


# drop all rows with NA, usually with as many NAs as this df has, we would try to salvage some of this data,
# but dropped it for simplicity
df = df.dropna()

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
# get total number of records
print("New number of records after dropping NA: ", df.shape[0])
# get the total number of NAs
print("New number of NA: ", df.isna().sum().sum())

# convert data frame to json
df.to_json("data/melb_data.json")

