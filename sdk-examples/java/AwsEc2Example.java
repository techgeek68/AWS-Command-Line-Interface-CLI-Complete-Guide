// Example: Launching an EC2 instance using AWS SDK for Java v2

import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.*;

public class AwsEc2Example {
    public static void main(String[] args) {
        Ec2Client ec2 = Ec2Client.create();

        RunInstancesRequest runRequest = RunInstancesRequest.builder()
                .imageId("ami-0abcdef1234567890") // Replace with a valid AMI ID
                .instanceType(InstanceType.T2_MICRO)
                .maxCount(1)
                .minCount(1)
                .build();

        RunInstancesResponse response = ec2.runInstances(runRequest);

        // Print the ID of the launched instance
        String instanceId = response.instances().get(0).instanceId();
        System.out.println("Launched EC2 instance with ID: " + instanceId);

        ec2.close();
    }
}