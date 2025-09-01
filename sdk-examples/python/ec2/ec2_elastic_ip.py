import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

# Allocate a new Elastic IP
allocation = ec2.allocate_address(Domain='vpc')
print(f"Allocated Elastic IP: {allocation['PublicIp']} (Allocation ID: {allocation['AllocationId']})")
