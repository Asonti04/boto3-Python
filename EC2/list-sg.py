#listing security groups
import boto3
ec2 = boto3.client('ec2')

response = ec2.describe_security_groups()

for sg in response['SecurityGroups']:
    print(sg['GroupName'], sg['GroupId'], sg['VpcId'], sg['Description'])
    
   
    for permissions in sg['IpPermissions']:
        if 'FromPort' in permissions:
            print(permissions['FromPort'], permissions['IpProtocol'], permissions['ToPort'])
            
        if 'IpRanges' in permissions:
            for iprange in permissions['IpRanges']:
                print(iprange['CidrIp'])