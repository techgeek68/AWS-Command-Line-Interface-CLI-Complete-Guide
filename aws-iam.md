# AWS CLI – IAM Guide

## Table of Contents
1. [Overview](#overview)
2. [Users](#1-users)
3. [Policies](#2-policies)
4. [Roles](#3-roles)
5. [Groups](#4-groups)
6. [Access Keys](#5-access-keys)
7. [Policy Evaluation Helpers](#6-policy-evaluation-helpers)
8. [Best Practices](#7-best-practices)
9. [Troubleshooting](#8-troubleshooting)

---

## Overview
AWS Identity and Access Management (IAM) governs authentication and authorization for users, groups, roles, and policies across AWS services. The CLI enables comprehensive management of identities and permission boundaries. This guide emphasizes security best practices, preferring roles with temporary credentials over long-lived user keys.

---

## 1. Users

### Create IAM User
````bash
aws iam create-user --user-name xxxxxxxx  # user input here (username)
````

### List All Users
````bash
aws iam list-users
````

### Get User Details
````bash
aws iam get-user --user-name xxxxxxxx  # user input here (username)
````

### Add User to Group
````bash
aws iam add-user-to-group \
  --group-name xxxxxxxx \  # user input here (group name)
  --user-name xxxxxxxx  # user input here (username)
````

### Remove User from Group
````bash
aws iam remove-user-from-group \
  --group-name xxxxxxxx \  # user input here (group name)
  --user-name xxxxxxxx  # user input here (username)
````

### Attach Policy to User
````bash
aws iam attach-user-policy \
  --user-name xxxxxxxx \  # user input here (username)
  --policy-arn xxxxxxxx  # user input here (policy ARN)
````

### Detach Policy from User
````bash
aws iam detach-user-policy \
  --user-name xxxxxxxx \  # user input here (username)
  --policy-arn xxxxxxxx  # user input here (policy ARN)
````

### List User's Attached Policies
````bash
aws iam list-attached-user-policies --user-name xxxxxxxx  # user input here (username)
````

### Delete IAM User
````bash
aws iam delete-user --user-name xxxxxxxx  # user input here (username)
````

### Create Login Profile (Console Access)
````bash
aws iam create-login-profile \
  --user-name xxxxxxxx \  # user input here (username)
  --password xxxxxxxx \  # user input here (password)
  --password-reset-required
````

### Enable MFA for User
````bash
aws iam enable-mfa-device \
  --user-name xxxxxxxx \  # user input here (username)
  --serial-number xxxxxxxx \  # user input here (MFA device ARN)
  --authentication-code-1 xxxxxxxx \  # user input here (first MFA code)
  --authentication-code-2 xxxxxxxx  # user input here (second MFA code)
````

---

## 2. Policies

### Create Managed Policy
````bash
aws iam create-policy \
  --policy-name xxxxxxxx \  # user input here (policy name)
  --policy-document file://xxxxxxxx  # user input here (path to policy JSON file)
````

### List Managed Policies
````bash
aws iam list-policies --scope Local
````

### Get Policy Details
````bash
aws iam get-policy --policy-arn xxxxxxxx  # user input here (policy ARN)
````

### Get Policy Version (Document)
````bash
aws iam get-policy-version \
  --policy-arn xxxxxxxx \  # user input here (policy ARN)
  --version-id xxxxxxxx  # user input here (version ID, often 'v1')
````

### Create New Policy Version
````bash
aws iam create-policy-version \
  --policy-arn xxxxxxxx \  # user input here (policy ARN)
  --policy-document file://xxxxxxxx \  # user input here (path to updated policy JSON)
  --set-as-default
````

### Delete Policy Version
````bash
aws iam delete-policy-version \
  --policy-arn xxxxxxxx \  # user input here (policy ARN)
  --version-id xxxxxxxx  # user input here (version ID)
````

### Delete Managed Policy
````bash
aws iam delete-policy --policy-arn xxxxxxxx  # user input here (policy ARN)
````

### Example Policy Document (S3 Read-Only)
````json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::xxxxxxxx",
        "arn:aws:s3:::xxxxxxxx/*"
      ]
    }
  ]
}
````

---

## 3. Roles

### Create IAM Role
````bash
aws iam create-role \
  --role-name xxxxxxxx \  # user input here (role name)
  --assume-role-policy-document file://xxxxxxxx  # user input here (path to trust policy JSON)
````

### List All Roles
````bash
aws iam list-roles
````

### Get Role Details
````bash
aws iam get-role --role-name xxxxxxxx  # user input here (role name)
````

### Attach Policy to Role
````bash
aws iam attach-role-policy \
  --role-name xxxxxxxx \  # user input here (role name)
  --policy-arn xxxxxxxx  # user input here (policy ARN)
````

### Detach Policy from Role
````bash
aws iam detach-role-policy \
  --role-name xxxxxxxx \  # user input here (role name)
  --policy-arn xxxxxxxx  # user input here (policy ARN)
````

### List Role's Attached Policies
````bash
aws iam list-attached-role-policies --role-name xxxxxxxx  # user input here (role name)
````

### Update Role's Trust Policy
````bash
aws iam update-assume-role-policy \
  --role-name xxxxxxxx \  # user input here (role name)
  --policy-document file://xxxxxxxx  # user input here (path to trust policy JSON)
````

### Create Instance Profile for EC2
````bash
aws iam create-instance-profile --instance-profile-name xxxxxxxx  # user input here (instance profile name)
````

### Add Role to Instance Profile
````bash
aws iam add-role-to-instance-profile \
  --instance-profile-name xxxxxxxx \  # user input here (instance profile name)
  --role-name xxxxxxxx  # user input here (role name)
````

### Delete Role
````bash
aws iam delete-role --role-name xxxxxxxx  # user input here (role name)
````

### Example Trust Policy (EC2)
````json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
````

### Example Trust Policy (Cross-Account with MFA)
````json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::xxxxxxxx:user/xxxxxxxx"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "Bool": {
          "aws:MultiFactorAuthPresent": "true"
        }
      }
    }
  ]
}
````

---

## 4. Groups

### Create Group
````bash
aws iam create-group --group-name xxxxxxxx  # user input here (group name)
````

### List All Groups
````bash
aws iam list-groups
````

### Get Group Details
````bash
aws iam get-group --group-name xxxxxxxx  # user input here (group name)
````

### Attach Policy to Group
````bash
aws iam attach-group-policy \
  --group-name xxxxxxxx \  # user input here (group name)
  --policy-arn xxxxxxxx  # user input here (policy ARN)
````

### Detach Policy from Group
````bash
aws iam detach-group-policy \
  --group-name xxxxxxxx \  # user input here (group name)
  --policy-arn xxxxxxxx  # user input here (policy ARN)
````

### Delete Group
````bash
aws iam delete-group --group-name xxxxxxxx  # user input here (group name)
````

---

## 5. Access Keys

### Create Access Key for User
````bash
aws iam create-access-key --user-name xxxxxxxx  # user input here (username)
````

### List User's Access Keys
````bash
aws iam list-access-keys --user-name xxxxxxxx  # user input here (username)
````

### Update Access Key Status (Activate/Deactivate)
````bash
aws iam update-access-key \
  --user-name xxxxxxxx \  # user input here (username)
  --access-key-id xxxxxxxx \  # user input here (access key ID)
  --status xxxxxxxx  # user input here (Active or Inactive)
````

### Delete Access Key
````bash
aws iam delete-access-key \
  --user-name xxxxxxxx \  # user input here (username)
  --access-key-id xxxxxxxx  # user input here (access key ID)
````

### Rotate Access Keys (Safe Process)
1. Create new access key
2. Update applications with new key  
3. Test applications
4. Deactivate old key
5. Test again
6. Delete old key

````bash
# Step 1: Create new key
aws iam create-access-key --user-name xxxxxxxx  # user input here (username)

# Step 4: Deactivate old key (after testing)
aws iam update-access-key --user-name xxxxxxxx --access-key-id xxxxxxxx --status Inactive  # user input here (username, old access key ID)

# Step 6: Delete old key (after final testing)
aws iam delete-access-key --user-name xxxxxxxx --access-key-id xxxxxxxx  # user input here (username, old access key ID)
````

---

## 6. Policy Evaluation Helpers

### Simulate Policy (What actions can a user perform?)
````bash
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::xxxxxxxx:user/xxxxxxxx \  # user input here (account ID, username)
  --action-names xxxxxxxx \  # user input here (action to test, e.g., s3:GetObject)
  --resource-arns xxxxxxxx  # user input here (resource ARN to test against)
````

### List Entities for Policy (Who has this policy?)
````bash
aws iam list-entities-for-policy --policy-arn xxxxxxxx  # user input here (policy ARN)
````

### Generate Credential Report
````bash
aws iam generate-credential-report
aws iam get-credential-report
````

### Get Account Summary
````bash
aws iam get-account-summary
````

### List Account Aliases
````bash
aws iam list-account-aliases
````

### Check Policy Syntax (Local validation)
Use tools like:
- AWS Policy Generator
- IAM Policy Simulator (Console)
- `cfn-lint` for CloudFormation IAM resources

---

## 7. Best Practices

- **Prefer roles with STS** over long-lived access keys whenever possible
- **Enforce MFA** using condition keys in policies for sensitive operations
- **Apply principle of least privilege** from the start; grant minimal required permissions
- **Rotate access keys regularly** and minimize the number of concurrent active keys per user
- **Use permission boundaries and SCPs** for additional guardrails in complex environments
- **Tag IAM resources** appropriately (e.g., `Owner`, `Environment`, `Purpose`)
- **Monitor IAM activity** with CloudTrail and set up alerts for suspicious activities
- **Use AWS managed policies** when they meet your requirements instead of creating custom ones
- **Implement separation of duties** with different roles for different functions
- **Regularly audit permissions** using access analyzer and credential reports
- **Use temporary credentials** (STS) for applications and cross-account access
- **Avoid embedding credentials** in code; use IAM roles for applications

---

## 8. Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| **AccessDenied error** | Missing action permissions or explicit deny | Review IAM policies, SCPs, and permission boundaries |
| **Cannot delete user** | User has attached resources | Remove access keys, policies, groups, login profile, and MFA devices |
| **AssumeRole fails** | Trust policy doesn't allow principal | Update role's trust policy to include correct principal |
| **Policy document too large** | Policy exceeds size limits | Split into multiple smaller policies and attach separately |
| **MFA required error** | Conditional policy requires MFA | Use `get-session-token` or `assume-role` with MFA |
| **Cannot attach policy** | Policy doesn't exist or wrong ARN | Verify policy ARN and that policy exists in account |
| **Cross-account access denied** | Missing trust relationship | Configure trust policy to allow cross-account access |
| **Permission boundary blocks action** | Boundary policy too restrictive | Review and adjust permission boundary if necessary |
| **Policy simulation shows deny** | Conflicting policies or conditions | Review all applicable policies for conflicts |

### Debugging Commands

Check what actions are explicitly denied:
````bash
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::xxxxxxxx:user/xxxxxxxx \  # user input here (account ID, username)
  --action-names "s3:*" \
  --resource-arns "*"
````

List all policy versions:
````bash
aws iam list-policy-versions --policy-arn xxxxxxxx  # user input here (policy ARN)
````

Get user's effective permissions:
````bash
aws iam get-user-policy \
  --user-name xxxxxxxx \  # user input here (username)
  --policy-name xxxxxxxx  # user input here (inline policy name)
````

Check role trust relationships:
````bash
aws iam get-role --role-name xxxxxxxx --query 'Role.AssumeRolePolicyDocument'  # user input here (role name)
````

---