// Example: Uploading a file to S3 using AWS SDK for .NET

using Amazon.S3;
using Amazon.S3.Model;
using System;
using System.IO;
using System.Threading.Tasks;

class AwsS3Example
{
    static async Task Main()
    {
        var s3Client = new AmazonS3Client();
        var bucketName = "your-bucket-name"; // Replace with your bucket name
        var keyName = "example.txt";
        var filePath = "/path/to/example.txt"; // Replace with your file path

        using (var fileStream = new FileStream(filePath, FileMode.Open, FileAccess.Read))
        {
            var putRequest = new PutObjectRequest
            {
                BucketName = bucketName,
                Key = keyName,
                InputStream = fileStream
            };

            var response = await s3Client.PutObjectAsync(putRequest);
            Console.WriteLine("File uploaded to S3.");
        }
    }
}