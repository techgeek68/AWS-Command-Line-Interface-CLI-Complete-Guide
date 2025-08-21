# 1. AWS Management Console Access Guide

**Audience:** New Cloud Engineers  
**Environment:** Production & Development  
**Region:** Example: us-east-1  
**Operating System:** Windows `PowerShell`, macOS `Terminal`, Linux `Terminal`

---

## 1. Overview

The AWS Management Console is the browser-based UI for interacting with AWS services.

- **Development/Learner Use:** Suitable for exploration and manual tasks.
- **Production Use:** Restrict access to AWS IAM Identity Center (Single Sign-On). Require Multi-Factor Authentication (MFA) and least-privilege roles. Never use the root account for daily operations.

---

## 2. Prerequisites Checklist

- AWS Account ID, Name, Organization/Organizational Unit (`<YOUR_AWS_ACCOUNT_ID>`, `<YOUR_ACCOUNT_NAME>`, `<YOUR_ORG>/<YOUR_OU>`)
- AWS IAM Identity Center (Single Sign-On) portal URL (`<SSO_PORTAL_URL>`) if enforced
- MFA device (authenticator app or hardware key)
- IAM or Single Sign-On user provisioned

---

## 3. Security Considerations

- **Enable MFA for all users** (required for production)
- **Enforce IAM Identity Center (Single Sign-On) for access**; disable IAM user console login in production
- **Never use the root account** for daily operations
- Assign **least-privilege roles**
- **Audit console logins regularly**

---

## 4. Step-by-Step Instructions

### 4.1. Create IAM User (Development/Learner Only)

> Use IAM Identity Center for production!

1. Log in at [AWS Console](https://console.aws.amazon.com/) with the root account (only for initial setup).
2. Go to **IAM > Users > Add user**.
3. Enter username: `<YOUR_USERNAME>`
4. Enable AWS Management Console access and set password (require reset).
5. Assign user to group with required permissions (e.g., `ReadOnlyAccess` for learners).
6. Click **Next**, review, and **Create user**.
7. Save login link and credentials securely.

### 4.2. Enforce Single Sign-On (Production)

1. Set up [IAM Identity Center (Single Sign-On)](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html).
2. Choose Identity Provider (e.g., Okta, Azure AD).
3. **Disable IAM user console login**:
   - IAM > Users > `<username>` > Security credentials
   - Click **Deactivate Console access**
4. Confirm only SSO users can log in.

### 4.3. Require Multi-Factor Authentication

1. IAM > Users > `<username>` > Security credentials
2. Click **Assign MFA device**
3. Select **Virtual MFA device** (e.g., Authy, Google Authenticator)
4. Scan QR code, enter two consecutive codes, and **Activate**

### 4.4. Assume Role via Console

1. Log in via AWS Console or SSO portal.
2. Click your account name (top right) > **Switch Role**
3. Enter **Account ID**: `<YOUR_AWS_ACCOUNT_ID>`
4. Enter **Role Name**: `<ROLE_NAME>`
5. Enter **Display Name/Color** (optional)
6. Click **Switch Role**

---

## 5. Verification Steps

- Log in and check your username/role at the top right.
- Attempt to access a resource based on assigned permissions (e.g., S3 bucket).
- Confirm MFA prompt at login.

---

## 6. Common Pitfalls & Troubleshooting

- **Permission Denied:**  
  - Check IAM or SSO group/permission sets.
- **MFA Device Not Recognized:**  
  - Re-sync or re-enroll MFA device.
- **Cannot Switch Role:**  
  - Confirm role trust relationships and permissions.

---

## 7. Cleanup Steps

- Remove unused IAM users/roles
- Detach unnecessary permissions
- Delete test resources

---

## 8. Cost Notes

- No charges for IAM users or groups; charges may apply for resources created via console

---

## 9. Best Practices & Production Notes

- Use Single Sign-On for all console logins in production
- Remove console access for IAM users
- Require MFA everywhere
- Audit console logins regularly

---

## 10. Reference Minimal IAM Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": "s3:ListAllMyBuckets",
    "Resource": "*"
  }]
}
```
*Allows the user to list S3 buckets. Restrict further in production.*

[Learn more: AWS IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)

---

## Further Reading

- [AWS Management Console](https://aws.amazon.com/console/)
- [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html)

---
