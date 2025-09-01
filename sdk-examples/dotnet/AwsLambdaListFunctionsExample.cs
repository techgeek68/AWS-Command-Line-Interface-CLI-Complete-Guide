// Example: Listing Lambda functions using AWS SDK for .NET

using Amazon.Lambda;
using Amazon.Lambda.Model;
using System;
using System.Threading.Tasks;

class AwsLambdaListFunctionsExample
{
    static async Task Main()
    {
        var lambdaClient = new AmazonLambdaClient();
        var listRequest = new ListFunctionsRequest();
        var listResponse = await lambdaClient.ListFunctionsAsync(listRequest);

        foreach (var function in listResponse.Functions)
        {
            Console.WriteLine($"Function Name: {function.FunctionName}, Runtime: {function.Runtime}");
        }
    }
}