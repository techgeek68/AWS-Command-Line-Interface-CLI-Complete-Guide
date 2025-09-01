import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

response = ec2.detach_volume(
    VolumeId='vol-0123456789abcdef0',  # Replace with your Volume ID
    InstanceId='i-0123456789abcdef0'   # Replace with your Instance ID
)
print(f"Detached Volume: {response['VolumeId']}")
