import boto3
import uuid

client = boto3.client('ec2',region_name='us-east-2')
response = client.describe_instances()
for ins in response['Reservations']:
    for vol in ins['Instances']:
        test = vol['InstanceId'],vol['State']['Name']
        print test


