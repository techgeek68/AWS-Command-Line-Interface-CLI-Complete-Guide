import boto3

s3 = boto3.resource("s3")
bucket_name = "your-bucket-name"
object_name = "largefile.bin"
file_path = "largefile.bin"

# Multipart upload (automatically handled by upload_file)
s3.Bucket(bucket_name).upload_file(file_path, object_name)
print(f"Multipart upload completed for '{object_name}'.")

# Server-side encryption (AES256)
s3.Object(bucket_name, object_name).put(
    Body=open(file_path, 'rb'),
    ServerSideEncryption='AES256'
)
print(f"Uploaded '{object_name}' with server-side encryption.")

# Object tagging
tags = {'TagSet': [{'Key': 'Project', 'Value': 'Demo'}, {'Key': 'Owner', 'Value': 'techgeek68'}]}
s3.Object(bucket_name, object_name).put_tagging(Tagging=tags)
print(f"Tags applied to '{object_name}'.")