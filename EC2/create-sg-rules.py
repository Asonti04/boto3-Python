#add rules to security gruops
import boto3
ec2 = boto3.client('ec2')

sg = 'sg-0098f861ce42be735'

response = ec2.authorize_security_group_ingress(
    GroupId= sg,
    IpPermissions=[
        {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                },
            ],
            'ToPort': 22,
        },
        {
            'FromPort': 80,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': '0.0.0.0/0',
                },
            ],
            'ToPort': 80,
        },
    ],
)

print(response)