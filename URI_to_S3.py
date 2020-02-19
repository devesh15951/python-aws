import requests
import boto3
import urllib.request

s3_client = boto3.client(
    's3',
    aws_access_key_id="MYOWNKEYID",
    aws_secret_access_key="USEYOUROWNKEY",
)

gz_link = "https://LINKOFTHEURI"

bucket_name="TARGET_BUCKET"
object_name="TARGET_OBJECT"

with urllib.request.urlopen(gz_link) as url:
    response = s3_client.upload_fileobj(url, bucket_name, object_name)
