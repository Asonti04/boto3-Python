#prsigned Urls
import boto3
s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object', Params={'Bucket': 'asontiboto3', 'Key': 'test.txt'}, ExpiresIn=3000)
print(response)