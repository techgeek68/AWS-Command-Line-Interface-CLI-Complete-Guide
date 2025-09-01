import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

response = ec2.run_instances(
    ImageId='ami-0abcdef1234567890',                          #Replace with valid AMI ID
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='your-key-pair-name',                             #Replace with your key pair
    SecurityGroupIds=['sg-0123456789abcdef0']                 #Replace with your security group ID
)

for instance in response['Instances']:
    print(f"Launched EC2 Instance: {instance['InstanceId']}")
