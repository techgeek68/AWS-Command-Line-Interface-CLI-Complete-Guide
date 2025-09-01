// Example: Listing CloudWatch alarms using AWS SDK for .NET

using Amazon.CloudWatch;
using Amazon.CloudWatch.Model;
using System;
using System.Threading.Tasks;

class AwsCloudWatchListAlarmsExample
{
    static async Task Main()
    {
        var cloudWatchClient = new AmazonCloudWatchClient();
        var listRequest = new DescribeAlarmsRequest();
        var listResponse = await cloudWatchClient.DescribeAlarmsAsync(listRequest);

        foreach (var alarm in listResponse.MetricAlarms)
        {
            Console.WriteLine($"Alarm Name: {alarm.AlarmName}, State: {alarm.StateValue}");
        }
    }
}