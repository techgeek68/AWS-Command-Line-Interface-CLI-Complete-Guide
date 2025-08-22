# AWS CLI – EC2 Guide

## Table of Contents
1. [Overview](#overview)
2. [Key Pairs](#1-key-pairs)
3. [Security Groups](#2-security-groups)
4. [Instance Lifecycle](#3-instance-lifecycle)
5. [Describe Common Resources](#4-describe-common-resources)
6. [SSH Access](#5-ssh-access)
7. [Best Practices](#6-best-practices)
8. [Troubleshooting](#7-troubleshooting)

---

## Overview
Amazon EC2 provides virtual server instances in the cloud. The AWS CLI enables automation for complete instance lifecycle management, key pairs, security groups, networking, and metadata queries. This guide covers the most frequently used foundational operations for managing EC2 resources efficiently.

---

## 1. Key Pairs

### Create and Save Key Pair (Linux/macOS)
````bash
aws ec2 create-key-pair \
  --key-name xxxxxxxx \  # user input here (key pair name)
  --key-type rsa \
  --key-format pem \
  --query 'KeyMaterial' \
  --output text > xxxxxxxx.pem && chmod 400 xxxxxxxx.pem  # user input here (key pair name for file)
````

### Windows (Command Prompt)
````bat
aws ec2 create-key-pair --key-name xxxxxxxx --key-type rsa --key-format pem --query "KeyMaterial" --output text > xxxxxxxx.pem
icacls xxxxxxxx.pem /inheritance:r /grant:r %USERNAME%:R
````

### Windows (PowerShell)
````powershell
aws.exe ec2 create-key-pair --key-name xxxxxxxx --key-type rsa --key-format pem --query "KeyMaterial" --output text > xxxxxxxx.pem  # user input here (key pair name)
icacls xxxxxxxx.pem /inheritance:r /grant:r "$($env:USERNAME):(R)"
````

### List Key Pairs
````bash
aws ec2 describe-key-pairs
````

### Delete Key Pair
````bash
aws ec2 delete-key-pair --key-name xxxxxxxx  # user input here (key pair name)
````

---

## 2. Security Groups

### Create Security Group
````bash
aws ec2 create-security-group \
  --group-name xxxxxxxx \  # user input here (security group name)
  --description "xxxxxxxx" \  # user input here (security group description)
  --vpc-id xxxxxxxx  # user input here (VPC ID)
````

### Add Ingress Rules
SSH access (port 22):
````bash
aws ec2 authorize-security-group-ingress \
  --group-id xxxxxxxx \  # user input here (security group ID)
  --protocol tcp \
  --port 22 \
  --cidr xxxxxxxx/xx  # user input here (CIDR block, e.g., 203.0.113.0/24)
````

HTTP access (port 80):
````bash
aws ec2 authorize-security-group-ingress \
  --group-id xxxxxxxx \  # user input here (security group ID)
  --protocol tcp \
  --port 80 \
  --cidr 0.0.0.0/0
````

HTTPS access (port 443):
````bash
aws ec2 authorize-security-group-ingress \
  --group-id xxxxxxxx \  # user input here (security group ID)
  --protocol tcp \
  --port 443 \
  --cidr 0.0.0.0/0
````

### Remove Ingress Rules
````bash
aws ec2 revoke-security-group-ingress \
  --group-id xxxxxxxx \  # user input here (security group ID)
  --protocol tcp \
  --port 22 \
  --cidr xxxxxxxx/xx  # user input here (CIDR block to revoke)
````

### List Security Groups
````bash
aws ec2 describe-security-groups
````

### Delete Security Group
````bash
aws ec2 delete-security-group --group-id xxxxxxxx  # user input here (security group ID)
````

---

## 3. Instance Lifecycle

### List All Instances
````bash
aws ec2 describe-instances
````

### List Running Instances (IDs only)
````bash
aws ec2 describe-instances \
  --filters Name=instance-state-name,Values=running \
  --query "Reservations[].Instances[].InstanceId" \
  --output text
````

### Launch New Instance (Basic)
````bash
aws ec2 run-instances \
  --image-id xxxxxxxx \  # user input here (AMI ID, e.g., ami-0abcdef1234567890)
  --count 1 \
  --instance-type xxxxxxxx \  # user input here (instance type, e.g., t3.micro)
  --key-name xxxxxxxx \  # user input here (key pair name)
  --security-group-ids xxxxxxxx \  # user input here (security group ID)
  --subnet-id xxxxxxxx  # user input here (subnet ID)
````

### Launch Instance with User Data
````bash
aws ec2 run-instances \
  --image-id xxxxxxxx \  # user input here (AMI ID)
  --count 1 \
  --instance-type xxxxxxxx \  # user input here (instance type)
  --key-name xxxxxxxx \  # user input here (key pair name)
  --security-group-ids xxxxxxxx \  # user input here (security group ID)
  --subnet-id xxxxxxxx \  # user input here (subnet ID)
  --user-data file://xxxxxxxx  # user input here (path to user data script)
````

### Launch Instance with Tags
````bash
aws ec2 run-instances \
  --image-id xxxxxxxx \  # user input here (AMI ID)
  --count 1 \
  --instance-type xxxxxxxx \  # user input here (instance type)
  --key-name xxxxxxxx \  # user input here (key pair name)
  --security-group-ids xxxxxxxx \  # user input here (security group ID)
  --subnet-id xxxxxxxx \  # user input here (subnet ID)
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=xxxxxxxx},{Key=Environment,Value=xxxxxxxx}]'  # user input here (tag values)
````

### Start Instances
````bash
aws ec2 start-instances --instance-ids xxxxxxxx  # user input here (instance ID)
````

### Stop Instances
````bash
aws ec2 stop-instances --instance-ids xxxxxxxx  # user input here (instance ID)
````

### Reboot Instances
````bash
aws ec2 reboot-instances --instance-ids xxxxxxxx  # user input here (instance ID)
````

### Terminate Instances
````bash
aws ec2 terminate-instances --instance-ids xxxxxxxx  # user input here (instance ID)
````

---

## 4. Describe Common Resources

### List Available AMIs (Amazon Linux 2)
````bash
aws ec2 describe-images \
  --owners amazon \
  --filters "Name=name,Values=amzn2-ami-hvm-*" \
  --query "Images[*].[ImageId,Name,CreationDate]" \
  --output table
````

### Find Latest Amazon Linux 2 AMI
````bash
aws ec2 describe-images \
  --owners amazon \
  --filters "Name=name,Values=amzn2-ami-hvm-*" "Name=state,Values=available" \
  --query "Images | sort_by(@, &CreationDate) | [-1].ImageId" \
  --output text
````

### List Availability Zones
````bash
aws ec2 describe-availability-zones --output table
````

### List VPCs
````bash
aws ec2 describe-vpcs --output table
````

### List Subnets
````bash
aws ec2 describe-subnets --output table
````

### List Instance Types in Region
````bash
aws ec2 describe-instance-types \
  --query "InstanceTypes[?InstanceType=='t3.micro' || InstanceType=='t3.small' || InstanceType=='t3.medium']" \
  --output table
````

### Get Instance Metadata (from within instance)
````bash
curl http://169.254.169.254/latest/meta-data/instance-id
curl http://169.254.169.254/latest/meta-data/public-hostname
curl http://169.254.169.254/latest/meta-data/security-groups
````

---

## 5. SSH Access

### Connect to Instance (Linux/macOS)
````bash
ssh -i xxxxxxxx.pem ec2-user@xxxxxxxx  # user input here (key file name and public IP/hostname)
````

### Connect to Ubuntu Instance
````bash
ssh -i xxxxxxxx.pem ubuntu@xxxxxxxx  # user input here (key file name and public IP/hostname)
````

### Connect via Systems Manager Session Manager
````bash
aws ssm start-session --target xxxxxxxx  # user input here (instance ID)
````

### Copy Files to Instance (SCP)
````bash
scp -i xxxxxxxx.pem xxxxxxxx ec2-user@xxxxxxxx:/home/ec2-user/  # user input here (key file, local file, and instance details)
````

### Copy Files from Instance
````bash
scp -i xxxxxxxx.pem ec2-user@xxxxxxxx:/path/to/file xxxxxxxx  # user input here (key file, instance details, remote file, local destination)
````

### Windows SSH (Command Prompt)
````bat
ssh -i xxxxxxxx.pem ec2-user@xxxxxxxx  # user input here (key file name and public IP/hostname)
````

### Windows SSH (PowerShell)
````powershell
ssh -i xxxxxxxx.pem ec2-user@xxxxxxxx  # user input here (key file name and public IP/hostname)
````

---

## 6. Best Practices

- **Restrict SSH access** (port 22) to known IP addresses; avoid `0.0.0.0/0` in production
- **Use Systems Manager Session Manager** instead of direct SSH access where possible for enhanced security
- **Apply descriptive tags** to instances for cost allocation and management: `--tag-specifications`
- **Use IAM roles for EC2** (Instance Profiles) instead of embedding credentials in instances
- **Regularly clean up** unused security groups, Elastic IPs, and stopped instances to reduce costs
- **Enable termination protection** for production instances
- **Use placement groups** for high-performance computing workloads
- **Monitor instance health** with CloudWatch and set up alarms for critical metrics
- **Implement proper backup strategies** using snapshots or AMIs
- **Use Auto Scaling Groups** for production workloads requiring high availability

---

## 7. Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| **Timeout on SSH connection** | Security group or NACL blocked | Verify ingress rule for port 22 & check public IP assignment |
| **`UnauthorizedOperation` error** | Missing IAM permissions | Add required `ec2:Describe*` or specific action permissions |
| **Instance stuck stopping** | Agent issues / volume problems | Try stop command again; force stop only if necessary |
| **Wrong AMI error** | Region mismatch or AMI not available | Query AMIs per region; verify AMI ID is correct |
| **Key permission denied** | Incorrect key file permissions | `chmod 400 MyKey.pem` (Linux/macOS) or fix `icacls` (Windows) |
| **Instance fails to launch** | Insufficient capacity or limits | Try different instance type or availability zone |
| **Cannot connect after reboot** | Public IP changed | Check new public IP; consider using Elastic IP |
| **High data transfer costs** | Traffic across AZs or regions | Optimize data flow; use CloudFront or local caching |
| **Performance issues** | Wrong instance type or EBS optimization | Monitor CloudWatch metrics; resize or enable EBS optimization |

### Debugging Commands
Check instance status:
````bash
aws ec2 describe-instance-status --instance-ids xxxxxxxx  # user input here (instance ID)
````

View system logs:
````bash
aws ec2 get-console-output --instance-id xxxxxxxx  # user input here (instance ID)
````

Monitor instance metrics:
````bash
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --dimensions Name=InstanceId,Value=xxxxxxxx \  # user input here (instance ID)
  --statistics Average \
  --start-time 2025-01-01T00:00:00Z \
  --end-time 2025-01-01T01:00:00Z \
  --period 300
````

---