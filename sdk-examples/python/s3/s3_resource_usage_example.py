import boto3

# Create an S3 resource object
s3 = boto3.resource("s3")

# List all buckets
print("Buckets:")
for bucket in s3.buckets.all():
    print(f"  - {bucket.name}")

# Upload a file to a bucket
bucket_name = "your-bucket-name"
file_path = "local_file.txt"
object_name = "uploaded_file.txt"
s3.Bucket(bucket_name).upload_file(file_path, object_name)
print(f"Uploaded '{file_path}' as '{object_name}' in bucket '{bucket_name}'.")

# Download a file from a bucket
s3.Bucket(bucket_name).download_file(object_name, "downloaded_file.txt")
print(f"Downloaded '{object_name}' from bucket '{bucket_name}' to 'downloaded_file.txt'.")

# List objects in a bucket
print(f"Objects in bucket '{bucket_name}':")
for obj in s3.Bucket(bucket_name).objects.all():
    print(f"  - {obj.key}")