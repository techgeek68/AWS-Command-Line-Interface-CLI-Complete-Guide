import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

image_id = 'ami-0abcdef1234567890'                  #Replace with your AMI ID

response = ec2.deregister_image(ImageId=image_id)
print(f"Deregistered AMI: {image_id}")
