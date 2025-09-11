# Spotify-Data-Pipeline-AWS
Python, AWS (S3, Lambda, Glue, and Athena), and PowerShell 
## Overview
On this project, we expect to Extract, Transform, and analyze data. Using Python/Lambda, we take Spotify's API and extract raw data into S3 buckets. In another Lambda function, we transform that data into an organized manner that allows AWS Glue to read each category and separate them into different Schemas. Lastly, we use Athena to create a database that allows us to query/sort the data
