# Spotify-Data-Pipeline-AWS
Python, AWS (S3, Lambda, Glue, and Athena), and PowerShell 
## Overview
On this project, we expect to Extract, Transform, and Analyze data with AWS Services and Spotify's API. Using Python/Lambda, we take Spotify's API and extract raw data into S3 buckets. In another Lambda function, we transform that data into an organized manner that allows AWS Glue to read each category and separate them into different Schemas. Lastly, we use Athena to create a database that allows us to query/sort the data
## Instructions
### 1. S3 Buckets
First, you want to create S3 Buckets within Amazon Web Services. Let's start with the names. Create two buckets named "spotify-raw-(yourname)" and "spotify-transformed-(yourname). After this is completed, in each bucket, create folders in each respective bucket named "to_processed" in the raw bucket and "transformed" in the transform bucket. 
#### It should look like this 
 ![Image Alt]([image_url](https://github.com/Grifynn/Spotify-Data-Pipeline-AWS/blob/main/images/S3%20Buckets.PNG))
