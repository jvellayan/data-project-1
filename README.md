# data-project-1

I chose to create an ETL data processor for my project.

## Extracting Data
The data used in this pipeline can be found on kaggle at the link below.

**https://www.kaggle.com/dansbecker/melbourne-housing-snapshot**

I uploaded the data to github, and utilized the GitHub raw url to import the data into the pipeline.

**https://raw.githubusercontent.com/jvellayan/data-project-1/main/data/melb_data.csv**

This dataset can be uploaded to any GitHub repository, and the corresponding raw GitHub url can replace the current one in the code. This would result in the same outputs; however, no changes need to be applied to the code in order for it to run correctly.

The data contains information about Melbourne Housing, including the number of rooms, housing prices, and much more. The pipeline initially prints some basic dataset information, including the number or records/rows, the number of columns and the number of NAs present.

## Transforming Data

The first thing done to transform the data is simply dropping all of the rows with NAs. This ended up dropping a large portion of the dataset. Usually, I would perform more data cleaning to try to salvage some of the rows with NAs, but for simplicity's sake, I decided to drop them instead. 

The second thing done to transform the data was creating two new columns. The first one is price per room, which is the price column divided by the rooms column. The second one is the price per landsize, which is the price column divided by the landsize column. Both of these columns will give us more insight on the housing situation in Melbourne. 

The last thing done to transform the data is dropping columns that would not be that useful in future analysis. Assuming that this dataset is going to be used for machine learning to predict housing prices or something similar, I decided to drop three columns. The first column dropped is called method, which is a categorical column with information about if/how the property was sold. Some example instances are: S - property sold; SP - property sold prior; PI - property passed in; PN - sold prior not disclosed; SN - sold not disclosed; NB - no bid; VB - vendor bid; W - withdrawn prior to auction; SA - sold after auction; SS - sold after auction price not disclosed. N/A - price or highest bid not available. The next column I dropped is CouncilArea, which lists the governing council area. There are many other location metrics in this dataset, like postcode, latitude, longitude, and region that would be more helpful than CouncilArea. The final column I dropped in Bedroom2, which is essentially a repeat of the room column, so it is not needed.

## Loading Data

After the data is cleaned up a bit, it is finally transformed into a JSON format. The JSON is now ready to be loaded into a S3, SQL database or something similar. 

## How to Use
No changes are required to run the ETL. Simply run the docker command and it will be downloaded from DockerHub then run: 

**docker run jlv7cr/jaya:5.0**

Then, you are done!

Below is the link to my DockerHub repositiories: 

**https://hub.docker.com/repository/docker/jlv7cr/jaya**

Here is the link of specific one for this project: 

**https://hub.docker.com/layers/145291237/jlv7cr/jaya/5.0/images/sha256-5040953d21337ed7a5ba638c858f3ca844a4e2a2f19ba2d80c64dae05f286eea?context=explore**

## How it Works

The main package I used in python is pandas. I simply used a url to get a csv, and converted this to a panada dataframe. It was easy to transform the data after this. The dockerfile simply installs python and the packages listed in requirements.txt, and then runs my main.py file.



