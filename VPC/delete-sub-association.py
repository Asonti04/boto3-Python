#deleting subnet associations with route tables
import boto3
ec2 =boto3.client('ec2')

rt_id = 'rtb-0173fc572e065be0c'

response = ec2.describe_route_tables(RouteTableIds=[rt_id],)

for association in response['RouteTables'][0]['Associations']:
    if not association['Main']:
        associationid = association['RouteTableAssociationId']
        print(associationid)
        ec2.disassociate_route_table(AssociationId=associationid)
