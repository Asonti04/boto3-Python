#creting ami
import boto3
ec2 = boto3.client('ec2')

response = ec2.create_image(
    Description='An AMI made with boto3',
    InstanceId='i-0683cfacf27f911f3',
    Name='Boto3AMI',
)

print(response['ImageId'])