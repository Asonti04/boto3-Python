#deleting ami
import boto3
ec2 = boto3.client('ec2')

ami = 'ami-0ca6563c823dd36a4'

response = ec2.deregister_image(
    ImageId= ami,
)