// Example: Uploading a file to S3 using AWS SDK for Java v2

import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;
import java.nio.file.Paths;

public class AwsS3Example {
    public static void main(String[] args) {
        S3Client s3 = S3Client.create();

        PutObjectRequest putRequest = PutObjectRequest.builder()
                .bucket("your-bucket-name") // Replace with your bucket name
                .key("example.txt")
                .build();

        // Upload the file located at /path/to/example.txt
        s3.putObject(putRequest, Paths.get("/path/to/example.txt"));

        System.out.println("File uploaded to S3.");

        s3.close();
    }
}