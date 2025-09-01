// Example: Inserting an item into DynamoDB using AWS SDK for Java v2

import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.PutItemRequest;
import software.amazon.awssdk.services.dynamodb.model.AttributeValue;
import java.util.HashMap;

public class AwsDynamoDbExample {
    public static void main(String[] args) {
        DynamoDbClient dynamoDb = DynamoDbClient.create();

        HashMap<String, AttributeValue> itemValues = new HashMap<>();
        itemValues.put("Id", AttributeValue.builder().s("101").build());
        itemValues.put("Name", AttributeValue.builder().s("Sample Item").build());

        PutItemRequest request = PutItemRequest.builder()
                .tableName("YourTableName") // Replace with your table name
                .item(itemValues)
                .build();

        dynamoDb.putItem(request);

        System.out.println("Item inserted into DynamoDB.");

        dynamoDb.close();
    }
}