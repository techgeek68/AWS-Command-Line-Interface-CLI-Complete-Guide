// Example: Put an item into a DynamoDB table using AWS SDK v3 for Node.js

const { DynamoDBClient, PutItemCommand } = require("@aws-sdk/client-dynamodb");

// Create a DynamoDB client
const ddbClient = new DynamoDBClient({ region: "us-east-1" });

async function putItemToDynamoDB(tableName, item) {
  try {
    // Item attributes should be in DynamoDB attribute value format
    const params = {
      TableName: tableName,
      Item: item,
    };

    // Put the item into the table
    await ddbClient.send(new PutItemCommand(params));
    console.log("Item inserted successfully.");
  } catch (err) {
    console.error("Error inserting item into DynamoDB:", err);
  }
}

// Usage example:
// putItemToDynamoDB("MyTable", {
//   id: { S: "123" },
//   name: { S: "John Doe" },
//   age: { N: "30" },
// });