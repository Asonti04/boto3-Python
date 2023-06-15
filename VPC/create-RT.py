#Create routetables
import boto3
ec2 = boto3.client('ec2')

vpc_id = 'vpc-05184786bf345ba4c'

Routetable = ec2.create_route_table(VpcId=vpc_id,)

print(Routetable['RouteTable']['RouteTableId'])