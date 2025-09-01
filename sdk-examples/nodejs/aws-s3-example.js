// Example: Upload a file to an S3 bucket using AWS SDK v3 for Node.js

const { S3Client, PutObjectCommand } = require("@aws-sdk/client-s3");
const fs = require("fs");

// Create an S3 client
const s3Client = new S3Client({ region: "us-east-1" });

async function uploadFileToS3(bucketName, key, filePath) {
  try {
    const fileStream = fs.createReadStream(filePath);

    // Prepare the upload command
    const uploadParams = {
      Bucket: bucketName,
      Key: key,
      Body: fileStream,
    };

    // Upload the file
    const data = await s3Client.send(new PutObjectCommand(uploadParams));
    console.log(`File uploaded successfully. ETag: ${data.ETag}`);
  } catch (err) {
    console.error("Error uploading file to S3:", err);
  }
}

// Usage: uploadFileToS3("my-bucket", "folder/myfile.txt", "./localfile.txt");