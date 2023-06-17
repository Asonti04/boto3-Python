#creating key pair
import boto3
import os 

ec2 = boto3.client('ec2')

file_name = 'KPfromboto3.pem'
response = ec2.create_key_pair(
    KeyName='boto3KP',
)

with open(file_name, 'w') as f:
    f.write(response['KeyMaterial'])
    
    
os.chmod(file_name, 0o400)

print(response['KeyName'])