import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

response = ec2.create_image(
    InstanceId='i-0123456789abcdef0',              #Replace with your instance ID
    Name='MyServerImage',
    Description='AMI created from my instance'
)
print(f"Created AMI: {response['ImageId']}")
