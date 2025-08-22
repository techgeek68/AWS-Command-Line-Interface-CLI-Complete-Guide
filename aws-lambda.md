# AWS CLI – Lambda Guide

## Table of Contents
1. [Overview](#overview)
2. [Creating Functions](#1-creating-functions)
3. [Updating Function Code](#2-updating-function-code)
4. [Invoking Functions](#3-invoking-functions)
5. [Versions & Aliases](#4-versions--aliases)
6. [Environment Variables](#5-environment-variables)
7. [Layers](#6-layers)
8. [Event Sources](#7-event-sources)
9. [Logs & Monitoring](#8-logs--monitoring)
10. [Best Practices](#9-best-practices)
11. [Troubleshooting](#10-troubleshooting)

---

## Overview
AWS Lambda runs code without managing servers, automatically scaling from zero to thousands of concurrent executions. The CLI enables function creation, code updates, configuration management, invocation, and monitoring. For production deployments, Lambda is typically combined with packaging tools like SAM, CDK, or CI/CD pipelines.

---

## 1. Creating Functions

### Create Function from ZIP File
````bash
aws lambda create-function \
  --function-name xxxxxxxx \  # user input here (function name)
  --runtime xxxxxxxx \  # user input here (runtime, e.g., python3.9, nodejs18.x, java11)
  --role arn:aws:iam::xxxxxxxx:role/xxxxxxxx \  # user input here (account ID and execution role name)
  --handler xxxxxxxx \  # user input here (handler, e.g., lambda_function.lambda_handler)
  --zip-file fileb://xxxxxxxx  # user input here (path to ZIP file)
````

### Create Function with Inline Code (Small Functions)
````bash
aws lambda create-function \
  --function-name xxxxxxxx \  # user input here (function name)
  --runtime python3.9 \
  --role arn:aws:iam::xxxxxxxx:role/xxxxxxxx \  # user input here (account ID and role name)
  --handler index.lambda_handler \
  --zip-file fileb://<(echo 'def lambda_handler(event, context): return {"statusCode": 200, "body": "Hello World"}' | zip -q - -) 
````

### Create Function with Environment Variables
````bash
aws lambda create-function \
  --function-name xxxxxxxx \  # user input here (function name)
  --runtime xxxxxxxx \  # user input here (runtime)
  --role arn:aws:iam::xxxxxxxx:role/xxxxxxxx \  # user input here (account ID and role name)
  --handler xxxxxxxx \  # user input here (handler)
  --zip-file fileb://xxxxxxxx \  # user input here (ZIP file path)
  --environment "Variables={xxxxxxxx=xxxxxxxx,xxxxxxxx=xxxxxxxx}"  # user input here (environment variables)
````

### Create Function with VPC Configuration
````bash
aws lambda create-function \
  --function-name xxxxxxxx \  # user input here (function name)
  --runtime xxxxxxxx \  # user input here (runtime)
  --role arn:aws:iam::xxxxxxxx:role/xxxxxxxx \  # user input here (account ID and role name)
  --handler xxxxxxxx \  # user input here (handler)
  --zip-file fileb://xxxxxxxx \  # user input here (ZIP file path)
  --vpc-config SubnetIds=xxxxxxxx,SecurityGroupIds=xxxxxxxx  # user input here (subnet and security group IDs)
````

### List Functions
````bash
aws lambda list-functions
````

### Get Function Details
````bash
aws lambda get-function --function-name xxxxxxxx  # user input here (function name)
````

### Delete Function
````bash
aws lambda delete-function --function-name xxxxxxxx  # user input here (function name)
````

---

## 2. Updating Function Code

### Update Code from ZIP File
````bash
aws lambda update-function-code \
  --function-name xxxxxxxx \  # user input here (function name)
  --zip-file fileb://xxxxxxxx  # user input here (path to updated ZIP file)
````

### Update Code from S3
````bash
aws lambda update-function-code \
  --function-name xxxxxxxx \  # user input here (function name)
  --s3-bucket xxxxxxxx \  # user input here (S3 bucket name)
  --s3-key xxxxxxxx  # user input here (S3 object key)
````

### Update Code from S3 with Version
````bash
aws lambda update-function-code \
  --function-name xxxxxxxx \  # user input here (function name)
  --s3-bucket xxxxxxxx \  # user input here (S3 bucket name)
  --s3-key xxxxxxxx \  # user input here (S3 object key)
  --s3-object-version xxxxxxxx  # user input here (S3 object version)
````

### Update Function Configuration
````bash
aws lambda update-function-configuration \
  --function-name xxxxxxxx \  # user input here (function name)
  --timeout xxxxxxxx \  # user input here (timeout in seconds)
  --memory-size xxxxxxxx \  # user input here (memory in MB)
  --runtime xxxxxxxx  # user input here (runtime version)
````

---

## 3. Invoking Functions

### Synchronous Invocation
````bash
aws lambda invoke \
  --function-name xxxxxxxx \  # user input here (function name)
  --payload '{"xxxxxxxx":"xxxxxxxx"}' \  # user input here (JSON payload)
  response.json
````

### Asynchronous Invocation
````bash
aws lambda invoke \
  --function-name xxxxxxxx \  # user input here (function name)
  --invocation-type Event \
  --payload '{"xxxxxxxx":"xxxxxxxx"}' \  # user input here (JSON payload)
  response.json
````

### Invoke with Log Output
````bash
aws lambda invoke \
  --function-name xxxxxxxx \  # user input here (function name)
  --log-type Tail \
  --payload '{"xxxxxxxx":"xxxxxxxx"}' \  # user input here (JSON payload)
  response.json \
  --query 'LogResult' --output text | base64 --decode
````

### Invoke from File
````bash
aws lambda invoke \
  --function-name xxxxxxxx \  # user input here (function name)
  --payload file://xxxxxxxx \  # user input here (path to JSON file)
  response.json
````

### Dry Run (Validate Parameters)
````bash
aws lambda invoke \
  --function-name xxxxxxxx \  # user input here (function name)
  --invocation-type DryRun \
  --payload '{}' \
  response.json
````

---

## 4. Versions & Aliases

### Publish New Version
````bash
aws lambda publish-version --function-name xxxxxxxx  # user input here (function name)
````

### Publish Version with Description
````bash
aws lambda publish-version \
  --function-name xxxxxxxx \  # user input here (function name)
  --description "xxxxxxxx"  # user input here (version description)
````

### List Function Versions
````bash
aws lambda list-versions-by-function --function-name xxxxxxxx  # user input here (function name)
````

### Create Alias
````bash
aws lambda create-alias \
  --function-name xxxxxxxx \  # user input here (function name)
  --name xxxxxxxx \  # user input here (alias name, e.g., prod, staging)
  --function-version xxxxxxxx  # user input here (version number)
````

### Update Alias
````bash
aws lambda update-alias \
  --function-name xxxxxxxx \  # user input here (function name)
  --name xxxxxxxx \  # user input here (alias name)
  --function-version xxxxxxxx  # user input here (new version number)
````

### List Aliases
````bash
aws lambda list-aliases --function-name xxxxxxxx  # user input here (function name)
````

### Delete Alias
````bash
aws lambda delete-alias \
  --function-name xxxxxxxx \  # user input here (function name)
  --name xxxxxxxx  # user input here (alias name)
````

### Invoke Specific Version
````bash
aws lambda invoke \
  --function-name xxxxxxxx:xxxxxxxx \  # user input here (function name:version or function name:alias)
  --payload '{}' \
  response.json
````

---

## 5. Environment Variables

### Update Environment Variables
````bash
aws lambda update-function-configuration \
  --function-name xxxxxxxx \  # user input here (function name)
  --environment "Variables={xxxxxxxx=xxxxxxxx,xxxxxxxx=xxxxxxxx}"  # user input here (environment variable key-value pairs)
````

### Add Single Environment Variable
````bash
aws lambda update-function-configuration \
  --function-name xxxxxxxx \  # user input here (function name)
  --environment "Variables={$(aws lambda get-function-configuration --function-name xxxxxxxx --query 'Environment.Variables' --output text | sed 's/\t/,/g'),xxxxxxxx=xxxxxxxx}"  # user input here (function name again, new variable)
````

### Remove All Environment Variables
````bash
aws lambda update-function-configuration \
  --function-name xxxxxxxx \  # user input here (function name)
  --environment "Variables={}"
````

### Get Current Environment Variables
````bash
aws lambda get-function-configuration \
  --function-name xxxxxxxx \  # user input here (function name)
  --query 'Environment.Variables'
````

---

## 6. Layers

### Create Layer Version
````bash
aws lambda publish-layer-version \
  --layer-name xxxxxxxx \  # user input here (layer name)
  --description "xxxxxxxx" \  # user input here (layer description)
  --zip-file fileb://xxxxxxxx \  # user input here (path to layer ZIP file)
  --compatible-runtimes xxxxxxxx xxxxxxxx  # user input here (compatible runtimes, e.g., python3.9 nodejs18.x)
````

### List Layers
````bash
aws lambda list-layers
````

### List Layer Versions
````bash
aws lambda list-layer-versions --layer-name xxxxxxxx  # user input here (layer name)
````

### Add Layer to Function
````bash
aws lambda update-function-configuration \
  --function-name xxxxxxxx \  # user input here (function name)
  --layers arn:aws:lambda:xxxxxxxx:xxxxxxxx:layer:xxxxxxxx:xxxxxxxx  # user input here (region, account ID, layer name, version)
````

### Remove Layer from Function
````bash
aws lambda update-function-configuration \
  --function-name xxxxxxxx \  # user input here (function name)
  --layers
````

### Delete Layer Version
````bash
aws lambda delete-layer-version \
  --layer-name xxxxxxxx \  # user input here (layer name)
  --version-number xxxxxxxx  # user input here (version number)
````

---

## 7. Event Sources

### Create Event Source Mapping (SQS)
````bash
aws lambda create-event-source-mapping \
  --function-name xxxxxxxx \  # user input here (function name)
  --event-source-arn arn:aws:sqs:xxxxxxxx:xxxxxxxx:xxxxxxxx \  # user input here (region, account ID, queue name)
  --batch-size xxxxxxxx  # user input here (batch size, e.g., 10)
````

### Create Event Source Mapping (Kinesis)
````bash
aws lambda create-event-source-mapping \
  --function-name xxxxxxxx \  # user input here (function name)
  --event-source-arn arn:aws:kinesis:xxxxxxxx:xxxxxxxx:stream/xxxxxxxx \  # user input here (region, account ID, stream name)
  --starting-position LATEST
````

### List Event Source Mappings
````bash
aws lambda list-event-source-mappings --function-name xxxxxxxx  # user input here (function name)
````

### Update Event Source Mapping
````bash
aws lambda update-event-source-mapping \
  --uuid xxxxxxxx \  # user input here (event source mapping UUID)
  --batch-size xxxxxxxx  # user input here (new batch size)
````

### Delete Event Source Mapping
````bash
aws lambda delete-event-source-mapping --uuid xxxxxxxx  # user input here (event source mapping UUID)
````

### Add S3 Event Notification
````bash
aws s3api put-bucket-notification-configuration \
  --bucket xxxxxxxx \  # user input here (bucket name)
  --notification-configuration file://xxxxxxxx  # user input here (path to notification config JSON)
````

---

## 8. Logs & Monitoring

### Tail Function Logs
````bash
aws logs tail /aws/lambda/xxxxxxxx --since 5m  # user input here (function name)
````

### Get Function Metrics
````bash
aws cloudwatch get-metric-statistics \
  --namespace AWS/Lambda \
  --metric-name Invocations \
  --dimensions Name=FunctionName,Value=xxxxxxxx \  # user input here (function name)
  --statistics Sum \
  --start-time 2025-01-01T00:00:00Z \
  --end-time 2025-01-02T00:00:00Z \
  --period 3600
````

### Get Error Rate
````bash
aws cloudwatch get-metric-statistics \
  --namespace AWS/Lambda \
  --metric-name Errors \
  --dimensions Name=FunctionName,Value=xxxxxxxx \  # user input here (function name)
  --statistics Sum \
  --start-time 2025-01-01T00:00:00Z \
  --end-time 2025-01-02T00:00:00Z \
  --period 3600
````

### Get Duration Metrics
````bash
aws cloudwatch get-metric-statistics \
  --namespace AWS/Lambda \
  --metric-name Duration \
  --dimensions Name=FunctionName,Value=xxxxxxxx \  # user input here (function name)
  --statistics Average,Maximum \
  --start-time 2025-01-01T00:00:00Z \
  --end-time 2025-01-02T00:00:00Z \
  --period 3600
````

---

## 9. Best Practices

- **Use least privilege execution roles** with only required permissions
- **Leverage layers** for shared dependencies and reduce deployment package size
- **Externalize configuration** via environment variables, Parameter Store, or Secrets Manager
- **Use versions and aliases** for safe deployments and traffic shifting
- **Monitor concurrency** and set reserved concurrency where needed to prevent throttling
- **Implement structured logging** (JSON format) for better observability
- **Optimize cold start performance** by minimizing initialization code and dependencies
- **Use appropriate memory allocation** based on CPU and memory requirements
- **Implement proper error handling** and retry logic for resilient applications
- **Enable X-Ray tracing** for distributed tracing in complex applications
- **Use dead letter queues** for failed asynchronous invocations
- **Keep functions small and focused** following single responsibility principle

---

## 10. Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| **Function times out** | Insufficient timeout setting | Increase timeout in function configuration |
| **Out of memory errors** | Insufficient memory allocation | Increase memory size (also increases CPU) |
| **Cold start latency** | Function initialization overhead | Optimize initialization, use provisioned concurrency |
| **Permission denied** | Missing IAM permissions | Update execution role with required permissions |
| **Package too large** | Deployment package exceeds limits | Use layers, optimize dependencies, or use container images |
| **VPC timeout** | No internet access in VPC | Add NAT Gateway or VPC endpoints |
| **Concurrent execution limit** | Account or function limit reached | Request limit increase or use reserved concurrency |
| **Dead letter queue not working** | Missing permissions or configuration | Check IAM permissions and DLQ configuration |
| **Environment variables not accessible** | Incorrect variable names | Verify environment variable names and values |
| **Layer not found** | Incorrect layer ARN or version | Verify layer ARN, version, and region compatibility |

### Debugging Commands

Check function configuration:
````bash
aws lambda get-function-configuration --function-name xxxxxxxx  # user input here (function name)
````

Get function policy:
````bash
aws lambda get-policy --function-name xxxxxxxx  # user input here (function name)
````

List function event source mappings:
````bash
aws lambda list-event-source-mappings --function-name xxxxxxxx  # user input here (function name)
````

Get account settings:
````bash
aws lambda get-account-settings
````

Test function with specific event:
````bash
aws lambda invoke \
  --function-name xxxxxxxx \  # user input here (function name)
  --payload file://test-event.json \
  --log-type Tail \
  response.json && cat response.json
````

---