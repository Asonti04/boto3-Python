#Uploading to S3
import boto3
s3 = boto3.client('s3')

with open("test.txt", 'rb') as f:
    s3.put_object(Bucket="asontiboto3", Key="test.txt", Body=f, ContentType="text/plain") #this put in a textfile

#This is another way to add files to a bucket
s3.upload_file("prac.txt", "asontiboto3", 'prac_upload.txt', ExtraArgs={"ContentType": "text/plain"})

s3.put_object(Bucket="asontiboto3", Key="test_string.txt", Body="This is a string", ContentType="text/plain") 
#line 11 is a way to add a NEWfile while providing their own body text
