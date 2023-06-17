#Creating an ec2 instance with apache
import boto3
ec2 = boto3.client('ec2')

ami = 'ami-09e67e426f25ce0d7'
sg = 'sg-0098f861ce42be735'
kp = 'boto3KP'


def create_instance(client, ami_id, sg, kp, user_data=None):
    response = client.run_instances(
        ImageId= ami,
        InstanceType='t2.micro',
        KeyName=kp,
        MaxCount=1,
        MinCount=1,
        SecurityGroupIds=[sg],
        UserData =user_data
    )
    print(response['Instances'][0]['InstanceId'])

user_data ='''#!/bin/bash
apt update -y
apt-get install -y apache2
systemctl start apache2
systemctl enable apache2'''


create_instance(ec2, ami, sg, kp, user_data)