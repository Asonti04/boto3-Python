#listing buckest with boto3
import boto3
s3 = boto3.client('s3')

response = s3.list_buckets()

Bucket = response['Buckets']

for buckets in Bucket:
    print(buckets['Name'], buckets['CreationDate'])