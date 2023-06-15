#detaching internet gateway
import boto3
ec2 = boto3.client('ec2')

igw = 'igw-04f6a0a965670b9d6'
vpc_id = 'vpc-05184786bf345ba4c'

ec2.detach_internet_gateway(InternetGatewayId=igw,VpcId=vpc_id)