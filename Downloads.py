#downloads objects from S3
import boto3
s3 = boto3.client('s3')

s3.download_file('asontiboto3', 'artiicle2.txt', 'artiicle2.txt')

#download single object
bucket = 'asontiboto3'
key = 'prac.txt'
filename = 'ptac.txt'

def download_obj(client, bucket, key, filename):
    client.download_file(bucket, key, filename)