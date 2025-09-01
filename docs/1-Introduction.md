# Ways to Access AWS (Junior/Associate Cloud Engineers • Dev/Test • Production)

This guide is designed for **Entry-level cloud engineers** working in a **production** environment. It provides thorough, beginner-friendly, and security-focused instructions for accessing AWS via multiple methods, covering all essentials for a safe, reliable, and scalable setup.

---

## Comparison Table: AWS Access Methods

| Method                              | Ease   | Security | Automation | Best For Learner | Best For Prod |
|--------------------------------------|--------|----------|------------|------------------|--------------|
| AWS Management Console               | High   | Medium   | Low        | ✅               | ⚠️ (with Single Sign-On)   |
| AWS Command Line Interface v2        | Medium | High     | High       | ✅               | ✅           |
| Software Development Kit (Python/boto3) | Medium | High  | High       | ✅               | ✅           |
| AWS CloudShell                       | High   | High     | Medium     | ✅               | ✅           |
| Infrastructure as Code (CloudFormation)| Medium | High  | High       | ✅               | ✅           |
| Identity and Access Management Identity Center (Single Sign-On) | Medium | High     | High       | ⚠️               | ✅           |
| Systems Manager Session Manager      | Medium | High     | Medium     | ⚠️               | ✅           |
| Direct Application Programming Interface (Signature Version 4) | Low    | High     | High       | ⚠️               | ✅           |

---

## Inputs & Variables Used Throughout

- **AWS Account ID**: `<YOUR_AWS_ACCOUNT_ID>`

- **Account Name**: `<YOUR_ACCOUNT_NAME>`

- **Organization / Organizational Unit (OU)**: `<YOUR_ORG>/<YOUR_OU>`

- **Primary Region**: `<us-east-1 | us-west-2 | eu-central-1>`

- **Local Operating System**: `<Windows-PowerShell | macOS-Terminal | Linux-Terminal>`

- **Command Line Interface Profile Name**: `"prod"`

- **Identity Provider (SSO)**: `<Okta | Azure Active Directory | AWS IAM Identity Center>`

- **Authentication Method**: `<SSO | IAM Role | Access Keys | Service Account>`

- **Role to Assume**: `<AdministratorAccess | PowerUser | ReadOnly>`

- **Multi-Factor Authentication (MFA)**: `<Enabled | Optional | Disabled>`

- **Virtual Private Cloud (VPC) Access Pattern**: `<public/private, VPN, Direct Connect, Transit Gateway>`

- **Network Security Controls**: `<Security Groups, NACLs, Firewall, CIDR Allowlist>`

- **Audit / Logging Destination**: `<CloudWatch | S3 | Splunk | SIEM>`

- **Encryption / Key Management**: `<AWS KMS | HashiCorp Vault | HSM>`

- **Cost Center / Billing Tag**: `<project=alpha, team=infra, env=prod>`

- **Session Timeout / Token Lifetime**: `<1h | 8h | 12h | 24h>`

- **Support Contacts / PagerDuty Group**: `<team-name | escalation-policy>`

---
