#Deleting key pair
import boto3
ec2 = boto3.client('ec2')

kp = 'boto3KP'

response = ec2.delete_key_pair(
    KeyName=kp,
)

print(response)