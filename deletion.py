#deleting object
import boto3
from objlist import list_objects_keys
s3 = boto3.client('s3')

bucket = 'asontiboto3'
key = 'cloudguru.yml'
response = s3.delete_object(
    Bucket=bucket,
    Key=key,
)

#delete multiple files 1
def delete(client, bucket, key):
    response = client.delete_object(
        Bucket= 'asontiboto3',
        Key= key
    )
        
    return response 
#delete multiple files         
def multidelete(client, bucket, keys):
   objects= [{'Key': key} for key in keys]
   
   response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects
        }
    )
   
   return response
   #delete contents inside a folder
if __name__ == '__main__':
    bucket = 'asontiboto3'
    prefix = 'randomfolder/f2/'  #delets only what is inside folder 2
    keys = list_objects_keys(s3, bucket, prefix=prefix)
    print(keys)
    keys = [key for key in keys if '/' not in key[len(prefix):]]
    print(keys)
    multidelete(s3, bucket, keys)
    
#delete folder & its content
if __name__ == '__main__':
    bucket = 'asontiboto3'
    keys = list_objects_keys(s3, bucket, prefix='myf1.txt_folder/')
    multidelete(s3, bucket, keys)
