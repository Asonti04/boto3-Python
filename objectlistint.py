import boto3

def filter_objects_extenstion(client, bucket, extension):
    keys = []
    response1 = client.list_objects_v2(Bucket=bucket)
    for content in response1['Contents']:
        if(extension in content['Key'][-(len(extension)):]):
            keys.append(content['Key'])
    return keys
s3 = boto3.client('s3')
response = s3.list_objects_v2(Bucket="asontiboto3")
print(response)
print('-------------------------------------------------')

#def list_objects(client, bucket, prefix=''):
    #keys = []
    #for content in response2['Contents']:
       # keys.append(content['Key'])
    #return keys

#response2 = list_objects(s3, 'asontiboto3', '/')  #works with the def
#print(response2)

print('-------------------------------------------------')

#prints just the namee ending in txt because the -4
for content in response['Contents']:
    if('.txt' in content['Key'][-4:]):
        print(content['Key'])
# response = s3.list_objects_v2(Bucket="asontiboto3", Prefix='folder/folder_a/") allowa you to pull from a specific folder
print('-------------------------------------------------')
#prints all names
for content in response['Contents']:
    print(content['Key'])
print('-------------------------------------------------')
#another way
extension = '.txt'
for content in response['Contents']:
    if(extension in content['Key'][-(len(extension)):]):
        print(content['Key'])
print('-------------------------------------------------')
        
response1 = filter_objects_extenstion(s3, 'asontiboto3', '.txt') #works with the def
print(response1)
print('-------------------------------------------------')