# AWS Access Methods Guide

A comprehensive, security-focused guide for accessing and managing AWS services, designed for new cloud engineers working in production environments.

## 📚 Documentation Structure

This repository provides modular documentation covering multiple AWS access methods with detailed, production-ready examples and security best practices.

### Core AWS CLI Documentation

- **[AWS CLI Guide](aws_cli_guide.md)** - Complete installation, configuration, authentication, and troubleshooting guide for AWS CLI v2

### Service-Specific CLI Guides

Each service guide includes overview, key commands, cross-platform examples, best practices, and troubleshooting:

- **[AWS EC2 CLI Guide](aws-ec2.md)** - Instance lifecycle, key pairs, security groups, SSH access
- **[AWS S3 CLI Guide](aws-s3.md)** - Bucket operations, object management, sync, presigned URLs  
- **[AWS IAM CLI Guide](aws-iam.md)** - Users, roles, policies, access keys, permission management
- **[AWS CloudFormation CLI Guide](aws-cloudformation.md)** - Stack deployment, change sets, drift detection
- **[AWS Lambda CLI Guide](aws-lambda.md)** - Function management, invocation, versions, environment variables
- **[AWS RDS CLI Guide](aws-rds.md)** - Database instances, snapshots, parameter groups, monitoring
- **[AWS CloudWatch CLI Guide](aws-cloudwatch.md)** - Logs, metrics, alarms, insights queries

### Additional Access Methods

- **[Introduction to AWS Access Methods](01-Intro-Ways-to-Access-AWS.md)** - Comparison of different ways to access AWS
- **[AWS Account Creation & Free Tier](02-AWS-Account-Creation-&-Free-Tier-Guidance.md)** - Getting started with AWS
- **[AWS Management Console Guide](03-AWS-Management-Console.md)** - Web console access and usage
- **[Management Console EC2 Guide](AWS-ManagementConsole-EC2.md)** - EC2 management via web console

## 🎯 Documentation Philosophy

### Modular Design
Each service has its own dedicated guide, making it easy to find relevant information without navigating through monolithic documentation.

### Production-Ready Focus
All examples include:
- Security best practices and least privilege principles
- Cross-platform compatibility (Linux, macOS, Windows)
- Error handling and troubleshooting guidance
- Real-world scenarios and edge cases

### Consistent Format
Every service guide follows the same structure:
1. **Overview** - Service introduction and CLI interaction model
2. **Core Operations** - Most frequently used commands with examples
3. **Cross-Platform Examples** - Platform-specific syntax where relevant
4. **Best Practices** - Security, cost optimization, and operational guidance
5. **Troubleshooting** - Common issues, causes, and solutions

### Security-First Approach
- Emphasis on IAM roles and temporary credentials over long-lived access keys
- MFA enforcement examples and conditional policies
- Network security considerations and VPC configurations
- Encryption at rest and in transit examples

## 🔧 Command Format Standards

All code examples follow consistent formatting:

### Placeholder Convention
````bash
aws service command --parameter xxxxxxxx  # user input here (description of what to enter)
````

### Syntax Highlighting
- `bash` for Linux/macOS commands
- `powershell` for Windows PowerShell
- `bat` for Windows Command Prompt  
- `json` for JSON configuration files
- `ini` for configuration files
- `yaml` for CloudFormation templates

### Cross-Platform Support
Where commands differ between operating systems, separate examples are provided for:
- Linux/macOS (bash)
- Windows PowerShell
- Windows Command Prompt

## 🚀 Getting Started

### For New AWS Users
1. Start with [AWS Account Creation](02-AWS-Account-Creation-&-Free-Tier-Guidance.md)
2. Review [Introduction to Access Methods](01-Intro-Ways-to-Access-AWS.md)
3. Follow the [AWS CLI Guide](aws_cli_guide.md) for command-line setup

### For CLI Users
1. Install and configure AWS CLI using the [AWS CLI Guide](aws_cli_guide.md)
2. Choose the relevant service guide for your specific needs
3. Follow security best practices in each service guide

### For Console Users
1. Review the [AWS Management Console Guide](03-AWS-Management-Console.md)
2. Use [Management Console EC2 Guide](AWS-ManagementConsole-EC2.md) for EC2-specific operations

## 📋 Quick Reference

### Core CLI Setup
````bash
# Install AWS CLI (see full guide for platform-specific instructions)
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip && sudo ./aws/install

# Configure with profiles
aws configure --profile production
aws configure --profile development

# Verify setup
aws sts get-caller-identity --profile production
````

### Essential Commands by Service

**EC2:**
````bash
aws ec2 describe-instances
aws ec2 run-instances --image-id ami-xxx --instance-type t3.micro
aws ec2 stop-instances --instance-ids i-xxx
````

**S3:**
````bash
aws s3 ls
aws s3 cp file.txt s3://my-bucket/
aws s3 sync ./directory s3://my-bucket/prefix/
````

**IAM:**
````bash
aws iam list-users
aws iam create-role --role-name MyRole --assume-role-policy-document file://trust-policy.json
aws sts assume-role --role-arn arn:aws:iam::123456789012:role/MyRole --role-session-name MySession
````

## 🔒 Security Considerations

### Authentication Priority
1. **IAM Roles with STS** (recommended for applications and cross-account access)
2. **IAM Identity Center (SSO)** for human users
3. **Temporary credentials with MFA** for elevated access
4. **Long-lived access keys** only when absolutely necessary

### Network Security
- Use VPC endpoints for AWS service access within VPCs
- Implement least privilege security group rules
- Enable VPC Flow Logs for network monitoring
- Consider AWS PrivateLink for sensitive workloads

### Data Protection
- Enable encryption at rest for all data stores
- Use KMS for key management and rotation
- Implement encryption in transit (TLS/SSL)
- Regular backup and disaster recovery testing

## 🛠 Contributing

This documentation is designed to be:
- **Accurate** - All examples are tested and verified
- **Complete** - Covers common use cases and edge cases
- **Secure** - Follows AWS security best practices
- **Accessible** - Clear examples for users of all skill levels

## 📝 License

This guide is provided for educational and operational use. All AWS service names and functionality descriptions are based on publicly available AWS documentation.

## 🆘 Support

For AWS service-specific support:
- AWS Support (for account holders)
- AWS Forums and Community
- AWS Documentation
- AWS re:Post

For documentation issues or improvements, please refer to the troubleshooting sections in each guide or consult AWS official documentation.

---

*Last updated: January 2025*