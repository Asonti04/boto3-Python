#creating security group
import boto3
ec2 = boto3.client('ec2')

vpc = 'vpc-080c75941a31b1ae0'

response = ec2.create_security_group(
    Description='BOTO3',
    GroupName='my-boto-sg',
    VpcId=vpc,
)

print(response['GroupId'])