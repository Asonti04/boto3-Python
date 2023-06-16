#list instance types
import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instance_types(
     Filters=[
        {
            'Name': 'free-tier-eligible',
            'Values': [
                'true',
            ]
        },
    ],
    )
for instancetype in response['InstanceTypes']:
    print(instancetype['InstanceType'], instancetype['FreeTierEligible'])
   
#list ami's 
response2 = ec2.describe_images(Owners =['amazon'])

for image in response2['Images']:
    print(image['Name'], image['ImageId'], image['CreationDate'])

