#route table routes
import boto3
ec2 = boto3.client('ec2')
rt_id = 'rtb-0173fc572e065be0c'
igw_id = 'igw-04f6a0a965670b9d6'
cidr = '0.0.0.0/0'
ec2.create_route(DestinationCidrBlock=cidr,GatewayId=igw_id,RouteTableId=rt_id)