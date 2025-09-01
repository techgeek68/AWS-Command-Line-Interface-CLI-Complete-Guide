import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

key_pair_name = 'MyNewKeyPair'
response = ec2.create_key_pair(KeyName=key_pair_name)
print(f"Created Key Pair: {key_pair_name}")
print(f"Private Key:\n{response['KeyMaterial']}")
