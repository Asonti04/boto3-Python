#Deleting internet gateway
import boto3
ec2 = boto3.client('ec2')

igw = 'igw-04f6a0a965670b9d6'

ec2.delete_internet_gateway(InternetGatewayId=igw)