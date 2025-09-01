import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

resource_id = 'i-0123456789abcdef0'  # Replace with your resource ID (instance, volume, etc.)
tags = [{'Key': 'Environment', 'Value': 'Development'}]

response = ec2.create_tags(Resources=[resource_id], Tags=tags)
print(f"Added tags to resource: {resource_id}")
