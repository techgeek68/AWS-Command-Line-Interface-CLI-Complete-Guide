# AWS CLI – CloudFormation Guide

## Table of Contents
1. [Overview](#overview)
2. [Deploying Stacks](#1-deploying-stacks)
3. [Packaging](#2-packaging-for-local-artifacts)
4. [Change Sets](#3-change-sets)
5. [Stack Outputs & Resources](#4-stack-outputs--resources)
6. [Deleting Stacks](#5-deleting-stacks)
7. [Drift Detection](#6-drift-detection)
8. [Stack Sets](#7-stack-sets)
9. [Best Practices](#8-best-practices)
10. [Troubleshooting](#9-troubleshooting)

---

## Overview
AWS CloudFormation provisions infrastructure as code using declarative templates in YAML or JSON format. The CLI supports packaging local artifacts, deploying stacks, managing change sets for safe updates, stack introspection, and drift detection. This guide covers essential CloudFormation operations for infrastructure automation.

---

## 1. Deploying Stacks

### Basic Stack Deployment
````bash
aws cloudformation deploy \
  --template-file xxxxxxxx \  # user input here (template file path, e.g., template.yaml)
  --stack-name xxxxxxxx \  # user input here (stack name)
  --capabilities CAPABILITY_IAM
````

### Deploy with Parameters
````bash
aws cloudformation deploy \
  --template-file xxxxxxxx \  # user input here (template file path)
  --stack-name xxxxxxxx \  # user input here (stack name)
  --parameter-overrides xxxxxxxx=xxxxxxxx xxxxxxxx=xxxxxxxx \  # user input here (parameter key-value pairs)
  --capabilities CAPABILITY_NAMED_IAM
````

### Deploy with Tags
````bash
aws cloudformation deploy \
  --template-file xxxxxxxx \  # user input here (template file path)
  --stack-name xxxxxxxx \  # user input here (stack name)
  --tags xxxxxxxx=xxxxxxxx xxxxxxxx=xxxxxxxx  # user input here (tag key-value pairs)
````

### Create Stack (Alternative Method)
````bash
aws cloudformation create-stack \
  --stack-name xxxxxxxx \  # user input here (stack name)
  --template-body file://xxxxxxxx \  # user input here (template file path)
  --parameters ParameterKey=xxxxxxxx,ParameterValue=xxxxxxxx  # user input here (parameter details)
````

### Update Stack
````bash
aws cloudformation update-stack \
  --stack-name xxxxxxxx \  # user input here (stack name)
  --template-body file://xxxxxxxx \  # user input here (updated template file path)
  --parameters ParameterKey=xxxxxxxx,ParameterValue=xxxxxxxx  # user input here (parameter details)
````

### PowerShell Example
````powershell
aws.exe cloudformation deploy --template-file xxxxxxxx --stack-name xxxxxxxx --capabilities CAPABILITY_IAM  # user input here (template file, stack name)
````

### Wait for Stack Operations
````bash
aws cloudformation wait stack-create-complete --stack-name xxxxxxxx  # user input here (stack name)
aws cloudformation wait stack-update-complete --stack-name xxxxxxxx  # user input here (stack name)
aws cloudformation wait stack-delete-complete --stack-name xxxxxxxx  # user input here (stack name)
````

---

## 2. Packaging (For Local Artifacts)

### Package Template with S3 Artifacts
````bash
aws cloudformation package \
  --template-file xxxxxxxx \  # user input here (template file with local references)
  --s3-bucket xxxxxxxx \  # user input here (S3 bucket for artifacts)
  --output-template-file xxxxxxxx  # user input here (output template file name)
````

### Package with S3 Prefix
````bash
aws cloudformation package \
  --template-file xxxxxxxx \  # user input here (template file)
  --s3-bucket xxxxxxxx \  # user input here (S3 bucket name)
  --s3-prefix xxxxxxxx \  # user input here (S3 prefix for organization)
  --output-template-file xxxxxxxx  # user input here (output template file)
````

### Deploy Packaged Template
````bash
aws cloudformation deploy \
  --template-file xxxxxxxx \  # user input here (packaged template file)
  --stack-name xxxxxxxx \  # user input here (stack name)
  --capabilities CAPABILITY_IAM
````

### Package and Deploy in One Command
````bash
aws cloudformation package \
  --template-file xxxxxxxx \  # user input here (template file)
  --s3-bucket xxxxxxxx \  # user input here (S3 bucket)
  --output-template-file packaged.yaml && \
aws cloudformation deploy \
  --template-file packaged.yaml \
  --stack-name xxxxxxxx \  # user input here (stack name)
  --capabilities CAPABILITY_IAM
````

---

## 3. Change Sets

### Create Change Set
````bash
aws cloudformation create-change-set \
  --stack-name xxxxxxxx \  # user input here (stack name)
  --change-set-name xxxxxxxx \  # user input here (change set name)
  --template-body file://xxxxxxxx \  # user input here (updated template file)
  --parameters ParameterKey=xxxxxxxx,ParameterValue=xxxxxxxx  # user input here (parameter details)
````

### List Change Sets for Stack
````bash
aws cloudformation list-change-sets --stack-name xxxxxxxx  # user input here (stack name)
````

### Describe Change Set
````bash
aws cloudformation describe-change-set \
  --stack-name xxxxxxxx \  # user input here (stack name)
  --change-set-name xxxxxxxx  # user input here (change set name)
````

### Execute Change Set
````bash
aws cloudformation execute-change-set \
  --stack-name xxxxxxxx \  # user input here (stack name)
  --change-set-name xxxxxxxx  # user input here (change set name)
````

### Delete Change Set
````bash
aws cloudformation delete-change-set \
  --stack-name xxxxxxxx \  # user input here (stack name)
  --change-set-name xxxxxxxx  # user input here (change set name)
````

---

## 4. Stack Outputs & Resources

### List All Stacks
````bash
aws cloudformation list-stacks
````

### List Stacks by Status
````bash
aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE
````

### Describe Stack
````bash
aws cloudformation describe-stacks --stack-name xxxxxxxx  # user input here (stack name)
````

### Get Stack Outputs
````bash
aws cloudformation describe-stacks \
  --stack-name xxxxxxxx \  # user input here (stack name)
  --query 'Stacks[0].Outputs'
````

### Get Specific Output Value
````bash
aws cloudformation describe-stacks \
  --stack-name xxxxxxxx \  # user input here (stack name)
  --query 'Stacks[0].Outputs[?OutputKey==`xxxxxxxx`].OutputValue' \  # user input here (output key name)
  --output text
````

### List Stack Resources
````bash
aws cloudformation list-stack-resources --stack-name xxxxxxxx  # user input here (stack name)
````

### Describe Stack Resource
````bash
aws cloudformation describe-stack-resource \
  --stack-name xxxxxxxx \  # user input here (stack name)
  --logical-resource-id xxxxxxxx  # user input here (logical resource ID from template)
````

### Get Stack Events
````bash
aws cloudformation describe-stack-events --stack-name xxxxxxxx  # user input here (stack name)
````

### Get Recent Stack Events
````bash
aws cloudformation describe-stack-events \
  --stack-name xxxxxxxx \  # user input here (stack name)
  --max-items 20
````

---

## 5. Deleting Stacks

### Delete Stack
````bash
aws cloudformation delete-stack --stack-name xxxxxxxx  # user input here (stack name)
````

### Delete Stack and Wait for Completion
````bash
aws cloudformation delete-stack --stack-name xxxxxxxx && \  # user input here (stack name)
aws cloudformation wait stack-delete-complete --stack-name xxxxxxxx  # user input here (stack name)
````

### Delete Stack with Retain Policy
````bash
aws cloudformation delete-stack \
  --stack-name xxxxxxxx \  # user input here (stack name)
  --retain-resources xxxxxxxx xxxxxxxx  # user input here (logical resource IDs to retain)
````

---

## 6. Drift Detection

### Start Drift Detection
````bash
aws cloudformation detect-stack-drift --stack-name xxxxxxxx  # user input here (stack name)
````

### Check Drift Detection Status
````bash
aws cloudformation describe-stack-drift-detection-status \
  --stack-drift-detection-id xxxxxxxx  # user input here (drift detection ID from previous command)
````

### List Stack Resource Drifts
````bash
aws cloudformation describe-stack-resource-drifts --stack-name xxxxxxxx  # user input here (stack name)
````

### Describe Specific Resource Drift
````bash
aws cloudformation describe-stack-resource-drift \
  --stack-name xxxxxxxx \  # user input here (stack name)
  --logical-resource-id xxxxxxxx  # user input here (logical resource ID)
````

---

## 7. Stack Sets

### Create Stack Set
````bash
aws cloudformation create-stack-set \
  --stack-set-name xxxxxxxx \  # user input here (stack set name)
  --template-body file://xxxxxxxx \  # user input here (template file)
  --capabilities CAPABILITY_IAM
````

### Create Stack Instances
````bash
aws cloudformation create-stack-instances \
  --stack-set-name xxxxxxxx \  # user input here (stack set name)
  --accounts xxxxxxxx xxxxxxxx \  # user input here (account IDs)
  --regions xxxxxxxx xxxxxxxx  # user input here (regions)
````

### List Stack Sets
````bash
aws cloudformation list-stack-sets
````

### List Stack Instances
````bash
aws cloudformation list-stack-instances --stack-set-name xxxxxxxx  # user input here (stack set name)
````

### Update Stack Set
````bash
aws cloudformation update-stack-set \
  --stack-set-name xxxxxxxx \  # user input here (stack set name)
  --template-body file://xxxxxxxx \  # user input here (updated template file)
  --capabilities CAPABILITY_IAM
````

### Delete Stack Instances
````bash
aws cloudformation delete-stack-instances \
  --stack-set-name xxxxxxxx \  # user input here (stack set name)
  --accounts xxxxxxxx \  # user input here (account IDs)
  --regions xxxxxxxx \  # user input here (regions)
  --retain-stacks
````

### Delete Stack Set
````bash
aws cloudformation delete-stack-set --stack-set-name xxxxxxxx  # user input here (stack set name)
````

---

## 8. Best Practices

- **Use change sets for production safety** - always preview changes before applying them
- **Modularize templates** using nested stacks or separate templates for different components
- **Parameterize environment-specific values** instead of hardcoding them in templates
- **Use exports sparingly** to avoid tight coupling between stacks
- **Apply consistent tags** for cost allocation and governance: `--tags Key=Environment,Value=Production`
- **Lint templates** using tools like `cfn-lint` before deployment
- **Use stack policies** to protect critical resources from accidental updates
- **Implement proper IAM permissions** for CloudFormation service roles
- **Version control templates** and maintain deployment procedures
- **Use stack sets** for multi-account and multi-region deployments
- **Monitor stack events** and set up notifications for deployment failures
- **Implement rollback strategies** and test them regularly

---

## 9. Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| **ROLLBACK_COMPLETE state** | Resource creation/update failed | Inspect stack events to identify failed resource |
| **Export name already exists** | Duplicate export across stacks | Rename export or remove conflicting export |
| **InsufficientCapabilities** | Missing IAM capability flag | Add `--capabilities CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM` |
| **Artifact not found** | Package command not run | Re-run `package` command before deploy |
| **Drift detection incomplete** | Detection still running | Poll status until complete before checking results |
| **Template validation error** | Invalid template syntax | Use `cfn-lint` or validate-template command |
| **Parameter validation failed** | Wrong parameter type/value | Check parameter constraints and allowed values |
| **Resource limit exceeded** | Account/region limits reached | Request limit increases or clean up unused resources |
| **Circular dependency** | Resources depend on each other | Restructure template to remove circular references |
| **Stack in UPDATE_ROLLBACK_FAILED** | Rollback failed | Manually fix resources or continue update with skip |

### Debugging Commands

Validate template syntax:
````bash
aws cloudformation validate-template --template-body file://xxxxxxxx  # user input here (template file)
````

Get recent stack events with details:
````bash
aws cloudformation describe-stack-events \
  --stack-name xxxxxxxx \  # user input here (stack name)
  --max-items 20 \
  --query 'StackEvents[?ResourceStatus!=`CREATE_IN_PROGRESS` && ResourceStatus!=`UPDATE_IN_PROGRESS`]'
````

Check stack status:
````bash
aws cloudformation describe-stacks \
  --stack-name xxxxxxxx \  # user input here (stack name)
  --query 'Stacks[0].{Status:StackStatus,Reason:StackStatusReason}'
````

List failed resources:
````bash
aws cloudformation describe-stack-events \
  --stack-name xxxxxxxx \  # user input here (stack name)
  --query 'StackEvents[?contains(ResourceStatus, `FAILED`)]'
````

Get template summary:
````bash
aws cloudformation get-template-summary --template-body file://xxxxxxxx  # user input here (template file)
````

---