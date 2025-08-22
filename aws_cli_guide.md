# AWS CLI v2 – Installation, Configuration, MFA & Troubleshooting

A focused guide for installing, configuring, and securely using the AWS Command Line Interface (AWS CLI v2) on Linux, macOS, and Windows.

---

## Table of Contents
1. [Overview](#1-overview)
2. [Supported Platforms](#2-supported-platforms)
3. [Prerequisites](#3-prerequisites)
4. [Installation](#4-installation)
   - [Linux](#41-linux-ubuntu--debian--rhel--centos--amazon-linux)
   - [macOS](#42-macos)
   - [Windows](#43-windows)
5. [Post‑install Verification](#5-postinstall-verification)
6. [Configuration](#6-configuration)
   - [Default Profile](#61-interactive-default-profile)
   - [Credentials & Config Files](#62-credentials--config-file-examples)
   - [Named Profiles](#63-named-profiles)
   - [Environment Variables](#64-environment-variables-override-mechanism)
   - [Profiles vs Env Vars](#65-profiles-vs-environment-variables)
7. [MFA & Temporary Credentials (STS)](#7-mfa--temporary-credentials-sts)
   - [get-session-token](#71-get-session-token-stay-as-iam-user)
   - [assume-role](#72-assume-role-change-effective-identity)
   - [Comparison](#73-comparison)
8. [CLI Output & Formatting](#8-cli-output--formatting)
9. [CLI Troubleshooting](#9-cli-troubleshooting)
10. [Best Practices](#10-best-practices)
11. [Service-Specific Documentation](#11-service-specific-documentation)

---

## 1. Overview
The AWS CLI provides a unified, scriptable interface to AWS services. This guide covers only the core CLI lifecycle: install → configure → authenticate (including MFA / roles) → verify → troubleshoot.

For service-specific operational examples, see the dedicated service guides:
- [AWS EC2 CLI Guide](aws-ec2.md)
- [AWS S3 CLI Guide](aws-s3.md) 
- [AWS IAM CLI Guide](aws-iam.md)
- [AWS CloudFormation CLI Guide](aws-cloudformation.md)
- [AWS Lambda CLI Guide](aws-lambda.md)
- [AWS RDS CLI Guide](aws-rds.md)
- [AWS CloudWatch CLI Guide](aws-cloudwatch.md)

---

## 2. Supported Platforms
- Linux (x86_64, aarch64): Ubuntu/Debian, RHEL/CentOS, Amazon Linux
- macOS (Intel & Apple silicon)
- Windows 10 / 11 (PowerShell, Command Prompt)

---

## 3. Prerequisites
- AWS account IAM user / federated SSO / role access
- Administrative or sudo rights for system installation
- `curl` and `unzip` (Linux/macOS manual install path)
- (Optional) `jq` for parsing JSON in shell scripts
- A terminal (bash / zsh / PowerShell)

---

## 4. Installation

> Use only the section matching your OS.

### 4.1 Linux (Ubuntu / Debian / RHEL / CentOS / Amazon Linux)

Update packages:

Debian / Ubuntu:
````bash
sudo apt update && sudo apt upgrade -y
````

RHEL / CentOS / Amazon Linux:
````bash
sudo yum update -y
````

Install prerequisites:
````bash
# Debian/Ubuntu
sudo apt install -y curl unzip

# RHEL/CentOS/Amazon Linux
sudo yum install -y curl unzip
````

Determine architecture:
````bash
uname -m
# Common outputs: x86_64, aarch64
````

Download (choose correct architecture):
````bash
# x86_64
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

# ARM (aarch64)
curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
````

Unzip & install:
````bash
unzip awscliv2.zip
sudo ./aws/install
````

Custom install location:
````bash
sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin
````

Verify:
````bash
aws --version
````

Uninstall:
````bash
sudo rm -rf /usr/local/aws-cli
sudo rm /usr/local/bin/aws 2>/dev/null || true
````

### 4.2 macOS

#### Method A – Homebrew (preferred for updates)
````bash
brew update
brew install awscli
aws --version
````

Upgrade later:
````bash
brew upgrade awscli
````

#### Method B – Official pkg
1. Download `AWSCLIV2.pkg` from AWS.
2. Double‑click & follow installer.
3. Verify:
````bash
aws --version
````

Remove (pkg install):
````bash
sudo rm -rf /usr/local/aws-cli
sudo rm /usr/local/bin/aws 2>/dev/null || true
````

### 4.3 Windows

#### Method A – MSI Installer
Download (browser) or run:
````powershell
msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
````
Finish wizard (Run as Administrator). Then:
````powershell
aws --version
````

#### Method B – winget
````powershell
winget source update
winget install Amazon.AWSCLI
aws --version
````

If `aws` is not recognized:
- Typical path: `C:\Program Files\Amazon\AWSCLIV2\bin\`
- Add path to System/User PATH env var
- Restart terminal

Uninstall:
````powershell
# winget
winget uninstall Amazon.AWSCLI
````
Or via Control Panel (for MSI).

---

## 5. Post‑install Verification
Run:
````bash
aws --version
aws sts get-caller-identity   # will fail if not configured
````
List regions (connectivity + permissions):
````bash
aws ec2 describe-regions --output table
````

PowerShell alternative (explicit exe):
````powershell
aws.exe sts get-caller-identity
````

---

## 6. Configuration

AWS CLI stores:
- Credentials: `~/.aws/credentials` (Linux/macOS) or `%UserProfile%\.aws\credentials`
- Config: `~/.aws/config`

### 6.1 Interactive Default Profile
````bash
aws configure
````
Prompts:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g., us-east-1)
- Default output (`json`, `yaml`, `text`, `table`)

If your key starts with `ASIA` you have temporary STS credentials; you must also supply a Session Token manually.

Add session token after configure:
````bash
# Linux/macOS
vi ~/.aws/credentials
# Windows
notepad %UserProfile%\.aws\credentials
````
Add:
````ini
aws_session_token = xxxxxxxx  # user input here (STS session token)
````

### 6.2 Credentials & Config File Examples

`~/.aws/credentials`:
````ini
[default]
aws_access_key_id = xxxxxxxx  # user input here (access key ID)
aws_secret_access_key = xxxxxxxx  # user input here (secret access key)

[prod]
aws_access_key_id = xxxxxxxx  # user input here (prod access key ID)
aws_secret_access_key = xxxxxxxx  # user input here (prod secret access key)
````

`~/.aws/config`:
````ini
[default]
region = xxxxxxxx  # user input here (default region, e.g. us-east-1)
output = json

[profile prod]
region = xxxxxxxx  # user input here (prod region, e.g. us-west-2)
output = json
````

### 6.3 Named Profiles
Create:
````bash
aws configure --profile xxxxxxxx  # user input here (profile name)
````
Use:
````bash
aws s3 ls --profile xxxxxxxx  # user input here (profile name)
````
Or export:
````bash
export AWS_PROFILE=xxxxxxxx  # user input here (profile name) - bash/zsh
````
PowerShell:
````powershell
$Env:AWS_PROFILE = 'xxxxxxxx'  # user input here (profile name)
````

### 6.4 Environment Variables (Override Mechanism)
Bash:
````bash
export AWS_ACCESS_KEY_ID="xxxxxxxx"  # user input here (access key ID)
export AWS_SECRET_ACCESS_KEY="xxxxxxxx"  # user input here (secret access key)
export AWS_SESSION_TOKEN="xxxxxxxx"  # user input here (session token, only for temporary creds)
export AWS_DEFAULT_REGION="xxxxxxxx"  # user input here (default region)
````
PowerShell:
````powershell
$Env:AWS_ACCESS_KEY_ID="xxxxxxxx"  # user input here (access key ID)
$Env:AWS_SECRET_ACCESS_KEY="xxxxxxxx"  # user input here (secret access key)
$Env:AWS_SESSION_TOKEN="xxxxxxxx"  # user input here (session token)
$Env:AWS_DEFAULT_REGION="xxxxxxxx"  # user input here (default region)
````
Unset (bash):
````bash
unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN AWS_PROFILE
````

### 6.5 Profiles vs Environment Variables
| Aspect | Profiles | Environment Variables |
|--------|----------|-----------------------|
| Persistence | Stored on disk | Temporary (session scope) |
| Use Case | Daily dev contexts | CI/CD, ephemeral sessions |
| Priority | Lower (overridden) | Higher (overrides profiles) |
| Security Rotation | Manual edit | Easy to rotate frequently |

Recommendation: Use profiles for stable contexts, env vars for automation / temporary STS sessions.

---

## 7. MFA & Temporary Credentials (STS)

### 7.1 get-session-token (Stay as IAM User)
Used when your IAM policies require MFA but you do not need to change roles.

Request:
````bash
aws sts get-session-token \
  --serial-number arn:aws:iam::xxxxxxxx:mfa/xxxxxxxx \  # user input here (account ID and MFA device name)
  --token-code xxxxxxxx \  # user input here (6-digit MFA code)
  --duration-seconds 3600
````

Response (truncated):
````json
{
  "Credentials": {
    "AccessKeyId": "ASIA....",
    "SecretAccessKey": "abcd...",
    "SessionToken": "IQoJb3...",
    "Expiration": "2025-08-17T12:34:56Z"
  }
}
````

Export (bash):
````bash
export AWS_ACCESS_KEY_ID="xxxxxxxx"  # user input here (AccessKeyId from response)
export AWS_SECRET_ACCESS_KEY="xxxxxxxx"  # user input here (SecretAccessKey from response)
export AWS_SESSION_TOKEN="xxxxxxxx"  # user input here (SessionToken from response)
````

Save to profile:
````bash
aws configure set aws_access_key_id "xxxxxxxx" --profile xxxxxxxx  # user input here (AccessKeyId and profile name)
aws configure set aws_secret_access_key "xxxxxxxx" --profile xxxxxxxx  # user input here (SecretAccessKey and profile name)
aws configure set aws_session_token "xxxxxxxx" --profile xxxxxxxx  # user input here (SessionToken and profile name)
````
Use:
````bash
aws s3 ls --profile xxxxxxxx  # user input here (profile name)
````

### 7.2 assume-role (Change Effective Identity)
Common for cross-account access, privilege escalation with MFA, or separating duties.

````bash
aws sts assume-role \
  --role-arn arn:aws:iam::xxxxxxxx:role/xxxxxxxx \  # user input here (account ID and role name)
  --role-session-name xxxxxxxx \  # user input here (session name)
  --serial-number arn:aws:iam::xxxxxxxx:mfa/xxxxxxxx \  # user input here (account ID and MFA device name)
  --token-code xxxxxxxx  # user input here (6-digit MFA code)
````

Extract & export (bash):
````bash
CREDS_JSON=$(aws sts assume-role ... )
export AWS_ACCESS_KEY_ID=$(echo "$CREDS_JSON" | jq -r '.Credentials.AccessKeyId')
export AWS_SECRET_ACCESS_KEY=$(echo "$CREDS_JSON" | jq -r '.Credentials.SecretAccessKey')
export AWS_SESSION_TOKEN=$(echo "$CREDS_JSON" | jq -r '.Credentials.SessionToken')
````

PowerShell example:
````powershell
$creds = aws sts assume-role --role-arn arn:aws:iam::xxxxxxxx:role/xxxxxxxx --role-session-name xxxxxxxx  # user input here (account ID, role name, and session name)
$ak = ($creds | ConvertFrom-Json).Credentials.AccessKeyId
$sk = ($creds | ConvertFrom-Json).Credentials.SecretAccessKey
$st = ($creds | ConvertFrom-Json).Credentials.SessionToken
$Env:AWS_ACCESS_KEY_ID  = $ak
$Env:AWS_SECRET_ACCESS_KEY = $sk
$Env:AWS_SESSION_TOKEN = $st
````

### 7.3 Comparison

| Feature | get-session-token | assume-role |
|---------|-------------------|-------------|
| Identity | Same IAM user | Role (different principal) |
| Permissions | Same as user | Role policy set |
| Typical Use | Add MFA to user | Cross-account / elevated rights |
| Max Duration | Up to 36h (user policy dependent) | Up to 12h (role setting) |
| MFA | At call if required | In trust policy / enforced |
| ExternalId | N/A | Supported |

---

## 8. CLI Output & Formatting

### Output Formats
````bash
aws ec2 describe-instances --output json    # Default JSON format
aws ec2 describe-instances --output yaml    # YAML format
aws ec2 describe-instances --output text    # Tab-separated text
aws ec2 describe-instances --output table   # Human-readable table
````

### Query Filtering
Extract specific fields using JMESPath:
````bash
aws ec2 describe-instances --query 'Reservations[].Instances[].{ID:InstanceId,State:State.Name}'
````

Get only running instances:
````bash
aws ec2 describe-instances \
  --filters Name=instance-state-name,Values=running \
  --query "Reservations[].Instances[].InstanceId" \
  --output text
````

### Pagination
Handle large result sets:
````bash
aws ec2 describe-instances --max-items 50 --starting-token xxxxxxxx  # user input here (pagination token)
````

---

## 9. CLI Troubleshooting

| Symptom | Cause | Resolution |
|---------|-------|-----------|
| `aws: command not found` | PATH missing | Reinstall or add install `bin` to PATH |
| `'aws' is not recognized` (Windows) | PATH not refreshed | Reopen terminal / add `C:\Program Files\Amazon\AWSCLIV2\bin` |
| `AccessDenied` | Missing permissions / wrong role | Check active credentials (`aws sts get-caller-identity`) |
| Invalid MFA token | Clock drift / wrong device | Verify device time & ARN |
| `Could not connect to the endpoint URL` | Wrong region / network / proxy | Confirm region flag or set `AWS_DEFAULT_REGION` |
| SSL errors | Corporate MITM / missing CA bundle | Configure `AWS_CA_BUNDLE` or trust corporate CA |
| Wrong profile used | Env var precedence | `unset AWS_PROFILE` or inspect `env \| grep AWS` |
| `ExpiredToken` | STS creds expired | Re-run `get-session-token` / `assume-role` |

Inspect current identity:
````bash
aws sts get-caller-identity
````
List configuration:
````bash
cat ~/.aws/credentials
cat ~/.aws/config
````

Enable debug mode:
````bash
aws --debug ec2 describe-regions
````

---

## 10. Best Practices

- **Prefer roles + MFA** over long‑lived user keys
- Keep least privilege: separate read-only, dev, prod profiles
- Avoid checking credentials into scripts; inject via environment/secrets manager in CI
- Rotate access keys regularly; remove unused ones
- Use `--profile` explicitly in automation to reduce ambiguity
- Validate commands with `--dry-run` (services that support it, e.g., EC2, certain actions)
- Leverage `--output yaml` or `--query` for clean structured automation
- Use `aws configure sso` for AWS IAM Identity Center (SSO) if available
- Set resource limits using CLI configuration to prevent accidental large operations
- Use `--cli-input-json` for complex commands with many parameters
- Test commands in non-production environments first

---

## 11. Service-Specific Documentation

This guide covers core AWS CLI functionality. For detailed examples of working with specific AWS services, refer to these guides:

- **[AWS EC2 CLI Guide](aws-ec2.md)** - Instance lifecycle, key pairs, security groups, SSH access
- **[AWS S3 CLI Guide](aws-s3.md)** - Bucket operations, object uploads/downloads, sync, presigned URLs
- **[AWS IAM CLI Guide](aws-iam.md)** - Users, roles, policies, access keys, permission management
- **[AWS CloudFormation CLI Guide](aws-cloudformation.md)** - Stack deployment, change sets, drift detection
- **[AWS Lambda CLI Guide](aws-lambda.md)** - Function creation, invocation, versions, environment variables
- **[AWS RDS CLI Guide](aws-rds.md)** - Database instances, snapshots, parameter groups
- **[AWS CloudWatch CLI Guide](aws-cloudwatch.md)** - Logs, metrics, alarms, monitoring

Each service guide includes:
- Service-specific CLI commands and syntax
- Cross-platform examples (Linux/macOS/Windows)
- Best practices tailored to the service
- Common troubleshooting scenarios

---