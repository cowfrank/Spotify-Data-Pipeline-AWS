# Spotify-Data-Pipeline-AWS
Python, AWS (S3, Lambda, Glue, and Athena), and PowerShell 
## Overview
On this project, we expect to Extract, Transform, and Analyze data with AWS Services and Spotify's API. Using Python/Lambda, we take Spotify's API and extract raw data into S3 buckets. In another Lambda function, we transform that data into an organized manner that allows AWS Glue to read each category and separate them into different Schemas. Lastly, we use Athena to create a database that allows us to query/sort the data
## Instructions
### 1. S3 Buckets
First, you want to create S3 Buckets within Amazon Web Services. Let's start with the names. Create two buckets named "spotify-raw-(yourname)" and "spotify-transformed-(yourname). After this is completed, in each bucket, create folders in each respective bucket named "to_processed" in the raw bucket and "transformed" in the transform bucket. 
#### It should look like this 
![S3 Buckets](images/S3%20Buckets.PNG)
![S3 Folder](images/S3%20Folder.PNG)
### 2. Lambda/Python
In this step, create two Lambda Functions named "spotify-extractor" and "spotify_transformer".
#### Function names
![S3 Folder](images/Lambda%20Function.PNG)
Once this is complete, let's go into the spotify_extractor function. Input <a href="https://github.com/Grifynn/Spotify-Data-Pipeline-AWS/blob/main/spotify_api_data_extract.py" > spotify_api_data_extract.py</a> into the code source.<br> <br>
Scroll down to "Runtime settings" and change the "Handler" to spotify_api_data_extract.lambda_handler. ( Exact name of py file before lambda_handler)
#### Handler
![S3 Folder](images/Runtime%20Settings.PNG)<br> <br>
Then you want to set the Environment Variables. You have 3 you want to input<br> <br>
S3_BUCKET_RAW = (Your Raw S3 Bucket) eg. spotify-raw-frank<br><br>
SPOTIFY_CLIENT_ID <br>
SPOTIFY_CLIENT_SECRET <br>
##### I'LL SHOW YOU HOW TO OBTAINS THESE BELOW!<br>
#### Environment Variables (Bottom Left)
![S3 Folder](images/Environment%20Variables.PNG) <br><br>
#### Obtain Spotify Keys
Head over to https://developer.spotify.com/ and sign in with your regular Spotify account. Head over to the dashboard and find your keys. <br> <br>
![S3 Folder](images/Runtime%20Settings.PNG) 
<br>
Once you have obtained them, input them into your Environmental Keys. <br> <br>
Now repeat this exact process for <a href="https://github.com/Grifynn/Spotify-Data-Pipeline-AWS/blob/main/spotify_api_data_extract.py](https://github.com/On-car/spotify-end-to-end-data-engineering--project/blob/main/spotify_transformation_load_function.py)" >spotify_transformation_load_function.py</a>


