#Internet Gatweay association with VPC
import boto3
ec2 = boto3.client('ec2')

igw_id = 'igw-04f6a0a965670b9d6'
vpc_id = 'vpc-05184786bf345ba4c'
ec2.attach_internet_gateway( InternetGatewayId=igw_id, VpcId=vpc_id,)