# AWS CLI — Complete Guide (Windows, macOS, Linux)

> A step‑by‑step guide for installing, configuring, and using **AWS CLI v2** on Windows, macOS (Intel & Apple silicon), and Linux (Ubuntu/Debian, RHEL/CentOS, Amazon Linux). Includes small but critical steps, platform differences, and troubleshooting tips.

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
   - [Linux (Ubuntu/Debian, RHEL/CentOS, Amazon Linux)](#linux)
   - [macOS (Homebrew/pkg)](#macos)
   - [Windows (MSI/winget)](#windows)
4. [Post-install verification](#post-install-verification)
5. [Configuration(credentials, profiles, env vars)](#configuration)
6. [MFA and temporary credentials (STS)](#mfa-temporary-credentials)
7. [Common tasks (cross-platform examples)](#common-tasks)
8. [Troubleshooting & common errors](#troubleshooting)
9. [Useful commands & best practices](#useful-commands--best-practices)

---

## Overview

The **AWS CLI** provides a unified tool to manage AWS services from your terminal. This guide targets **AWS CLI v2**, which ships as a native binary and does not require a separate Python install.

Supported platforms covered:
   - Linux (x86_64 and aarch64)
      - Ubuntu/Debian, RHEL/CentOS, Amazon Linux
   - macOS
      - Intel & Apple silicon (via Homebrew or official pkg)
   - Windows 10 / 11
      - MSI installer or winget
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

Debian/Ubuntu:
```bash
   sudo apt update && sudo apt upgrade -y
```

RHEL/CentOS/Amazon Linux:
```bash
   sudo yum update -y
```

2. **Install prerequisites**

Debian/Ubuntu:

```bash
   sudo apt install -y curl unzip
```

RHEL/CentOS/AmazonLinux:

```bash
   sudo yum install -y curl unzip
```

3. **Download the AWS CLI v2 zip** (Choose x86_64 or aarch64)

**How to know your system architecture ?**:

   For Windows, run the command:
```
      wmic os get osarchitecture
```
   For Linux & Mac, run the command:
```
      unname -m
```

For x86_64
```bash
   curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
```

For aarch64 (ARM)
```bash
   curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
```

4. **Unzip & install**
   
Unzip:
```bash
   unzip awscliv2.zip
```

Install:
```bash
   sudo ./aws/install
```

Optional:
   Install to a custom location and place a symlink/exec in PATH

```bash
   sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin
```

5. **Verify**

```bash
   aws --version

#Example output: aws-cli/2.x.x Python/3.x Linux/4.x.x botocore/2.x.x
```

6. **Uninstall** (if needed)

```bash
   sudo rm -rf /usr/local/aws-cli
```
```bash
   sudo rm /usr/local/bin/aws
```
---

### macOS (Intel & Apple silicon)

#### Method A — Homebrew (recommended)
Update:
```bash
   brew update
```
Install:
```bash
   brew install awscli
```
Verify:
```bash
   aws --version
```

> If you previously installed via the pkg installer, consider `brew uninstall awscli` to avoid conflicts.

#### Method B — Official macOS pkg

1. Download the `AWSCLIV2.pkg` from the official AWS site.
   
3. Double-click the `.pkg` and follow the Installer.
   
5. Verify in Terminal:

```bash
   aws --version
```
---

### Windows (Windows 10 / 11)

#### Method A — MSI Installer
   1. Download `AWSCLIV2.msi` from the official AWS distribution.
      
   Download link:
```
      https://awscli.amazonaws.com/AWSCLIV2.msi
```

   or Download in PowerShell or Command Prompt:
```
      msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
```

   2. Right‑click → **Run as administrator** → follow the wizard.
      
   4. Verify in PowerShell or Command Prompt:

```powershell
   aws --version
```

#### Method B — winget (scriptable, preferred for automation)

```powershell
      winget source update
```

```powershell
      winget install Amazon.AWSCLI
```

For PowerShell:
```powershell
      aws.exe --version
```

For Command Prompt:
```
      aws --version
```

##### If `aws` is not recognized
- Typical install path: `C:\Program Files\Amazon\AWSCLIV2\` or `C:\Program Files\Amazon\AWSCLI\`
  
- Add the `bin` folder to PATH: `C:\Program Files\Amazon\AWSCLIV2\bin\`
  
- Restart the terminal after changing environment variables

### Uninstalling AWS CLI v2
**Method A — if installed via MSI**
   - Open Control Panel
   - Programs and Features
   - Find AWS Command Line Interface v2
   - Right-click
   - Uninstall


**Method B — if installed via winget**

Uninstall:
```powershell
      winget uninstall Amazon.AWSCLI
```

Verify:
```
      aws    --version
```
---

## Post-install verification

Run these on any OS to verify basic functionality:

```bash
   aws --version
```
```bash
   aws sts get-caller-identity
```
```bash
   aws ec2 describe-regions --output table
```

If `aws sts get-caller-identity` errors with credentials, proceed to configuration.

---

> Note: In PowerShell, make sure to run AWS CLI commands using the full executable name:

```
   aws.exe --version
```
```
   aws sts get-caller-identity
```
```
   aws.exe configure
```
---

## Configuration
AWS CLI stores credentials in `~/.aws/credentials` and config in `~/.aws/config` (or `%UserProfile%\.aws\` on Windows).

**Interactive configure for default profile**

```bash
   aws configure
```

You will be prompted for:
   - AWS Access Key ID:
   - AWS Secret Access Key:
   - Default region name (e.g., `us-east-1`):
   - Default output format (`json`, `text`, `table`):


Additionally, if your Access Key ID begins with ASIA, it indicates that STS temporary credentials are being used, which require you to provide a Session Token manually.


On Windows OS: `C:\Users\<Your_Host_Name>\.aws\credentials`

Open the file with the help of a text editor and then,

```
   aws_session_token= <Enter Your Token Here>
```

On Linux/Mac:  `cd ~/.aws/`
```
   sudo vi credentials
```
```
   aws_session_token= <Enter Your Token Here>
```

### Named profiles (Multiple Profiles Configuration)
- It sets up a named profile called prod in the same files, without changing the default profile.
- This allows you to manage multiple sets of credentials (for dev, staging, prod, etc.).

**Create a profile called** *`prod`*:

```bash
   aws configure --profile prod
```

Use it:

```bash
   aws s3 ls --profile prod
```

or set AWS_PROFILE environment variable:

`Bash`
```bash
   export AWS_PROFILE=prod
```

`PowerShell`
```powershell
   $Env:AWS_PROFILE='prod'                 
```

### Environment variables
- Environment variables are just another way of supplying credentials & region — but they take priority over profile files and are best for temporary sessions and automation.

- Environment variables aren’t “necessary” all the time, but they’re a powerful way to override, isolate, and automate credentials/regions securely and temporarily, without changing your permanent AWS config.

***Profiles vs Environment Variables**
> **Profiles** (aws configure)
   > Good for long-term developer use on your laptop. You can switch the profile.

> **Environment variables**
   > Good for temporary sessions, automation, and CI/CD, where you need a quick override or don’t want to persist credentials.

**Linux/macOS (`bash`)**

```bash
      export AWS_ACCESS_KEY_ID="AKIA..."
      export AWS_SECRET_ACCESS_KEY="..."
      export AWS_DEFAULT_REGION="us-east-1"
```

**Windows (`PowerShell`)**

```powershell
      $Env:AWS_ACCESS_KEY_ID = "AKIA..."
      $Env:AWS_SECRET_ACCESS_KEY = "..."
      $Env:AWS_DEFAULT_REGION = "us-east-1"
```

### Credentials & Config File Examples:

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

## MFA & Temporary Credentials (STS)

- Some AWS accounts require Multi-Factor Authentication (MFA) for extra security.
  
- When MFA is enforced, your long-lived IAM AccessKey/Secret alone won’t work.
  
- You must authenticate with your MFA device to obtain short-lived credentials (via STS).
  
- If your account requires MFA, obtain temporary credentials with `aws sts get-session-token`.
   - In this method, you stay as your IAM user, but get temporary credentials (useful if MFA        is required).

```bash
   aws sts get-session-token \
     --serial-number arn:aws:iam::123456789012:mfa/your-username \
     --token-code 123456 \
     --duration-seconds 3600
```
---
**Complete Example**:

1. You call aws sts get-session-token with:
   
`--serial-number: The ARN of your MFA device (like arn:aws:iam::123456789012:mfa/your-username)`

`--token-code:      The 6-digit code from your MFA app/device`

`--duration-seconds: How long the credentials should last (e.g., 3600 = 1 hour)`

2. AWS returns temporary security credentials:
```
{
  "Credentials": {
    "AccessKeyId": "ASIA....",
    "SecretAccessKey": "abcd....",
    "SessionToken": "IQoJb3....",
    "Expiration": "2025-08-17T12:34:56Z"
  }
}
```

3. You then export these as environment variables so AWS CLI/SDKs can use them:
```
   export AWS_ACCESS_KEY_ID="ASIA...."
   export AWS_SECRET_ACCESS_KEY="abcd...."
   export AWS_SESSION_TOKEN="IQoJb3...."
```

Or save them into a named profile (recommended if you don’t want to overwrite your defaults):
```
   aws configure set aws_access_key_id "ASIA..."     --profile mfa
   aws configure set aws_secret_access_key "abcd..." --profile mfa
   aws configure set aws_session_token "IQoJb3..."   --profile mfa
```

4. Now run commands using the profile:
```
   aws s3 ls --profile mfa
```

---
**Assume role:**

   - Returns temporary credentials (AccessKeyId, SecretAccessKey, SessionToken).

   - You use these creds to act in the role, not as your IAM user.


**Commonly used for:**

   - Cross-account access (jump into another AWS account).

   - Privilege separation (use a low-privilege user + assume a role for admin tasks).

   - MFA enforcement (if the trust policy requires MFA).


**Parameters:**

   - RoleArn: The ARN of the IAM role you want to assume. (required)

   - RoleSessionName: A unique name for your session (shows up in CloudTrail). (required)

   - DurationSeconds: How long the session lasts (default 1h, max up to 12h depending on role config).

   - SerialNumber + TokenCode: Provide these if the role’s trust policy enforces MFA.

   - Policy / PolicyArns: You can further restrict the session’s permissions (session policies).

   - Tags / TransitiveTagKeys: Pass tags to the session (can be used for ABAC — attribute-based access control).

   - ExternalId: Extra security for cross-account trust (often used when granting access to third parties).


**Permissions Needed:**

   - The role’s trust policy must allow you (or your account) to assume it.

   - Your IAM user or group policy must grant sts: AssumeRole on that role ARN.


Example:   

```bash
aws sts assume-role \
  --role-arn arn:aws:iam::123456789012:role/YourRole \
  --role-session-name mySession \
  --serial-number arn:aws:iam::123456789012:mfa/your-username \
  --token-code 123456
```

---

***Comparison: `get-session-token` vs `assume-role`**

| Feature     | `get-session-token`               | `assume-role`                                         |
| ----------- | --------------------------------- | ----------------------------------------------------- |
| Identity    | **Stays as IAM user**             | **Becomes role** (assumed role session)               |
| Permissions | Same as IAM user                  | Role’s permissions (may differ from your user’s)      |
| MFA         | Used when IAM policy requires MFA | Used when role trust policy requires MFA              |
| Duration    | Up to 36h (IAM user)              | Up to 12h (role, if configured)                       |
| Use Case    | Add MFA to user sessions          | Switch to different role (e.g., admin, cross-account) |

---


## Common tasks (cross-platform examples)
The demonstration below shows how to perform common AWS CLI tasks on both Linux/macOS (bash) and Windows (PowerShell)

### Create and save an EC2 key pair

**Linux/macOS (bash)**

Syntax:

```bash
   aws ec2 create-key-pair \
     --key-name <Key_Pair_Name> \
     --key-type <Key_Pair_Type> \
     --key-format <Key_Pair_Format> \
     --query 'KeyMaterial' --output text > <Key_Pair_Name> && chmod <Permission> <Key_Pair_Name>
```
      
Example:

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

**Connect:**

Syntax:
```bash
   ssh -i Key_Name.pem User_Name@Public_DNS
```

Example:

```bash
   ssh -i MyProdKey.pem ec2-user@ec2-xxx-xx-xxx-x.compute-1.amazonaws.com
```

**Delete (AWS side)**:

```bash
   aws ec2 delete-key-pair --key-name MyProdKey
```

---

### Create a Security Group and add rules

**Syntax Rules:**

**Variable assignment**
```
   Bash: VAR=$(command)

   PowerShell: $VAR = (command)
```

**Variable reference**
```
   Bash: $VAR

   PowerShell: $VAR
```

**Output/print**
```
   Bash: echo $VAR

   PowerShell: Write-Output $VAR (though just typing $VAR also works)
```
---

1. **Get the VPC ID**

Bash:
```bash
   VPC_ID=$(aws ec2 describe-vpcs --query "Vpcs[0].VpcId" --output text)
```
```bash
   echo $VPC_ID
```

PowerShell
```powershell
   $VPC_ID = (aws ec2 describe-vpcs --query "Vpcs[0].VpcId" --output text)
```
```powershell
   $VPC_ID
```

2. **Create the security group**
 
**Linux/Unix**:

Example:

```bash
   SG_JSON=$(aws ec2 create-security-group --group-name MySecurityGroup --description "My security group" --vpc-id $VPC_ID)
```

`Bash`: It requires jq to parse JSON.

   - You’re expected to write or run a Bash script (shell script).

   - That script will need to handle JSON data.

   - Since Bash alone cannot parse JSON reliably, the script will depend on the tool jq
    (a lightweight JSON processor) to extract, filter, and manipulate values from JSON.
```bash
   SG_ID=$(echo $SG_JSON | jq -r '.GroupId')
```

```bash
   echo $SG_ID
```

**PowerShell**

Example:
```powershell

   $create = aws ec2 create-security-group --group-name MySecurityGroup --description "My security group" --vpc-id $VPC_ID --output json
```

```powershell
   $SG_ID = (ConvertFrom-Json $create).GroupId
```
```powershell
   $SG_ID
```

3. **Add ingress rules**

**SSH(port 22)**
```bash
   aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 22 --cidr 0.0.0.0/0
```
**HTTP (port 80)**
```bash
   aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 80 --cidr 0.0.0.0/0
```

**MYSQL From Custom Source**
```bash
aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 3306 --cidr X.X.X.X/32
```
```
   --protocol tcp: MySQL runs over TCP.

   --port 3306: default MySQL port.

   --cidr X.X.X.X/32: replace X.X.X.X with the public IP address you want to allow access from.

      - /32 means just that single IP.

         -Example: 203.0.113.25/32

   If you want to allow a range of IPs instead of a single one: --cidr 192.168.1.0/24
            This would allow all IPs in the 192.168.1.x range.
```

**SMTP From Anywhere IPV4**
```bash
aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 25 --cidr 0.0.0.0/0
```
```
   --protocol tcp: SMTP uses TCP.

   --port 25: Default SMTP port.

   --cidr 0.0.0.0/0: Allows all IPv4 addresses.
```

**SMTP From Anywhere IPV6**
```bash
aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 25 --cidr ::/0
```
```
   --protocol tcp: SMTP uses TCP.

   --port 25: Default SMTP port.

   --cidr ::/0: Allows all IPv6 addresses.
```

**All Traffic From All Sources**
```bash
aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol -1 --port -1 --cidr 0.0.0.0/0
```
```
   --protocol -1: means all protocols (TCP, UDP, ICMP, etc.).

   --port -1:  means all ports.

   --cidr 0.0.0.0/0: means all IPv4 addresses (worldwide access).
```


4. **List & Delete**
**List**
```bash
   aws ec2 describe-security-groups --group-ids $SG_ID
```
**Delete**
```bash
   aws ec2 delete-security-group --group-id $SG_ID
```
---

## Troubleshooting & common errors

- **`aws: command not found` / `'aws' is not recognized`**: Ensure AWS CLI binary is installed and on PATH. On Windows, add `C:\Program Files\Amazon\AWSCLIV2\bin\` to PATH and restart the terminal.

- **Permissions errors with `.pem` files**: `chmod 400 MyKey.pem` (Linux/macOS). On Windows, use `icacls` to remove inheritance and restrict it to your user.

- **Credential/AccessDenied**: Validate credentials, check IAM policy, or use assumed roles/MFA as required.

- **SSL/curl download errors**: Ensure `curl` is installed and CA certs present.

- **Could not connect to the endpoint URL**: Verify network, region, and proxy settings. Configure `HTTP_PROXY` / `HTTPS_PROXY` for corporate proxies.

---

## Commonly used commands:

---

**1. General Commands**

```bash
   aws configure                      #Set up AWS credentials and default region
```
```
   aws sts get-caller-identity        #Verify current AWS identity
```
```
   aws help                           #Get help for AWS CLI
```
```
   aws <service> help                 #Get help for a specific service
```

---

**2. EC2 (Compute)**

List EC2 instances:
```bash
   aws ec2 describe-instances

```
   Start an instance:
```
      aws ec2 start-instances --instance-ids i-1234567890abcdef0
```
   Stop an instance:
```
      aws ec2 stop-instances --instance-ids i-1234567890abcdef0
```
   Terminate an instance:
```
      aws ec2 terminate-instances --instance-ids i-1234567890abcdef0
```

**Security Group rules**

```
aws ec2 describe-security-groups
```
```
aws ec2 authorize-security-group-ingress --group-id sg-`xxxx` --protocol tcp --port 22 --cidr 0.0.0.0/0
```
```
aws ec2 revoke-security-group-ingress --group-id sg-`xxxx` --protocol tcp --port 22 --cidr 0.0.0.0/0
```

---

**3. S3 (Storage)**

List buckets:
```bash
   aws s3 ls
```

Upload files
```
   aws s3 cp localfile.txt s3://my-bucket/
```
Download files
```
   aws s3 cp s3://my-bucket/remotefile.txt ./ 
```

Sync local folder with bucket
```
   aws s3 sync ./local-folder s3://my-bucket/
```

Sync bucket with local folder
```
   aws s3 sync s3://my-bucket/ ./local-folder
```

---

**4. IAM (Users/Roles/Policies)**

List users
```bash
   aws iam list-users
```

Create a new user
```
   aws iam create-user --user-name David
```

Attach policy to user
```
aws iam attach-user-policy --user-name David --policy-arn                      arn:aws:iam::aws:policy/AdministratorAccess
```

---

**5. CloudFormation**

Deploy a stack
```bash
   aws cloudformation deploy --template-file template.yaml --stack-name MyStack
```

Describe stack
```
   aws cloudformation describe-stacks --stack-name MyStack
```

---

**6. Lambda**

List functions
```bash
   aws lambda list-functions
```

Invoke a function
```
   aws lambda invoke --function-name MyFunction output.json
```

---

**7. RDS (Databases)**

List databases
```bash
aws rds describe-db-instances
```

Create snapshot
```
aws rds create-db-snapshot --db-instance-identifier mydb --db-snapshot-identifier mydb-snapshot
```

---

**8. CloudWatch/Logs**

List log groups
```bash
   aws logs describe-log-groups
```

Get log events
```
   aws logs get-log-events --log-group-name my-log-group --log-stream-name my-log-stream
```

---
Best Practices:

- Use named profiles and avoid storing long-lived credentials in source control.
  
- Prefer role assumption with least privilege.
  
- Rotate access keys regularly and delete unused keys.

---
  
