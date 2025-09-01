// Example: Creating a CloudWatch Alarm using AWS SDK for .NET

using Amazon.CloudWatch;
using Amazon.CloudWatch.Model;
using System;
using System.Threading.Tasks;

class AwsCloudWatchExample
{
    static async Task Main()
    {
        var cloudWatchClient = new AmazonCloudWatchClient();

        var alarmRequest = new PutMetricAlarmRequest
        {
            AlarmName = "HighCPUUtilization", // Alarm name
            MetricName = "CPUUtilization",
            Namespace = "AWS/EC2",
            Statistic = Statistic.Average,
            Period = 300,
            EvaluationPeriods = 1,
            Threshold = 80.0,
            ComparisonOperator = ComparisonOperator.GreaterThanThreshold,
            AlarmActions = new List<string> 
            { 
                "arn:aws:sns:us-west-2:123456789012:my-sns-topic" // Replace with your SNS topic ARN
            },
            Dimensions = new List<Dimension>
            {
                new Dimension
                {
                    Name = "InstanceId",
                    Value = "i-1234567890abcdef0" // Replace with your instance ID
                }
            }
        };

        var response = await cloudWatchClient.PutMetricAlarmAsync(alarmRequest);
        Console.WriteLine("CloudWatch alarm created.");
    }
}