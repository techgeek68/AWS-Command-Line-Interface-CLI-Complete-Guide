import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

response = ec2.describe_vpcs()
print("VPCs:")
for vpc in response['Vpcs']:
    print(f"  - VPC ID: {vpc['VpcId']} | CIDR: {vpc['CidrBlock']}")
