import boto3

s3 = boto3.resource("s3")
bucket_name = "your-bucket-name"

# Enable versioning
versioning = s3.BucketVersioning(bucket_name)
versioning.enable()
print(f"Versioning enabled for '{bucket_name}'.")

# Set lifecycle configuration (delete objects after 30 days)
lifecycle_configuration = {
    'Rules': [{
        'ID': 'Delete old objects',
        'Prefix': '',
        'Status': 'Enabled',
        'Expiration': {'Days': 30},
    }]
}
s3.BucketLifecycleConfiguration(bucket_name).put(LifecycleConfiguration=lifecycle_configuration)
print("Lifecycle rule applied: Delete objects after 30 days.")