import boto3

s3 = boto3.resource("s3")
bucket_name = "your-bucket-name"
local_upload_file = "upload.txt"
object_name = "uploaded.txt"

# Upload an object
s3.Bucket(bucket_name).upload_file(local_upload_file, object_name)
print(f"Uploaded '{local_upload_file}' as '{object_name}'.")

# List objects in the bucket
print(f"Objects in '{bucket_name}':")
for obj in s3.Bucket(bucket_name).objects.all():
    print(f"  - {obj.key}")

# Download an object
download_path = "downloaded.txt"
s3.Bucket(bucket_name).download_file(object_name, download_path)
print(f"Downloaded '{object_name}' to '{download_path}'.")

# Copy object
copy_source = {'Bucket': bucket_name, 'Key': object_name}
copied_name = "copied.txt"
s3.Bucket(bucket_name).copy(copy_source, copied_name)
print(f"Copied '{object_name}' to '{copied_name}'.")

# Delete object
s3.Object(bucket_name, copied_name).delete()
print(f"Deleted object '{copied_name}'.")