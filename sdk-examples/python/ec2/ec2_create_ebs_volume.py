import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

response = ec2.create_volume(
    AvailabilityZone='us-east-1a',
    Size=8,                                          #Size in GiB
    VolumeType='gp2'
)
print(f"Created EBS Volume: {response['VolumeId']}")
