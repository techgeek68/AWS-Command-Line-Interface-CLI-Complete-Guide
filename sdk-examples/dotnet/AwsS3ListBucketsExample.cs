// Example: Listing all S3 buckets using AWS SDK for .NET

using Amazon.S3;
using System;
using System.Threading.Tasks;

class AwsS3ListBucketsExample
{
    static async Task Main()
    {
        var s3Client = new AmazonS3Client();
        var response = await s3Client.ListBucketsAsync();

        foreach (var bucket in response.Buckets)
        {
            Console.WriteLine($"Bucket Name: {bucket.BucketName}, Created On: {bucket.CreationDate}");
        }
    }
}