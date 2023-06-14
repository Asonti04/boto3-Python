#listing Internet gatways
import boto3
ec2 = boto3.client('ec2')

response = ec2.describe_internet_gateways()
for ig in response['InternetGateways']:
    for attachment in ig['Attachments']:
        print(ig['InternetGatewayId'], attachment['VpcId'], attachment['State'])