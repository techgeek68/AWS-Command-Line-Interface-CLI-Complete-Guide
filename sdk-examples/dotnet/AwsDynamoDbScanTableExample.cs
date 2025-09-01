// Example: Scanning a DynamoDB table using AWS SDK for .NET

using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using System;
using System.Threading.Tasks;

class AwsDynamoDbScanTableExample
{
    static async Task Main()
    {
        var dynamoDbClient = new AmazonDynamoDBClient();
        var scanRequest = new ScanRequest
        {
            TableName = "YourTableName" // Replace with your table name
        };

        var scanResponse = await dynamoDbClient.ScanAsync(scanRequest);

        foreach (var item in scanResponse.Items)
        {
            Console.WriteLine($"Id: {item["Id"].S}, Name: {item["Name"].S}");
        }
    }
}