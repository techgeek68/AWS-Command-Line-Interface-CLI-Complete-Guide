# AWS Account Creation & Free Tier Guidance

This guide provides step-by-step instructions for creating an AWS account via the AWS Management Console, including details on AWS Free Tier benefits and monitoring usage to avoid unexpected charges.

---

## Table of Contents

- [Creating an AWS Account](#creating-an-aws-account)
  - [1. Navigate to the AWS Sign-Up Page](#1-navigate-to-the-aws-sign-up-page)
  - [2. Enter Account and Contact Information](#2-enter-account-and-contact-information)
  - [3. Add Payment Details & Complete Identity Verification](#3-add-payment-details--complete-identity-verification)
  - [4. Choose the Free Basic Support Plan](#4-choose-the-free-basic-support-plan)
  - [5. Log in to the AWS Management Console](#5-log-in-to-the-aws-management-console)
- [How the AWS Free Tier Works](#how-the-aws-free-tier-works)
  - [Free Tier Types](#free-tier-types)
  - [Common Limits](#common-limits)
  - [Monitoring Free Tier Usage](#monitoring-free-tier-usage)
- [Helpful Links](#helpful-links)

---

## Creating an AWS Account

### 1. Navigate to the AWS Sign-Up Page

- Go to [aws.amazon.com](https://aws.amazon.com).
- Click **Create an AWS Account** at the top-right.
- If you have an Amazon.com account, you can use those credentials or create a new account.

### 2. Enter Account and Contact Information

- **Account Name**: Enter your preferred account name.
- **Email Address**: Provide a valid email address.
- **Password**: Create a strong password.
- **Contact Information**: Enter your name, company (if applicable), and phone number.
- **Country/Region & Address**: Fill in your location and mailing address.

### 3. Add Payment Details & Complete Identity Verification

- **Payment Method**: Enter a credit/debit card (AWS may make a small, temporary charge for verification).
- **Identity Verification**:
  - Enter your mobile number.
  - Receive a code via SMS or voice call and enter it.

### 4. Choose the Free Basic Support Plan

- AWS will prompt you to select a support plan.
- Choose **Basic Support – Free**.

### 5. Log in to the AWS Management Console

- Go to [console.aws.amazon.com](https://console.aws.amazon.com/).
- Log in with your registered email and password (root user).
- Explore the AWS Console dashboard.

---

## How the AWS Free Tier Works

### Free Tier Types

1. **12-Month Free Tier**
   - For new accounts, select services are free for the first 12 months.
   - Example limits:
     - **Amazon EC2**: 750 hours/month of t2.micro or t3.micro instances (Linux/Windows).
     - **Amazon S3**: 5 GB storage, 20,000 GET, 2,000 PUT requests/month.
     - **Amazon RDS**: 750 hours/month of db.t2.micro or db.t3.micro, 20 GB storage.

2. **Always-Free Offers**
   - Certain services offer free usage indefinitely.
   - Example limits:
     - **AWS Lambda**: 1 million requests, 400,000 GB-seconds/month.
     - **Amazon DynamoDB**: 25 GB storage, 25 Write/Read Capacity Units.

3. **Short-Term Trials**
   - Free trials for specific services, typically a few days to months.

### Common Limits

| Service      | Free Tier Limit (per month)                  | Duration    |
|--------------|----------------------------------------------|-------------|
| EC2          | 750 hours of t2.micro/t3.micro               | 12 months   |
| S3           | 5 GB storage, 20,000 GET, 2,000 PUT requests | 12 months   |
| RDS          | 750 hours, 20 GB storage                     | 12 months   |
| Lambda       | 1M requests, 400,000 GB-seconds              | Always Free |
| DynamoDB     | 25 GB storage, 25 WCU, 25 RCU                | Always Free |

### Monitoring Free Tier Usage

- **Free Tier Dashboard**:  
  - Go to [AWS Billing Console](https://console.aws.amazon.com/billing/home).
  - Select **Free Tier** to view usage and alerts.

- **Billing Alerts**:  
  - Set up billing alerts using **AWS Budgets**.
  - Create a budget with a threshold (e.g., $1) and configure email/SNS alerts.

- **Best Practices**:
  - Check the Free Tier dashboard regularly.
  - Understand and track service limits.
  - Stop/terminate unused resources.
  - Delete unused storage.

---

## Helpful Links

- [AWS Free Tier Details](https://aws.amazon.com/free)
- [AWS Free Tier Usage Dashboard](https://console.aws.amazon.com/billing/home#/freetier)
- [AWS Budgets](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-create.html)

## Video Tutorials 
- [AWS Account Creation & Free Tier (Video Guide)](https://www.youtube.com/watch?v=CecVvOVOtuQ)

---

**Start building on AWS confidently and monitor usage to stay within Free Tier limits!**
