# AWS Access Methods Guide

Structured, hands‑on notes, labs, and code examples showing multiple ways to access and interact with AWS:
- AWS Management Console workflow & navigation
- Foundational security setup (key pairs, security groups)
- AWS CLI v2 usage across core services
- CloudShell usage
- Multi‑language AWS SDK introductions (Python, Node.js, .NET, Java)
- Small runnable code samples (list regions, create key pair + security group, etc.)
- Cross‑cutting SDK topics

> NOTE: This README was generated from the currently retrievable repository contents. The content listing retrieved via the GitHub API may be incomplete (API pagination limit). Always consult the full repository tree for authoritative structure: https://github.com/techgeek68/aws-access-methods-guide/tree/master

---

## Repository Contents (Current Primary Files)

| Section | File |
|---------|------|
| 1. Introduction | [1-Introduction.md](1-Introduction.md) |
| 2. Account Creation & Free Tier Guidance | [2-Account-Creation-&-Free-Tier-Guidance.md](2-Account-Creation-%26-Free-Tier-Guidance.md) |
| 3.0 AWS Management Console – Accessing & Navigating | [3.0-aws-management-console-Accessing-Navigating.md](3.0-aws-management-console-Accessing-Navigating.md) |
| 3.01 Lab: Key Pairs (Console) | [3.01-Lab-key-pairs](3.01-Lab-key-pairs) |
| 3.02 Lab: Security Groups (Console) | [3.02-Lab-security-groups.md](3.02-Lab-security-groups.md) |
| 3.03 EC2 via Console | [3.03-MgtConsole-EC2.md](3.03-MgtConsole-EC2.md) |
| 4.0 AWS CLI v2 Overview | [4.0-aws-CLI-V2.md](4.0-aws-CLI-V2.md) |
| 4.01 CLI: Key Pairs | [4.01-awscli-KeyPairs.md](4.01-awscli-KeyPairs.md) |
| 4.02 CLI: Security Groups | [4.02-awscli-SecurityGroups.md](4.02-awscli-SecurityGroups.md) |
| 4.03 CLI: EC2 | [4.03-awscli-EC2.md](4.03-awscli-EC2.md) |
| 4.04 CLI: S3 | [4.04-awscli-S3.md](4.04-awscli-S3.md) |
| 4.05 CLI: IAM | [4.05-awscli-IAM.md](4.05-awscli-IAM.md) |
| 4.06 CLI: SSM | [4.06-awscli-SSM.md](4.06-awscli-SSM.md) |
| 4.07 CLI: CloudFormation | [4.07-awscli-CloudFormation.md](4.07-awscli-CloudFormation.md) |
| 4.08 CLI: RDS | [4.08-awscli-RDS.md](4.08-awscli-RDS.md) |
| 4.09 CLI: Lambda | [4.09-awscli-Lambda.md](4.09-awscli-Lambda.md) |
| 4.10 CLI: CloudWatch | [4.10-awscli-CloudWatch.md](4.10-awscli-CloudWatch.md) |
| 4.11 CLI: DynamoDB | [4.11--awscli-DynamoDB.md](4.11--awscli-DynamoDB.md) |
| 4.12 CLI: SNS | [4.12-aws-SNS.md](4.12-aws-SNS.md) |
| 4.13 CLI: SQS | [4.13-aws-SQS.md](4.13-aws-SQS.md) |
| 4.14 CLI: EKS | [4.14-awscli-EKS.md](4.14-awscli-EKS.md) |
| 4.15 CLI: ECR | [4.15-awscli-ECR.md](4.15-awscli-ECR.md) |
| 5.0 AWS CloudShell | [5.0-aws-CloudShell.md](5.0-aws-CloudShell.md) |
| 6.0 AWS SDK – Python | [6.0-awsSDK-Python.md](6.0-awsSDK-Python.md) |
| 6.0.1 Python Sample | [6.0.1-list-regions.py](6.0.1-list-regions.py) |
| 6.0.2 Python Sample (Create key pair & SG) | [6.0.2-create-key-sg.py](6.0.2-create-key-sg.py) |
| 6.01 AWS SDK – Node.js | [6.01-awsSDK-Nodejs.md](6.01-awsSDK-Nodejs.md) |
| 6.01.1 Node.js Sample | [6.01.1-list-regions.js](6.01.1-list-regions.js) |
| 6.01.2 Node.js Sample (Create key pair & SG) | [6.01.2-create-key-sg.mjs](6.01.2-create-key-sg.mjs) |
| 6.01.3 Node.js Sample Output | [6.01.3-list-regions.json](6.01.3-list-regions.json) |
| 6.02 AWS SDK – .NET | [6.02-awsSDK-dotNET.md](6.02-awsSDK-dotNET.md) |
| 6.02.1 .NET Sample | [6.02.1-list-regions.cs](6.02.1-list-regions.cs) |
| 6.02.3 Java Sample (naming anomaly) | [6.02.3-list-regions.java](6.02.3-list-regions.java) |
| 6.03 AWS SDK – Java | [6.03-awsSDK-Java.md](6.03-awsSDK-Java.md) |
| 6.04 AWS SDK – Cross Cutting Topics | [6.04-awsSDK-cross-cutting-topics.md](6.04-awsSDK-cross-cutting-topics.md) |

(Any additional files beyond the first 30 returned may not be listed here.)

---

## Purpose

Provide a progressive path for learners to:
1. Create or prepare an AWS account responsibly (Free Tier awareness)
2. Understand console navigation and essential EC2 networking primitives (key pairs, security groups)
3. Transition from console tasks to scripted and repeatable AWS CLI commands
4. Explore service operations across a breadth of core AWS services
5. Use AWS CloudShell for browser-based CLI access
6. Onboard to AWS SDK usage in multiple programming languages with small, consistent examples
7. Recognize cross‑cutting SDK themes (configuration, credentials, pagination, regions)

---

## Audience

- Students / self‑learners preparing for foundational AWS certifications
- Developers moving from ad-hoc console use to automation
- Instructors needing modular lab content
- Engineers comparing multilingual SDK usage patterns

---

## Prerequisites

- An AWS account (preferably a sandbox or training account)
- IAM user or federated role with the least privileges required for each lab
- AWS CLI v2 installed (for sections 4.x) if not using CloudShell
- Optional language runtimes:
  - Python 3.x & pip
  - Node.js 18+ (ES Modules enabled for .mjs sample)
  - .NET 6+ SDK
  - Java 11+ & Maven/Gradle (as needed)

---

## Recommended Learning Order

1. Read Introduction (1-Introduction.md)  
2. Complete account & Free Tier guidance (2-Account-Creation-&-Free-Tier-Guidance.md)  
3. Console fundamentals (3.0 + 3.01–3.03)  
4. CLI overview, then targeted service labs (4.0 → 4.01+ sequentially or pick services)  
5. CloudShell (5.0) to contrast local vs managed environment  
6. SDK language of choice (6.0 / 6.01 / 6.02 / 6.03)  
7. Cross-cutting SDK insights (6.04)  

---

## Code Sample Overview

All samples focus on:
- Region enumeration
- Creating basic security artifacts (key pair, security group)
- Demonstrating credential and region handling patterns

Example (Python list regions – 6.0.1-list-regions.py):
```bash
python3 6.0.1-list-regions.py
```

Example (Node.js list regions – 6.01.1-list-regions.js):
```bash
node 6.01.1-list-regions.js
```

Example (.NET list regions – 6.02.1-list-regions.cs):
```bash
dotnet script 6.02.1-list-regions.cs
```
(or include in a small console project)

Example (Java list regions – 6.02.3-list-regions.java):
```bash
javac 6.02.3-list-regions.java && java ListRegions
```
(Ensure class name matches source file content.)

---

## Credential & Configuration Notes

Most labs assume the standard AWS CLI credential/provider chain:
- Environment variables (AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY / AWS_SESSION_TOKEN)
- Profile in ~/.aws/credentials and ~/.aws/config
- CloudShell automatic role credentials
- SDK default provider chain behavior (documented per language in 6.04)

Tip: Avoid embedding long‑lived credentials directly in source. Prefer profiles or federation.

---

## File Naming Observations

- Mixed numbering styles (e.g., `4.11--awscli-DynamoDB.md` has a double hyphen).
- One file without a `.md` extension (`3.01-Lab-key-pairs`). Consider normalizing for consistency and automatic Markdown rendering.
- Java sample `6.02.3-list-regions.java` appears numerically grouped with the .NET section; consider moving under 6.03 or renaming.

These inconsistencies do not affect function, but standardization improves clarity.

---

## How to Contribute

1. Open an issue describing the proposed improvement (content addition, correction, or naming cleanup).
2. For new service sections: follow the existing pattern (intro, prerequisite IAM permissions, key commands, cleanup steps).
3. For new SDK examples: keep them minimal, readable, and parallel to existing region listing or simple resource creation tasks.
4. Ensure any resource‑creating lab includes a cleanup section.
5. Keep scope focused: This repository emphasizes *access methods & interaction patterns*, not deep architecture design.

Suggested Contribution Areas:
- Add missing cleanup instructions where absent
- Normalize filenames
- Provide diagrams (e.g., credential provider chain)
- Expand cross-cutting topics (6.04) with retry strategies or error handling examples

---

## Style & Conventions

- Use fenced code blocks with language hints (bash, json, python, javascript, csharp, java).
- Keep lines concise; prefer bullet lists for procedural steps.
- Explicitly call out region and resource name variables (e.g., `$REGION`, `$KEY_NAME`) in CLI labs.

---

## Known Gaps / Future Enhancements

(Only list what is evidenced or logically adjacent to the current scope)
- Additional SDK language examples (Go, Ruby, PHP) are not yet present
- Diagrammatic overview of credential chain
- Unified cleanup checklist across all service labs
- Optional Docker container for multi-language SDK environment

---

## Disclaimer

Labs may incur AWS charges if run outside the Free Tier or left undeleted. Follow the cleanup steps diligently.

---

## Quick Reference Links

- Full repository: https://github.com/techgeek68/aws-access-methods-guide
- AWS CLI Installation: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
- SDK Docs (multi-language): See per-language sections (6.x)

---

## Attribution / Maintainer

Maintainer: @techgeek68  

---

If anything in this README does not reflect recent changes, please open an issue—some files may not have been visible in the partial API listing used to assemble this summary.

Happy learning and automating!
