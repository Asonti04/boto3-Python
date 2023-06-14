#list subnets
import boto3
ec2 = boto3.client('ec2')

response = ec2.describe_subnets()
for subnet in response['Subnets']:
    print('CidrBlock: ', subnet['CidrBlock'], 'SubnetID: ', subnet['SubnetId'], 'The VPC: ', subnet['VpcId'])