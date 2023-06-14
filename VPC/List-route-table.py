#list route tables
import boto3
ec2 = boto3.client('ec2')

response = ec2.describe_route_tables()
for table in response['RouteTables']:
    print('VPC ID: ', table['VpcId'], 'The RT:', table['RouteTableId'], )
    
    for association in table['Associations']:
        print(association['RouteTableAssociationId'])
        if 'SubnetId' in association:
            print(association['SubnetId'])
            
    for route in table['Routes']:
        print(route['DestinationCidrBlock'], route['GatewayId'])