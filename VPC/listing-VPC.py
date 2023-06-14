#Getting VPC INFO
import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_vpcs()

def get_vpc(client, filters=[]):
    response = ec2.describe_vpcs(Filters=filters)
    for vpc in response['Vpcs']:
        print('The VPC ID:', vpc['VpcId'], 'The CidrBlock: ', vpc['CidrBlock'], 'Default?', vpc['IsDefault'])

def get_vpc_name(client, filters=[]):
    response = ec2.describe_vpcs(Filters=filters)
    for vpc in response['Vpcs']:
        if 'Tags' in vpc:
            for tag in vpc['Tags']:
                if 'Name' == tag['Key']:
                    print('The VPC Name:', tag['Value'], 'The VPC ID:', vpc['VpcId'], 'The CidrBlock: ', vpc['CidrBlock'], 'Default?', vpc['IsDefault'])
                    
if __name__ == '__main__':
    ec2 = boto3.client('ec2')
    Filters=[
            {'Name': 'isDefault', 'Values': ['true',]},
        ]
    
    get_vpc(ec2)
    get_vpc_name(ec2)