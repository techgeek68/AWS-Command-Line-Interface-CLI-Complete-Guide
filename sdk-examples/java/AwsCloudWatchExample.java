// Example: Creating a CloudWatch Alarm using AWS SDK for Java v2

import software.amazon.awssdk.services.cloudwatch.CloudWatchClient;
import software.amazon.awssdk.services.cloudwatch.model.*;

public class AwsCloudWatchExample {
    public static void main(String[] args) {
        CloudWatchClient cloudWatch = CloudWatchClient.create();

        PutMetricAlarmRequest alarmRequest = PutMetricAlarmRequest.builder()
                .alarmName("HighCPUUtilization") // Alarm name
                .metricName("CPUUtilization")
                .namespace("AWS/EC2")
                .statistic(Statistic.AVERAGE)
                .period(300)
                .evaluationPeriods(1)
                .threshold(80.0)
                .comparisonOperator(ComparisonOperator.GREATER_THAN_THRESHOLD)
                .alarmActions("arn:aws:sns:us-west-2:123456789012:my-sns-topic") // Replace with your SNS topic ARN
                .dimensions(Dimension.builder()
                    .name("InstanceId")
                    .value("i-1234567890abcdef0") // Replace with your instance ID
                    .build())
                .build();

        cloudWatch.putMetricAlarm(alarmRequest);

        System.out.println("CloudWatch alarm created.");

        cloudWatch.close();
    }
}