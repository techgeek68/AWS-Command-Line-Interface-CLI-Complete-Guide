# AWS CLI — Professional Guide (Windows, macOS, Linux)

> A step‑by‑step, GitHub-ready Markdown guide for installing, configuring, and using **AWS CLI v2** on Windows, macOS (Intel & Apple silicon), and Linux (Ubuntu/Debian, RHEL/CentOS, Amazon Linux). Includes small but critical steps, platform differences, and troubleshooting tips.

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
   - [Linux (Ubuntu/Debian, RHEL/CentOS, Amazon Linux)](#linux)
   - [macOS (Homebrew / pkg)](#macos)
   - [Windows (MSI / winget)](#windows)
4. [Post-install verification](#post-install-verification)
5. [Configuration (credentials, profiles, env vars)](#configuration)
6. [MFA & temporary credentials (STS)](#mfa--temporary-credentials)
7. [Common tasks (cross-platform examples)](#common-tasks)
8. [Troubleshooting & common errors](#troubleshooting)
9. [Useful commands & best practices](#useful-commands--best-practices)
10. [Appendix: file locations & examples](#appendix)

---

## Overview

The **AWS CLI** provides a unified tool to manage AWS services from your terminal. This guide targets **AWS CLI v2**, which ships as a native binary and does not require a separate Python install.

Supported platforms covered:
- Linux (x86_64 and aarch64) — Ubuntu/Debian, RHEL/CentOS, Amazon Linux
- macOS — Intel & Apple silicon (via Homebrew or official pkg)
- Windows 10 / 11 — MSI installer or winget

---

## Prerequisites

- An AWS account or IAM user with programmatic access (Access Key ID + Secret Access Key) or SSO.
- Administrator / sudo privileges for system installs.
- `curl`, `unzip` (Linux/macOS) for the manual installer paths.

---

## Installation

> Use the platform section that matches your OS. Commands shown for both bash (Linux/macOS) and PowerShell (Windows) where applicable.

### Linux (Ubuntu / Debian / RHEL / CentOS / Amazon Linux)

1. **Update packages**

```bash
# Debian/Ubuntu
sudo apt update && sudo apt upgrade -y

# RHEL/CentOS/Amazon Linux
sudo yum update -y
```

2. **Install prerequisites**

```bash
# Debian/Ubuntu
sudo apt install -y curl unzip

# RHEL/CentOS/AmazonLinux
sudo yum install -y curl unzip
```

3. **Download the AWS CLI v2 zip** (choose x86_64 or aarch64)

```bash
# x86_64
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

# aarch64 (ARM)
curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
```

4. **Unzip & install**

```bash
unzip awscliv2.zip
sudo ./aws/install
```

Optional: install to custom location and place symlink/exec in PATH

```bash
sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin
```

5. **Verify**

```bash
aws --version
# Example output: aws-cli/2.x.x Python/3.x Linux/4.x.x botocore/2.x.x
```

6. **Uninstall** (if needed)

```bash
sudo rm -rf /usr/local/aws-cli
sudo rm /usr/local/bin/aws
```

---

### macOS (Intel & Apple silicon)

#### Method A — Homebrew (recommended)

```bash
brew update
brew install awscli
aws --version
```

> If you previously installed via the pkg installer, consider `brew uninstall awscli` to avoid conflicts.

#### Method B — Official macOS pkg

1. Download the `AWSCLIV2.pkg` from the official AWS site.
2. Double-click the `.pkg` and follow the Installer.
3. Verify in Terminal:

```bash
aws --version
```

---

### Windows (Windows 10 / 11)

#### Method A — MSI Installer
1. Download `AWSCLIV2.msi` from the official AWS distribution.
2. Right‑click → **Run as administrator** → follow the wizard.
3. Verify in PowerShell or Command Prompt:

```powershell
aws --version
```

#### Method B — winget (scriptable, preferred for automation)

```powershell
winget source update
winget install Amazon.AWSCLI
aws --version
```

##### If `aws` not recognized
- Typical install path: `C:\Program Files\Amazon\AWSCLIV2\` or `C:\Program Files\Amazon\AWSCLI\`.
- Add the `bin` folder to PATH: `C:\Program Files\Amazon\AWSCLIV2\bin\`.
- Restart terminal after changing environment variables.

---

## Post-install verification

Run these on any OS to verify basic functionality:

```bash
aws --version
aws sts get-caller-identity
aws ec2 describe-regions --output table
```

If `aws sts get-caller-identity` errors with credentials, proceed to configuration.

---

## Configuration

AWS CLI stores credentials in `~/.aws/credentials` and config in `~/.aws/config` (or `%UserProfile%\.aws\` on Windows).

### Quick interactive configure

```bash
aws configure
```

You will be prompted for:
- AWS Access Key ID
- AWS Secret Access Key
- Default region name (e.g., `us-east-1`)
- Default output format (`json`, `text`, `table`)

### Named profiles

Create a profile called `prod`:

```bash
aws configure --profile prod
```

Use it:

```bash
aws s3 ls --profile prod
# or set AWS_PROFILE environment variable
export AWS_PROFILE=prod        # bash
$Env:AWS_PROFILE='prod'        # PowerShell
```

### Environment variables (session-scoped)

**Linux/macOS (bash)**

```bash
export AWS_ACCESS_KEY_ID="AKIA..."
export AWS_SECRET_ACCESS_KEY="..."
export AWS_DEFAULT_REGION="us-east-1"
```

**Windows PowerShell**

```powershell
$Env:AWS_ACCESS_KEY_ID = "AKIA..."
$Env:AWS_SECRET_ACCESS_KEY = "..."
$Env:AWS_DEFAULT_REGION = "us-east-1"
```

> Environment variables override profile files for the running session.

### Credentials & config file examples

**`~/.aws/credentials`**

```ini
[default]
aws_access_key_id = AKIA...
aws_secret_access_key = ...

[prod]
aws_access_key_id = AKIA_PROD...
aws_secret_access_key = prodsecret...
```

**`~/.aws/config`**

```ini
[default]
region = us-east-1
output = json

[profile prod]
region = us-west-2
output = json
```

---

## MFA & temporary credentials (STS)

If your account requires MFA, obtain temporary credentials with `aws sts get-session-token`.

```bash
aws sts get-session-token \
  --serial-number arn:aws:iam::123456789012:mfa/your-username \
  --token-code 123456 \
  --duration-seconds 3600
```

The response contains `AccessKeyId`, `SecretAccessKey`, and `SessionToken` — export these as env vars or save them to a profile.

**Assume role (with MFA if required)**

```bash
aws sts assume-role \
  --role-arn arn:aws:iam::123456789012:role/YourRole \
  --role-session-name sessionName \
  --serial-number arn:aws:iam::123456789012:mfa/your-username \
  --token-code 123456
```

---

## Common tasks (cross-platform examples)

> Commands show bash first, then PowerShell where the syntax differs.

### Create and save an EC2 key pair

**Linux / macOS (bash)**

```bash
aws ec2 create-key-pair \
  --key-name MyProdKey \
  --key-type rsa \
  --key-format pem \
  --query 'KeyMaterial' --output text > MyProdKey.pem && chmod 400 MyProdKey.pem
```

**Windows PowerShell**

```powershell
aws ec2 create-key-pair --key-name MyProdKey --key-type rsa --key-format pem --query 'KeyMaterial' --output text > MyProdKey.pem
icacls MyProdKey.pem /inheritance:r /grant:r "$($env:USERNAME):(R)"
```

Connect:

```bash
ssh -i MyProdKey.pem ec2-user@ec2-198-51-100-1.compute-1.amazonaws.com
```

Delete (AWS side):

```bash
aws ec2 delete-key-pair --key-name MyProdKey
```

---

### Create a Security Group and add rules

1. **Get the VPC ID**

```bash
# bash
VPC_ID=$(aws ec2 describe-vpcs --query "Vpcs[0].VpcId" --output text)
echo $VPC_ID

# PowerShell
$VPC_ID = (aws ec2 describe-vpcs --query "Vpcs[0].VpcId" --output text)
$VPC_ID
```

2. **Create the security group**

```bash
# bash (requires jq to parse JSON)
SG_JSON=$(aws ec2 create-security-group --group-name MySecurityGroup --description "My security group" --vpc-id $VPC_ID)
SG_ID=$(echo $SG_JSON | jq -r '.GroupId')
echo $SG_ID

# PowerShell
$create = aws ec2 create-security-group --group-name MySecurityGroup --description "My security group" --vpc-id $VPC_ID --output json
$SG_ID = (ConvertFrom-Json $create).GroupId
$SG_ID
```

3. **Add ingress rules**

```bash
# SSH (port 22) and HTTP (port 80)
aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 22 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 80 --cidr 0.0.0.0/0
```

4. **List & Delete**

```bash
aws ec2 describe-security-groups --group-ids $SG_ID
aws ec2 delete-security-group --group-id $SG_ID
```

---

## Troubleshooting & common errors

- **`aws: command not found` / `'aws' is not recognized`**: Ensure AWS CLI binary installed and on PATH. On Windows, add `C:\Program Files\Amazon\AWSCLIV2\bin\` to PATH and restart terminal.

- **Permissions errors with `.pem` files**: `chmod 400 MyKey.pem` (Linux/macOS). On Windows, use `icacls` to remove inheritance and restrict to your user.

- **Credential/AccessDenied**: Validate credentials, check IAM policy, or use assumed roles/MFA as required.

- **SSL/curl download errors**: Ensure `curl` is installed and CA certs present.

- **Could not connect to the endpoint URL**: Verify network, region, and proxy settings. Configure `HTTP_PROXY` / `HTTPS_PROXY` for corporate proxies.

---

## Useful commands & best practices

- Verify identity:

```bash
aws sts get-caller-identity
```

- List regions:

```bash
aws ec2 describe-regions --output table
```

- S3: list buckets

```bash
aws s3 ls
```

- Use named profiles and avoid storing long-lived credentials in source control.
- Prefer role assumption with least privilege.
- Rotate access keys regularly and delete unused keys.

---

## Appendix: file locations & examples

- macOS / Linux: `~/.aws/credentials` and `~/.aws/config`
- Windows: `%UserProfile%\.aws\credentials` and `%UserProfile%\.aws\config`

**Example `~/.aws/credentials`**

```ini
[default]
aws_access_key_id = AKIA...
aws_secret_access_key = ...

[dev]
aws_access_key_id = AKIADEV...
aws_secret_access_key = devsecret...
```

**Example `~/.aws/config`**

```ini
[default]
region = us-east-1
output = json

[profile dev]
region = us-west-2
output = json
```

---

### Want more?
If you'd like, I can:
- Export this Markdown to a downloadable `README.md` file.
- Create a one‑page printable cheat sheet.
- Add a GitHub Actions workflow that installs the AWS CLI and runs a sample command as part of CI.
- Commit this file to a GitHub repo (provide repository & token) or open a PR.

Tell me which action you want and I'll do it now.

