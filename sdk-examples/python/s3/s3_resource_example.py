import boto3

# Create an S3 resource object (default region from your AWS config)
s3_resource = boto3.resource("s3")

# Print a human-readable description of the resource object
print("Successfully created S3 resource object.")
print(f"Resource Info:\nService: {s3_resource.meta.service_name}")

# Example: List all S3 bucket names in a clean format
print("Your S3 Buckets:")
for bucket in s3_resource.buckets.all():
    print(f"  - {bucket.name}")