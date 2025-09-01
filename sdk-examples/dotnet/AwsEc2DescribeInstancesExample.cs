// Example: Describing EC2 instances using AWS SDK for .NET

using Amazon.EC2;
using Amazon.EC2.Model;
using System;
using System.Threading.Tasks;

class AwsEc2DescribeInstancesExample
{
    static async Task Main()
    {
        var ec2Client = new AmazonEC2Client();

        var describeRequest = new DescribeInstancesRequest();
        var describeResponse = await ec2Client.DescribeInstancesAsync(describeRequest);

        foreach (var reservation in describeResponse.Reservations)
        {
            foreach (var instance in reservation.Instances)
            {
                Console.WriteLine($"Instance ID: {instance.InstanceId}, State: {instance.State.Name}");
            }
        }
    }
}