import boto3
s3 = boto3.client('s3')
bucket = 'asontiboto3'

def list_objects_keys(client, bucket, prefix=''):
    keys = []
    response = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    for content in response["Contents"]:
        keys.append(content['Key'])
    
    return keys

response = list_objects_keys(s3, 'asontiboto3')  #works with the def
print(response)