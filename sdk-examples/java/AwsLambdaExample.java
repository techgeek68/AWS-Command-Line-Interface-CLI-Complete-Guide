// Example: Invoking a Lambda function using AWS SDK for Java v2

import software.amazon.awssdk.services.lambda.LambdaClient;
import software.amazon.awssdk.services.lambda.model.InvokeRequest;
import software.amazon.awssdk.core.SdkBytes;

public class AwsLambdaExample {
    public static void main(String[] args) {
        LambdaClient lambda = LambdaClient.create();

        InvokeRequest invokeRequest = InvokeRequest.builder()
                .functionName("your-lambda-function-name") // Replace with your Lambda function name
                .payload(SdkBytes.fromUtf8String("{\"key\":\"value\"}")) // JSON payload
                .build();

        // Invoke the Lambda function
        var result = lambda.invoke(invokeRequest);

        String responsePayload = result.payload().asUtf8String();
        System.out.println("Lambda response: " + responsePayload);

        lambda.close();
    }
}