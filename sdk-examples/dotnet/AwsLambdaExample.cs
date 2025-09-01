// Example: Invoking a Lambda function using AWS SDK for .NET

using Amazon.Lambda;
using Amazon.Lambda.Model;
using System;
using System.Text;
using System.Threading.Tasks;

class AwsLambdaExample
{
    static async Task Main()
    {
        var lambdaClient = new AmazonLambdaClient();

        var invokeRequest = new InvokeRequest
        {
            FunctionName = "your-lambda-function-name", // Replace with your Lambda function name
            Payload = "{\"key\":\"value\"}" // JSON payload
        };

        var response = await lambdaClient.InvokeAsync(invokeRequest);

        string responsePayload = Encoding.UTF8.GetString(response.Payload.ToArray());
        Console.WriteLine("Lambda response: " + responsePayload);
    }
}