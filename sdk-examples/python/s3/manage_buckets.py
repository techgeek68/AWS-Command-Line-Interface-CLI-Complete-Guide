import boto3

s3 = boto3.resource("s3")

# Create a new bucket
bucket_name = "example-bucket-techgeek68"
s3.create_bucket(Bucket=bucket_name)
print(f"Bucket '{bucket_name}' created.")

# List all buckets
print("All Buckets:")
for bucket in s3.buckets.all():
    print(f"  - {bucket.name}")

# Delete a bucket
s3.Bucket(bucket_name).delete()
print(f"Bucket '{bucket_name}' deleted.")