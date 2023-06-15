#Delete routes from route table
import boto3
ec2 = boto3.client('ec2')

rt_id = 'rtb-0173fc572e065be0c'

ec2.delete_route(DestinationCidrBlock='0.0.0.0/0', RouteTableId=rt_id)