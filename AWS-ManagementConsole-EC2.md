# 2. Creating an Amazon EC2 Instance Using the AWS Management Console

This guide continues with a comprehensive walkthrough for launching your first Amazon EC2 instance using the AWS Management Console. It covers every step from signing in to AWS to connecting to your running instance.

---

## Table of Contents

1. [Sign Into AWS Management Console](#step-1-sign-into-aws-management-console)
2. [Navigate to EC2 Dashboard](#step-2-navigate-to-ec2-dashboard)
3. [Launch Instance Wizard](#step-3-launch-instance-wizard)
4. [Choose an Amazon Machine Image (AMI)](#step-4-choose-an-amazon-machine-image-ami)
5. [Choose an Instance Type](#step-5-choose-an-instance-type)
6. [Configure Instance Details](#step-6-configure-instance-details)
7. [Add Storage](#step-7-add-storage)
8. [Add Tags (Optional)](#step-8-add-tags-optional)
9. [Configure Security Group](#step-9-configure-security-group)
10. [Create or Select a Key Pair](#step-10-create-or-select-a-key-pair)
11. [Review and Launch Instance](#step-11-review-and-launch-instance)
12. [Connect to Your Instance](#step-12-connect-to-your-instance)

---

## Step 1: Sign Into AWS Management Console

1. Go to [https://aws.amazon.com/](https://aws.amazon.com/).
2. Click **Sign In to the Console**.
3. Enter your AWS account credentials (email/username and password).
4. Click **Sign In**.

---

## Step 2: Navigate to EC2 Dashboard

1. In the AWS Management Console, type `EC2` in the search bar at the top.
2. Click on **EC2** from the dropdown suggestions.
3. You will be redirected to the EC2 Dashboard.

---

## Step 3: Launch Instance Wizard

1. On the EC2 Dashboard, click the orange **Launch Instance** button.
2. The **Launch an instance** wizard opens.

---

## Step 4: Choose an Amazon Machine Image (AMI)

1. Browse the list of available AMIs (Amazon Machine Images).
   - Common choices: **Amazon Linux**, **Ubuntu**, **Red Hat**, **Windows Server**, etc.
2. To select an AMI:
   - Click **Select** next to your desired AMI.
   - You may filter or search for specific AMI types, architecture, or features.
3. Review the AMI details before continuing.

---

## Step 5: Choose an Instance Type

1. Select the desired instance type (e.g., `t2.micro` for free tier).
2. Review vCPU, memory, network performance, and pricing.
3. Click **Next: Configure Instance Details**.

---

## Step 6: Configure Instance Details

1. Set the **Number of instances** (usually 1 for beginners).
2. Choose a **Network** (VPC). Default VPC is selected if you haven’t created one.
3. Choose a **Subnet** (availability zone).
4. Decide if you want to enable **Auto-assign Public IP** (recommended for public access).
5. Configure any **Advanced Details** as required (IAM role, monitoring, etc.).
6. Click **Next: Add Storage**.

---

## Step 7: Add Storage

1. Review the default root volume size and type.
2. To add more storage:
   - Click **Add New Volume**.
   - Specify volume type, size, and other options.
3. When finished, click **Next: Add Tags**.

---

## Step 8: Add Tags (Optional)

1. Click **Add Tag**.
2. Enter a **Key** (e.g., `Name`) and a **Value** (e.g., `MyFirstEC2`).
3. Tags help organize and identify your instances.
4. Click **Next: Configure Security Group**.

---

## Step 9: Configure Security Group

1. Choose **Create a new security group** or **Select an existing security group**.
2. Set inbound rules to allow traffic:
   - For SSH (Linux): Type = `SSH`, Protocol = `TCP`, Port Range = `22`, Source = `My IP` (recommended) or `Anywhere`.
   - For RDP (Windows): Type = `RDP`, Protocol = `TCP`, Port Range = `3389`, Source = `My IP` or `Anywhere`.
   - Add other rules as needed (HTTP, HTTPS).
3. Click **Review and Launch**.

---

## Step 10: Create or Select a Key Pair

1. When prompted, select an existing key pair **or** create a new one:
   - To create a new key pair:  
     a. Enter a key pair name.  
     b. Click **Create key pair**.  
     c. Download the `.pem` (Linux/Mac) or `.ppk` (Windows, for PuTTY) file and store it securely.
2. You **must** have access to the private key file to connect to your instance.

---

## Step 11: Review and Launch Instance

1. Review all configuration and settings.
2. Click **Launch**.
3. Select a key pair (or confirm you have the private key file).
4. Click **Launch Instances**.
5. Click **View Instances** to go to the Instances page.
6. Wait for the instance state to show **running**.

---

## Step 12: Connect to Your Instance

### For Linux Instances (SSH):

1. Select your instance from the Instances list.
2. Click **Connect** (top right).
3. Copy the example SSH command, which looks like:  
   ```
   ssh -i /path/to/your-key.pem ec2-user@<Public-IP-address>
   ```
4. Open your terminal and paste the command.
5. If you get a permission denied error, ensure your `.pem` file is read-only:
   ```
   chmod 400 /path/to/your-key.pem
   ```
6. Connect and you will have shell access to your instance.

---

### For Windows Instances (RDP):

**Step-by-Step Instructions:**

1. **Get Your Instance's Public DNS/IPv4 Address**
   - In the EC2 Dashboard, select your Windows instance.
   - In the lower panel, copy the **Public IPv4 DNS** or **Public IPv4 address**.

2. **Retrieve the Administrator Password**
   - With your instance selected, click the **Connect** button at the top.
   - Go to the **RDP client** tab.
   - Click **Get Password**.
   - Upload your private key file (`.pem`) that you used when launching the instance.
   - Click **Decrypt Password**.
   - Copy the **Administrator password** that is revealed.

3. **Download the RDP File**
   - Click **Download Remote Desktop File** on the Connect dialog.
   - Save the `.rdp` file to your computer.

4. **Open Remote Desktop Connection**
   - Double-click the downloaded `.rdp` file, or
   - Open the Windows **Start menu**, type `Remote Desktop Connection`, and launch it.
   - Paste the **Public DNS** or **Public IP** if prompted.

5. **Enter Credentials**
   - When prompted for username, enter: `Administrator`
   - Paste the decrypted password from step 2.

6. **Accept Security Certificate Warning**
   - A certificate warning may appear; click **Yes** to continue.

7. **Connect and Use Your Instance**
   - You should now see the Windows desktop of your EC2 instance.
   - Proceed to install software, configure settings, or perform other tasks as needed.

---

### Additional Tips for Windows EC2 Connections

- If connection fails, ensure your security group allows inbound TCP 3389 from your IP.
- If you lose your password, you must stop the instance, detach the volume, and recover the password with another instance (advanced).
- Always close Remote Desktop sessions and shut down your instance when done to avoid unnecessary costs.

---

## Additional Notes

- **Security**: Never share your key pair (.pem or .ppk) with anyone.
- **Billing**: Running EC2 instances may incur costs. Terminate instances when not in use.
- **Regions**: Make sure you are operating in the correct AWS region.

---

**Congratulations!** You have successfully launched and connected to your Amazon EC2 instance using the AWS Management Console.
