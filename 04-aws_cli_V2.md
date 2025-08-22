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
8. [CLI Troubleshooting](#8-cli-troubleshooting-core-only)
9. [Best Practices](#9-best-practices-cli-scope)
10. [What’s Next](#whats-next)

---

## 1. Overview
The AWS CLI provides a unified, scriptable interface to AWS services. This guide covers only the core CLI lifecycle: install → configure → authenticate (including MFA / roles) → verify → troubleshoot.

Service task examples now live in:
- `docs/aws-ec2.md`
- `docs/aws-s3.md`
- `docs/aws-iam.md`
- `docs/aws-cloudformation.md`
- `docs/aws-lambda.md`
- `docs/aws-rds.md`
- `docs/aws-cloudwatch.md`

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
```bash
sudo apt update && sudo apt upgrade -y
```

RHEL / CentOS / Amazon Linux:
```bash
sudo yum update -y
```

Install prerequisites:
```bash
# Debian/Ubuntu
sudo apt install -y curl unzip

# RHEL/CentOS/Amazon Linux
sudo yum install -y curl unzip
```

Determine architecture:
```bash
uname -m
# Common outputs: x86_64, aarch64
```

Download (choose correct architecture):
```bash
# x86_64
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

# ARM (aarch64)
curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
```

Unzip & install:
```bash
unzip awscliv2.zip
sudo ./aws/install
```

Custom install location:
```bash
sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin
```

Verify:
```bash
aws --version
```

Uninstall:
```bash
sudo rm -rf /usr/local/aws-cli
sudo rm /usr/local/bin/aws 2>/dev/null || true
```

### 4.2 macOS

#### Method A – Homebrew (preferred for updates)
```bash
brew update
brew install awscli
aws --version
```

Upgrade later:
```bash
brew upgrade awscli
```

#### Method B – Official pkg
1. Download `AWSCLIV2.pkg` from AWS.
2. Double‑click & follow installer.
3. Verify:
```bash
aws --version
```

Remove (pkg install):
```bash
sudo rm -rf /usr/local/aws-cli
sudo rm /usr/local/bin/aws 2>/dev/null || true
```

### 4.3 Windows

#### Method A – MSI Installer
Download (browser) or run:
```powershell
msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
```
Finish wizard (Run as Administrator). Then:
```powershell
aws --version
```

#### Method B – winget
```powershell
winget source update
winget install Amazon.AWSCLI
aws --version
```

If `aws` is not recognized:
- Typical path: `C:\Program Files\Amazon\AWSCLIV2\bin\`
- Add path to System/User PATH env var
- Restart terminal

Uninstall:
```powershell
# winget
winget uninstall Amazon.AWSCLI
```
Or via Control Panel (for MSI).

---

## 5. Post‑install Verification
Run:
```bash
aws --version
aws sts get-caller-identity   # will fail if not configured
```
List regions (connectivity + permissions):
```bash
aws ec2 describe-regions --output table
```

PowerShell alternative (explicit exe):
```powershell
aws.exe sts get-caller-identity
```

---

## 6. Configuration

AWS CLI stores:
- Credentials: `~/.aws/credentials` (Linux/macOS) or `%UserProfile%\.aws\credentials`
- Config: `~/.aws/config`

### 6.1 Interactive Default Profile
```bash
aws configure
```
Prompts:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g., us-east-1)
- Default output (`json`, `yaml`, `text`, `table`)

If your key starts with `ASIA` you have temporary STS credentials; you must also supply a Session Token manually.

Add session token after configure:
```bash
# Linux/macOS
vi ~/.aws/credentials
# Windows
notepad %UserProfile%\.aws\credentials
```
Add:
```
aws_session_token = <SESSION_TOKEN>
```

### 6.2 Credentials & Config File Examples

`~/.aws/credentials`:
```ini
[default]
aws_access_key_id = AKIA_DEFAULT...
aws_secret_access_key = defaultSecret...

[prod]
aws_access_key_id = AKIA_PROD...
aws_secret_access_key = prodSecret...
```

`~/.aws/config`:
```ini
[default]
region = us-east-1
output = json

[profile prod]
region = us-west-2
output = json
```

### 6.3 Named Profiles
Create:
```bash
aws configure --profile prod
```
Use:
```bash
aws s3 ls --profile prod
```
Or export:
```bash
export AWS_PROFILE=prod  # bash/zsh
```
PowerShell:
```powershell
$Env:AWS_PROFILE = 'prod'
```

### 6.4 Environment Variables (Override Mechanism)
Bash:
```bash
export AWS_ACCESS_KEY_ID="AKIA..."
export AWS_SECRET_ACCESS_KEY="..."
export AWS_SESSION_TOKEN="..."        # only for temporary creds
export AWS_DEFAULT_REGION="us-east-1"
```
PowerShell:
```powershell
$Env:AWS_ACCESS_KEY_ID="AKIA..."
$Env:AWS_SECRET_ACCESS_KEY="..."
$Env:AWS_SESSION_TOKEN="..."
$Env:AWS_DEFAULT_REGION="us-east-1"
```
Unset (bash):
```bash
unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN AWS_PROFILE
```

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
```bash
aws sts get-session-token \
  --serial-number arn:aws:iam::123456789012:mfa/your-username \
  --token-code 123456 \
  --duration-seconds 3600
```

Response (truncated):
```json
{
  "Credentials": {
    "AccessKeyId": "ASIA....",
    "SecretAccessKey": "abcd...",
    "SessionToken": "IQoJb3...",
    "Expiration": "2025-08-17T12:34:56Z"
  }
}
```

Export (bash):
```bash
export AWS_ACCESS_KEY_ID="ASIA..."
export AWS_SECRET_ACCESS_KEY="abcd..."
export AWS_SESSION_TOKEN="IQoJb3..."
```

Save to profile:
```bash
aws configure set aws_access_key_id "ASIA..."     --profile mfa
aws configure set aws_secret_access_key "abcd..." --profile mfa
aws configure set aws_session_token "IQoJb3..."   --profile mfa
```
Use:
```bash
aws s3 ls --profile mfa
```

### 7.2 assume-role (Change Effective Identity)
Common for cross-account access, privilege escalation with MFA, or separating duties.

```bash
aws sts assume-role \
  --role-arn arn:aws:iam::123456789012:role/AdminRole \
  --role-session-name mySession \
  --serial-number arn:aws:iam::123456789012:mfa/your-username \
  --token-code 123456
```

Extract & export (bash):
```bash
CREDS_JSON=$(aws sts assume-role ... )
export AWS_ACCESS_KEY_ID=$(echo "$CREDS_JSON" | jq -r '.Credentials.AccessKeyId')
export AWS_SECRET_ACCESS_KEY=$(echo "$CREDS_JSON" | jq -r '.Credentials.SecretAccessKey')
export AWS_SESSION_TOKEN=$(echo "$CREDS_JSON" | jq -r '.Credentials.SessionToken')
```

PowerShell example:
```powershell
$creds = aws sts assume-role --role-arn arn:aws:iam::123456789012:role/AdminRole --role-session-name mySession
$ak = ($creds | ConvertFrom-Json).Credentials.AccessKeyId
$sk = ($creds | ConvertFrom-Json).Credentials.SecretAccessKey
$st = ($creds | ConvertFrom-Json).Credentials.SessionToken
$Env:AWS_ACCESS_KEY_ID  = $ak
$Env:AWS_SECRET_ACCESS_KEY = $sk
$Env:AWS_SESSION_TOKEN = $st
```

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

## 8. CLI Troubleshooting (Basic Only)

| Symptom | Cause | Resolution |
|---------|-------|-----------|
| `aws: command not found` | PATH missing | Reinstall or add install `bin` to PATH |
| `'aws' is not recognized` (Windows) | PATH not refreshed | Reopen terminal / add `C:\Program Files\Amazon\AWSCLIV2\bin` |
| `AccessDenied` | Missing permissions / wrong role | Check active credentials (`aws sts get-caller-identity`) |
| Invalid MFA token | Clock drift / wrong device | Verify device time & ARN |
| `Could not connect to the endpoint URL` | Wrong region / network / proxy | Confirm region flag or set `AWS_DEFAULT_REGION` |
| SSL errors | Corporate MITM / missing CA bundle | Configure `AWS_CA_BUNDLE` or trust corporate CA |
| Wrong profile used | Env var precedence | `unset AWS_PROFILE` or inspect `env | grep AWS` |
| `ExpiredToken` | STS creds expired | Re-run `get-session-token` / `assume-role` |

Inspect current identity:
```bash
aws sts get-caller-identity
```
List files:
```bash
cat ~/.aws/credentials
cat ~/.aws/config
```

---

## 9. Best Practices (CLI Scope)
- Prefer **roles + MFA** over long‑lived user keys.
- Keep least privilege: separate read-only, dev, prod profiles.
- Avoid checking credentials into scripts; inject via environment/secrets manager in CI.
- Rotate access keys regularly; remove unused ones.
- Use `--profile` explicitly in automation to reduce ambiguity.
- Validate commands with `--dry-run` (services that support it, e.g., EC2, certain actions).
- Leverage `--output yaml` or `--query` for clean structured automation.
- Use `aws configure sso` for AWS IAM Identity Center (SSO) if available (not covered in depth here to keep scope concise).

---

## What’s Next
See service guides in chapter `04.4.xx` for task-focused examples (EC2, S3, IAM, etc.).

---
