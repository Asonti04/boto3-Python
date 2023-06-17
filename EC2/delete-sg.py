#delete security group
import boto3
ec2 = boto3.client('ec2')

sg = 'sg-0098f861ce42be735'


response = ec2.delete_security_group(
    GroupId= sg,
)

print(response)