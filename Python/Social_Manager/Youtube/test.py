import httplib2
import os
import random
import sys
import time
import mysql.connector

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

# Explicitly tell the underlying HTTP transport library not to retry, since we are handling retry logic ourselves.
httplib2.RETRIES = 1

# Maximum number of times to retry before giving up.
MAX_RETRIES = 10

# Always retry when these exceptions are raised.
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError)

# Always retry when an apiclient.errors.HttpError with one of these status codes is raised.
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains the OAuth 2.0 information for this application, including its client_id and client_secret.
CLIENT_SECRETS_FILE = "client_secrets.json"

# This OAuth 2.0 access scope allows an application to upload files to the authenticated user's YouTube channel, but doesn't allow other types of access.
YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is missing.
MISSING_CLIENT_SECRETS_MESSAGE = f"""
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file found at:

   {os.path.abspath(os.path.join(os.path.dirname(__file__), CLIENT_SECRETS_FILE))}

with information from the API Console https://console.cloud.google.com/

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
"""

VALID_PRIVACY_STATUSES = ("public", "private", "unlisted")

def get_authenticated_service():
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
                                   scope=YOUTUBE_UPLOAD_SCOPE,
                                   message=MISSING_CLIENT_SECRETS_MESSAGE)

    storage = Storage(f"{sys.argv[0]}-oauth2.json")
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage, argparser.parse_args())

    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                 http=credentials.authorize(httplib2.Http()))

def initialize_upload(youtube, options):
    tags = None
    if options['keywords']:
        tags = options['keywords'].split(",")

    body = dict(
        snippet=dict(
            title=options['title'],
            description=options['description'],
            tags=tags,
            categoryId=options['category']
        ),
        status=dict(
            privacyStatus=options['privacyStatus']
        )
    )

    # Call the API's videos.insert method to create and upload the video.
    insert_request = youtube.videos().insert(
        part=",".join(body.keys()),
        body=body,
        media_body=MediaFileUpload(options['file'], chunksize=-1, resumable=True)
    )

    resumable_upload(insert_request)

# This method implements an exponential backoff strategy to resume a failed upload.
def resumable_upload(insert_request):
    response = None
    error = None
    retry = 0
    while response is None:
        try:
            print("Uploading file...")
            status, response = insert_request.next_chunk()
            if response is not None:
                if 'id' in response:
                    print("Video id was successfully uploaded.", response['id'])
                else:
                    exit(f"The upload failed with an unexpected response: {response}")
        except HttpError as e:
            if e.resp.status in RETRIABLE_STATUS_CODES:
                error = f"A retriable HTTP error {e.resp.status} occurred:\n{e.content}"
            else:
                raise
        except RETRIABLE_EXCEPTIONS as e:
            error = f"A retriable error occurred: {e}"

        if error is not None:
            print(error)
            retry += 1
            if retry > MAX_RETRIES:
                exit("No longer attempting to retry.")

            max_sleep = 2 ** retry
            sleep_seconds = random.random() * max_sleep
            print(f"Sleeping {sleep_seconds} seconds and then retrying...")
            time.sleep(sleep_seconds)

def get_video_data_from_db():
    # Replace with your actual database connection details
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='client_upload'
    )
    cursor = conn.cursor(dictionary=True)
    
    # Replace with your actual table name and conditions
    cursor.execute("SELECT file, title, description, category, keywords, privacyStatus FROM videos WHERE id = 1")
    
    result = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return result

if __name__ == '__main__':
    video_data = get_video_data_from_db()

    if not os.path.exists(video_data['file']):
        exit("Please specify a valid file in the database.")

    youtube = get_authenticated_service()
    try:
        initialize_upload(youtube, video_data)
    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred:\n{e.content}")
