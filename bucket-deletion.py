#empty and delete buckets
import boto3
s3 = boto3.client('s3')
bucket='asontiboto3'
def empty(client, bucket):
    response = client.list_objects_v2(Bucket=bucket)
   
    if "Contents" in response:
        objects= [{'Key': content['Key']} for content in response["Contents"]]
   
        response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects
        }
    )
    
        while response.get('NextContinuationToken'):
            response = client.list_objects_v2(Bucket=bucket, ContinuationToken=response['NextContinuationToken'])
            objects= [{'Key': content} for content in response["Contents"]]
            response = client.delete_objects(
                Bucket=bucket,
                Delete={
                    'Objects': objects
                }
            )
            

bucket='asontiboto3'

empty(s3, bucket)
response = s3.delete_bucket(
    Bucket=bucket
)