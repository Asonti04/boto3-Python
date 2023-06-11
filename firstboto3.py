#making s3 bucket
import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket= 'asontiboto3'
)
    
print(response)