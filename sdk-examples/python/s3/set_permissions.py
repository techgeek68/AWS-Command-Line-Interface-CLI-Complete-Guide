import boto3

s3 = boto3.resource("s3")
bucket_name = "your-bucket-name"

# Set bucket policy (example policy: allow public read access)
bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "PublicReadGetObject",
        "Effect": "Allow",
        "Principal": "*",
        "Action": ["s3:GetObject"],
        "Resource": [f"arn:aws:s3:::{bucket_name}/*"]
    }]
}

bucket_policy_str = str(bucket_policy).replace("'", '"')
s3.Bucket(bucket_name).Policy().put(Policy=bucket_policy_str)
print("Bucket policy applied.")

# Set ACL (make bucket public-read)
s3.Bucket(bucket_name).Acl().put(ACL='public-read')
print("Bucket ACL set to public-read.")