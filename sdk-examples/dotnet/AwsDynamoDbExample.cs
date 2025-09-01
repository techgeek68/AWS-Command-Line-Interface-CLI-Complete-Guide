// Example: Inserting an item into DynamoDB using AWS SDK for .NET

using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

class AwsDynamoDbExample
{
    static async Task Main()
    {
        var dynamoDbClient = new AmazonDynamoDBClient();

        var item = new Dictionary<string, AttributeValue>
        {
            { "Id", new AttributeValue { S = "101" } },
            { "Name", new AttributeValue { S = "Sample Item" } }
        };

        var putRequest = new PutItemRequest
        {
            TableName = "YourTableName", // Replace with your table name
            Item = item
        };

        var response = await dynamoDbClient.PutItemAsync(putRequest);
        Console.WriteLine("Item inserted into DynamoDB.");
    }
}