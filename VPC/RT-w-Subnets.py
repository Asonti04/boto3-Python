#create a route table with subnet associations
import boto3
ec2 = boto3.client('ec2')

subnet = 'subnet-00cf8cbadab83d062'
rtid = 'rtb-0173fc572e065be0c'

association = ec2.associate_route_table(RouteTableId=rtid,SubnetId=subnet)

print(association['AssociationId'])