#Creating an ec2 instance
import boto3
ec2 = boto3.client('ec2')

ami = 'ami-0ca6563c823dd36a4'
sg = 'sg-0098f861ce42be735'
kp = 'boto3KP'

response = ec2.run_instances(
    ImageId= ami,
    InstanceType='t2.micro',
    KeyName=kp,
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[sg],
)

print(response['Instances'][0]['InstanceId'])