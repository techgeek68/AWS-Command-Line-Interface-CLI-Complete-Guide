import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')
instance_id = 'i-0123456789abcdef0'                      #Replace with your instance ID

response = ec2.stop_instances(InstanceIds=[instance_id])
print(f"Stopped Instance: {instance_id}")
