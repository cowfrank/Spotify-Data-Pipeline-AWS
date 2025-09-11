import json
import boto3
import os
from datetime import datetime
import io


def lambda_handler(event=None, context=None):
    # Get bucket names from environment variables
    raw_bucket = os.environ.get('S3_BUCKET_RAW')
    transformed_bucket = os.environ.get('S3_BUCKET_TRANSFORMED')

    if not raw_bucket or not transformed_bucket:
        print("❌ Missing environment variables (S3_BUCKET_RAW, S3_BUCKET_RAW, S3_BUCKET_TRANSFORMED)")
        return

    s3 = boto3.client('s3')

    # 1. Find the latest raw file in S3
    response = s3.list_objects_v2(Bucket=raw_bucket, Prefix="to_processed/")
    if 'Contents' not in response:
        print("❌ No raw files found in bucket:", raw_bucket)
        return

    # Sort files by last modified date
    files = sorted(response['Contents'], key=lambda x: x['LastModified'], reverse=True)
    latest_file = files[0]['Key']

    print(f"📂 Found latest raw file: {latest_file}")

    # 2. Download the raw JSON
    raw_obj = s3.get_object(Bucket=raw_bucket, Key=latest_file)
    raw_data = json.loads(raw_obj['Body'].read().decode('utf-8'))

    # Sort the raw data by track popularity before processing
    # The 'popularity' score is a proxy for how often a track is played globally
    sorted_items = sorted(raw_data['items'], key=lambda x: x['track']['popularity'], reverse=True)

    print(f"📥 Downloaded {latest_file}, contains {len(sorted_items)} tracks (sorted by popularity)")

    # 3. Transform the data and prepare for upload
    output_buffer = io.StringIO()
    record_count = 0
    for item in sorted_items:
        track = item['track']
        transformed_record = {
            "track_id": track['id'],
            "track_name": track['name'],
            "artist": track['artists'][0]['name'] if track['artists'] else None,
            "album": track['album']['name'],
            "release_date": track['album']['release_date'],
            "added_at": item['added_at'],
            "popularity": track['popularity']  # Include the popularity score
        }
        # Write each record as a JSON line
        output_buffer.write(json.dumps(transformed_record) + "\n")
        record_count += 1

    print(f"🔄 Transformed {record_count} tracks")

    # Get the buffer's content
    json_lines_output = output_buffer.getvalue()

    # 4. Upload transformed JSON Lines to new bucket
    filename = "spotify_transformed_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".jsonl"
    s3.put_object(
        Bucket=transformed_bucket,
        Key="transformed/" + filename,
        Body=json_lines_output.encode('utf-8')

    )

    print(f"✅ Uploaded {filename} to {transformed_bucket}/raw_data/to_processed/")
    print(f"✅ Number of tracks fetched: {len(sorted_items)}")