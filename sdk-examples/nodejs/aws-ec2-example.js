// Example: List all EC2 instances in a region using AWS SDK v3 for Node.js

const { EC2Client, DescribeInstancesCommand } = require("@aws-sdk/client-ec2");

// Create an EC2 client
const ec2Client = new EC2Client({ region: "us-east-1" });

async function listEC2Instances() {
  try {
    // DescribeInstancesCommand fetches details about EC2 instances
    const data = await ec2Client.send(new DescribeInstancesCommand({}));
    const instances = [];
    // Traverse through reservations and instances
    data.Reservations.forEach((reservation) => {
      reservation.Instances.forEach((instance) => {
        instances.push({
          InstanceId: instance.InstanceId,
          State: instance.State.Name,
          Type: instance.InstanceType,
        });
      });
    });
    console.log("EC2 Instances:", instances);
  } catch (err) {
    console.error("Error listing EC2 instances:", err);
  }
}

listEC2Instances();