# AWS CLI – S3 Guide

## Table of Contents
1. [Overview](#overview)
2. [Buckets](#1-buckets)
3. [Object Operations](#2-object-operations)
4. [Synchronization](#3-synchronization)
5. [Versioning & Encryption](#4-versioning--encryption)
6. [Presigned URLs](#5-presigned-urls)
7. [Cross-Platform Notes](#6-cross-platform-notes)
8. [Best Practices](#7-best-practices)
9. [Troubleshooting](#8-troubleshooting)

---

## Overview
Amazon S3 provides scalable object storage for unstructured data. The AWS CLI enables efficient management of buckets and objects, including listing, uploading, downloading, synchronization, metadata management, and presigned URLs for temporary access. This guide covers the most common S3 operations and best practices.

---

## 1. Buckets

### List All Buckets
````bash
aws s3 ls
````

### Create Bucket (US East 1)
````bash
aws s3 mb s3://xxxxxxxx  # user input here (unique bucket name)
````

### Create Bucket in Specific Region
````bash
aws s3api create-bucket \
  --bucket xxxxxxxx \  # user input here (unique bucket name)
  --region xxxxxxxx \  # user input here (region, e.g., us-west-2)
  --create-bucket-configuration LocationConstraint=xxxxxxxx  # user input here (same region)
````

### List Objects in Bucket
````bash
aws s3 ls s3://xxxxxxxx/  # user input here (bucket name)
````

### List Objects with Details
````bash
aws s3 ls s3://xxxxxxxx/ --human-readable --summarize  # user input here (bucket name)
````

### List Objects Recursively
````bash
aws s3 ls s3://xxxxxxxx/ --recursive  # user input here (bucket name)
````

### Delete Empty Bucket
````bash
aws s3 rb s3://xxxxxxxx  # user input here (bucket name)
````

### Delete Bucket and All Contents (Force)
````bash
aws s3 rb s3://xxxxxxxx --force  # user input here (bucket name)
````

---

## 2. Object Operations

### Upload File
````bash
aws s3 cp xxxxxxxx s3://xxxxxxxx/xxxxxxxx  # user input here (local file path, bucket name, object key)
````

### Upload with Storage Class
````bash
aws s3 cp xxxxxxxx s3://xxxxxxxx/xxxxxxxx --storage-class xxxxxxxx  # user input here (local file, bucket, object key, storage class like STANDARD_IA)
````

### Download File
````bash
aws s3 cp s3://xxxxxxxx/xxxxxxxx xxxxxxxx  # user input here (bucket name, object key, local file path)
````

### Copy Between Buckets
````bash
aws s3 cp s3://xxxxxxxx/xxxxxxxx s3://xxxxxxxx/xxxxxxxx  # user input here (source bucket/key, destination bucket/key)
````

### Move File (Rename/Relocate)
````bash
aws s3 mv s3://xxxxxxxx/xxxxxxxx s3://xxxxxxxx/xxxxxxxx  # user input here (source bucket/key, destination bucket/key)
````

### Delete Object
````bash
aws s3 rm s3://xxxxxxxx/xxxxxxxx  # user input here (bucket name, object key)
````

### Delete Multiple Objects (Prefix)
````bash
aws s3 rm s3://xxxxxxxx/xxxxxxxx --recursive  # user input here (bucket name, prefix path)
````

### Set Object Metadata
````bash
aws s3api put-object \
  --bucket xxxxxxxx \  # user input here (bucket name)
  --key xxxxxxxx \  # user input here (object key)
  --metadata "xxxxxxxx=xxxxxxxx,xxxxxxxx=xxxxxxxx" \  # user input here (metadata key-value pairs)
  --body xxxxxxxx  # user input here (local file path)
````

### Get Object Metadata
````bash
aws s3api head-object --bucket xxxxxxxx --key xxxxxxxx  # user input here (bucket name, object key)
````

---

## 3. Synchronization

### Sync Local Directory to S3
````bash
aws s3 sync xxxxxxxx/ s3://xxxxxxxx/xxxxxxxx  # user input here (local directory path, bucket name, prefix)
````

### Sync S3 to Local Directory
````bash
aws s3 sync s3://xxxxxxxx/xxxxxxxx xxxxxxxx/  # user input here (bucket name, prefix, local directory path)
````

### Sync with Delete (Mirror)
````bash
aws s3 sync xxxxxxxx/ s3://xxxxxxxx/xxxxxxxx --delete  # user input here (local directory, bucket, prefix)
````

### Sync with Exclusions
````bash
aws s3 sync xxxxxxxx/ s3://xxxxxxxx/xxxxxxxx --exclude "xxxxxxxx"  # user input here (local directory, bucket, prefix, pattern to exclude)
````

### Sync Only Specific File Types
````bash
aws s3 sync xxxxxxxx/ s3://xxxxxxxx/xxxxxxxx --exclude "*" --include "xxxxxxxx"  # user input here (local directory, bucket, prefix, pattern to include)
````

### Dry Run Sync (Preview Changes)
````bash
aws s3 sync xxxxxxxx/ s3://xxxxxxxx/xxxxxxxx --dryrun  # user input here (local directory, bucket, prefix)
````

---

## 4. Versioning & Encryption

### Enable Versioning
````bash
aws s3api put-bucket-versioning \
  --bucket xxxxxxxx \  # user input here (bucket name)
  --versioning-configuration Status=Enabled
````

### Check Versioning Status
````bash
aws s3api get-bucket-versioning --bucket xxxxxxxx  # user input here (bucket name)
````

### List Object Versions
````bash
aws s3api list-object-versions --bucket xxxxxxxx  # user input here (bucket name)
````

### Enable Default Encryption (SSE-S3)
````bash
aws s3api put-bucket-encryption \
  --bucket xxxxxxxx \  # user input here (bucket name)
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "AES256"
      }
    }]
  }'
````

### Enable Default Encryption (SSE-KMS)
````bash
aws s3api put-bucket-encryption \
  --bucket xxxxxxxx \  # user input here (bucket name)
  --server-side-encryption-configuration '{
    "Rules": [{
      "ApplyServerSideEncryptionByDefault": {
        "SSEAlgorithm": "aws:kms",
        "KMSMasterKeyID": "xxxxxxxx"
      }
    }]
  }'  # user input here (KMS key ID)
````

### Upload with Server-Side Encryption
````bash
aws s3 cp xxxxxxxx s3://xxxxxxxx/xxxxxxxx --sse AES256  # user input here (local file, bucket, object key)
````

### Upload with KMS Encryption
````bash
aws s3 cp xxxxxxxx s3://xxxxxxxx/xxxxxxxx --sse aws:kms --sse-kms-key-id xxxxxxxx  # user input here (local file, bucket, object key, KMS key ID)
````

---

## 5. Presigned URLs

### Generate Presigned URL for Download (1 hour)
````bash
aws s3 presign s3://xxxxxxxx/xxxxxxxx --expires-in 3600  # user input here (bucket name, object key)
````

### Generate Presigned URL for Upload
````bash
aws s3 presign s3://xxxxxxxx/xxxxxxxx --expires-in 3600 --http-method PUT  # user input here (bucket name, object key)
````

### Generate Presigned URL with Custom Expiration
````bash
aws s3 presign s3://xxxxxxxx/xxxxxxxx --expires-in xxxxxxxx  # user input here (bucket name, object key, seconds)
````

---

## 6. Cross-Platform Notes

### PowerShell Examples
````powershell
aws.exe s3 ls
aws.exe s3 sync xxxxxxxx s3://xxxxxxxx/  # user input here (local path, bucket name)
aws.exe s3 cp xxxxxxxx s3://xxxxxxxx/xxxxxxxx  # user input here (local file, bucket, object key)
````

### Windows Command Prompt
````bat
aws s3 ls
aws s3 sync "xxxxxxxx" s3://xxxxxxxx/  # user input here (local path with quotes if spaces, bucket name)
aws s3 cp "xxxxxxxx" s3://xxxxxxxx/xxxxxxxx  # user input here (local file with quotes, bucket, object key)
````

### Handling Special Characters in Paths
Linux/macOS:
````bash
aws s3 cp "xxxxxxxx" s3://xxxxxxxx/xxxxxxxx  # user input here (file with spaces or special chars, bucket, object key)
````

Windows PowerShell:
````powershell
aws.exe s3 cp "xxxxxxxx" s3://xxxxxxxx/xxxxxxxx  # user input here (file path with quotes, bucket, object key)
````

---

## 7. Best Practices

- **Use unique, DNS-compliant bucket names** - follow naming conventions and avoid periods in bucket names
- **Enable versioning** for important data and set up lifecycle policies for cost optimization
- **Enforce encryption** using default bucket encryption + bucket policies
- **Block public access** unless specifically required; review bucket policies regularly
- **Use appropriate storage classes** for cost optimization (Standard, Standard-IA, Glacier, etc.)
- **Apply object tags** for cost allocation, lifecycle management, and governance
- **Implement lifecycle policies** to transition objects to cheaper storage classes and delete expired data
- **Use multipart uploads** for large files (>100MB) for better performance and reliability
- **Monitor data transfer costs** and optimize by using CloudFront for frequently accessed content
- **Set up CloudTrail logging** for audit trails of S3 API calls
- **Use IAM roles and policies** for fine-grained access control instead of bucket ACLs
- **Avoid blind recursive deletions** in production; use `--dryrun` first

---

## 8. Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| **Bucket name already exists** | Global namespace conflict | Choose a different unique bucket name |
| **Access Denied on bucket operations** | Missing IAM permissions or bucket policy | Verify IAM permissions and bucket policies |
| **SSL certificate errors** | HTTPS required or wrong region | Ensure HTTPS and correct region in endpoint |
| **Slow upload/download speeds** | Network or multipart config | Use multipart upload for large files; check network |
| **403 Forbidden on public bucket** | Bucket policy blocks access | Review and update bucket policy; check Block Public Access settings |
| **Objects not found after sync** | Wrong prefix or case sensitivity | Verify exact path and key names; S3 is case-sensitive |
| **Lifecycle policy not working** | Incorrect rule configuration | Check rule syntax, prefixes, and tags in lifecycle policy |
| **High storage costs** | Wrong storage class or lack of lifecycle | Implement lifecycle policies; use storage class analysis |
| **Versioning consuming space** | Too many versions retained | Set up version lifecycle policies to delete old versions |
| **Cross-region replication failing** | Missing permissions or wrong config | Verify IAM role, bucket policies, and replication rules |

### Debugging Commands

Check bucket policy:
````bash
aws s3api get-bucket-policy --bucket xxxxxxxx  # user input here (bucket name)
````

Check bucket location:
````bash
aws s3api get-bucket-location --bucket xxxxxxxx  # user input here (bucket name)
````

Check bucket encryption:
````bash
aws s3api get-bucket-encryption --bucket xxxxxxxx  # user input here (bucket name)
````

List incomplete multipart uploads:
````bash
aws s3api list-multipart-uploads --bucket xxxxxxxx  # user input here (bucket name)
````

Get bucket size and object count:
````bash
aws cloudwatch get-metric-statistics \
  --namespace AWS/S3 \
  --metric-name BucketSizeBytes \
  --dimensions Name=BucketName,Value=xxxxxxxx Name=StorageType,Value=StandardStorage \  # user input here (bucket name)
  --statistics Average \
  --start-time 2025-01-01T00:00:00Z \
  --end-time 2025-01-02T00:00:00Z \
  --period 86400
````

---