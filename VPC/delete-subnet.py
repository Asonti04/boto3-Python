#deleting subnet
import boto3
ec2 = boto3.client('ec2')

subnet = 'subnet-00cf8cbadab83d062'

ec2.delete_subnet(SubnetId=subnet)
