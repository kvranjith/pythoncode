import boto3
import uuid

random_id = str(uuid.uuid4())
print random_id
client = boto3.client('ec2',region_name='us-east-2')
response = client.describe_instances()
for ins in response['Reservations']:
    for vol in ins['Instances']:
        test = vol['InstanceId'],vol['State']['Name']
        print "output",random_id,'-',test


