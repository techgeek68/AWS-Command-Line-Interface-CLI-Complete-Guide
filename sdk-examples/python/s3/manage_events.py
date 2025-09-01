import boto3

s3_client = boto3.client("s3")
bucket_name = "your-bucket-name"

# Set up an event notification to send to an SNS topic (replace with your topic ARN)
topic_arn = "arn:aws:sns:us-east-1:123456789012:YourSNSTopic"
notification_configuration = {
    'TopicConfigurations': [
        {
            'TopicArn': topic_arn,
            'Events': ['s3:ObjectCreated:*']
        }
    ]
}

s3_client.put_bucket_notification_configuration(
    Bucket=bucket_name,
    NotificationConfiguration=notification_configuration
)
print("Bucket event notification configured for ObjectCreated events.")