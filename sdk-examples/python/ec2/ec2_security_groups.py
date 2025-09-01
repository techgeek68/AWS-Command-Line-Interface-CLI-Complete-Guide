import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

response = ec2.describe_security_groups()
print("Security Groups:")
for sg in response['SecurityGroups']:
    print(f"  - {sg['GroupName']} (ID: {sg['GroupId']})")
