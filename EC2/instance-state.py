#modify ec2 instance state
import boto3
ec2 = boto3.client('ec2')

instance = 'i-0fcc2051104ceeecf'

def stop_instance(client, instance):
    response = ec2.stop_instances(
        InstanceIds=[instance,],
)
    print(instance, 'Stopped')

def start_instance(client, instance):
    response = ec2.start_instances(
        InstanceIds=[instance,],
)
    print(instance, 'Started')

def terminate_instance(client, instance):
    response = ec2.terminate_instances(
        InstanceIds=[instance,],
)
    print(instance, 'terminated')

if __name__ == '__main__':
    instance = 'i-0fcc2051104ceeecf'

    terminate_instance(ec2, instance)