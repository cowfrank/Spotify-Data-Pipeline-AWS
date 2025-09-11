import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime
import boto3   # ✅ KEEP this import (provided by Lambda, don’t bundle)

def lambda_handler(event, context):
    # 🔑 Environment variables (set in Lambda console)
    client_id = os.environ.get('SPOTIFY_CLIENT_ID')
    client_secret = os.environ.get('SPOTIFY_CLIENT_SECRET')
    bucket_name = os.environ.get('S3_BUCKET_RAW')

    # 🎶 Spotify connection
    client_credentials_manager = SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # ✅ Playlist to extract
    playlist_link = "https://open.spotify.com/playlist/40nIc5cBmMwoo3vPZ1DRgn?si=fb6d1c3c002f400f"
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]

    # 📥 Extract playlist items
    spotify_data = sp.playlist_items(playlist_URI)

    # 📤 Upload raw JSON to S3
    s3 = boto3.client('s3')
    filename = "spotify_raw_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".json"

    s3.put_object(
        Bucket=bucket_name,
        Key="to_processed/" + filename,
        Body=json.dumps(spotify_data)
    )

    print(f"✅ Uploaded {filename} to {bucket_name}/raw_data/to_processed/")
    print(f"✅ Number of tracks fetched: {len(spotify_data['items'])}")