// Example: Launching an EC2 instance using AWS SDK for .NET

using Amazon.EC2;
using Amazon.EC2.Model;
using System;
using System.Threading.Tasks;

class AwsEc2Example
{
    static async Task Main()
    {
        var ec2Client = new AmazonEC2Client();

        var launchRequest = new RunInstancesRequest
        {
            ImageId = "ami-0abcdef1234567890", // Replace with a valid AMI ID
            InstanceType = InstanceType.T2Micro,
            MinCount = 1,
            MaxCount = 1
        };

        var launchResponse = await ec2Client.RunInstancesAsync(launchRequest);

        // Print the ID of the launched instance
        foreach (var instance in launchResponse.Reservation.Instances)
        {
            Console.WriteLine($"Launched EC2 instance with ID: {instance.InstanceId}");
        }
    }
}