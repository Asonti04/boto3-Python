#deleting VPC
import boto3
ec2 = boto3.client('ec2')

vpc_id = 'vpc-05184786bf345ba4c'

ec2.delete_vpc(VpcId=vpc_id)