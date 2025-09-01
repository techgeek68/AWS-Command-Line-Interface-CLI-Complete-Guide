// Example: Put a custom metric data point to CloudWatch using AWS SDK v3 for Node.js

const { CloudWatchClient, PutMetricDataCommand } = require("@aws-sdk/client-cloudwatch");

// Create a CloudWatch client
const cloudWatchClient = new CloudWatchClient({ region: "us-east-1" });

async function putCustomMetric(namespace, metricName, value) {
  try {
    const params = {
      Namespace: namespace,
      MetricData: [
        {
          MetricName: metricName,
          Value: value,
          Unit: "Count",
        },
      ],
    };

    // Put metric data
    await cloudWatchClient.send(new PutMetricDataCommand(params));
    console.log(`Metric ${metricName} with value ${value} sent to CloudWatch.`);
  } catch (err) {
    console.error("Error putting metric data to CloudWatch:", err);
  }
}

// Usage example:
// putCustomMetric("MyCustomNamespace", "MyCustomMetric", 42);