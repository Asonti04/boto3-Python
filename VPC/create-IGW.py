#creating internet GateWay
import boto3
ec2 = boto3.client('ec2')

IGW = ec2.create_internet_gateway()

print(IGW['InternetGateway']['InternetGatewayId'])