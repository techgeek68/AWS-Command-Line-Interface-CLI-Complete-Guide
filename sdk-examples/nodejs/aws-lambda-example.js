// Example: Invoke a Lambda function using AWS SDK v3 for Node.js

const { LambdaClient, InvokeCommand } = require("@aws-sdk/client-lambda");

// Create a Lambda client
const lambdaClient = new LambdaClient({ region: "us-east-1" });

async function invokeLambda(functionName, payload) {
  try {
    // Prepare the invoke command
    const params = {
      FunctionName: functionName,
      Payload: Buffer.from(JSON.stringify(payload)),
    };

    // Invoke the Lambda function
    const data = await lambdaClient.send(new InvokeCommand(params));
    // Lambda returns the response payload as a Buffer
    const responsePayload = Buffer.from(data.Payload).toString();
    console.log("Lambda response:", responsePayload);
  } catch (err) {
    console.error("Error invoking Lambda function:", err);
  }
}

// Usage example:
// invokeLambda("MyLambdaFunction", { key1: "value1" });