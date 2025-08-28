#!/usr/bin/env python3
"""
Create an EC2 key pair & security group (idempotent).
- Saves private key to PEM file with strict perms (Linux/macOS).
- Restricts SSH to detected public IP (fallback 0.0.0.0/0 if detection fails).
"""
import os, stat, sys, urllib.request
import boto3
from botocore.exceptions import ClientError

KEY_NAME = "MySDKKey"
KEY_FILE = f"{KEY_NAME}.pem"
SG_NAME  = "MySDKSecurityGroup"
SG_DESC  = "Security group created by script"
IP_DETECT_URL = "https://api.ipify.org"

ec2 = boto3.client("ec2")

def get_public_ip():
    try:
        with urllib.request.urlopen(IP_DETECT_URL, timeout=5) as r:
            return r.read().decode().strip()
    except Exception as e:
        print("Public IP detection failed:", e)
        return None

def write_key(km):
    with open(KEY_FILE, "w", encoding="utf-8") as f:
        f.write(km)
    try:
        os.chmod(KEY_FILE, stat.S_IRUSR)  # 400
    except OSError:
        print("Warning: chmod not applied (likely Windows).")

def ensure_key():
    try:
        print(f"Creating key pair {KEY_NAME}...")
        resp = ec2.create_key_pair(KeyName=KEY_NAME, KeyType="rsa", KeyFormat="pem")
        write_key(resp["KeyMaterial"])
        print(f"Key saved: {KEY_FILE}")
    except ClientError as e:
        if e.response["Error"]["Code"] == "InvalidKeyPair.Duplicate":
            print(f"Key pair {KEY_NAME} already exists. Skipping.")
        else:
            raise

def get_default_vpc():
    vpcs = ec2.describe_vpcs(Filters=[{"Name": "isDefault", "Values": ["true"]}])["Vpcs"]
    if not vpcs:
        print("No default VPC found.")
        sys.exit(1)
    return vpcs[0]["VpcId"]

def ensure_security_group(vpc_id):
    try:
        print(f"Creating security group {SG_NAME}...")
        resp = ec2.create_security_group(GroupName=SG_NAME, Description=SG_DESC, VpcId=vpc_id)
        return resp["GroupId"], True
    except ClientError as e:
        if e.response["Error"]["Code"] == "InvalidGroup.Duplicate":
            groups = ec2.describe_security_groups(Filters=[{"Name": "group-name", "Values": [SG_NAME]}])
            return groups["SecurityGroups"][0]["GroupId"], False
        raise

def authorize_rules(sg_id, ssh_cidr):
    perms = [
        {"IpProtocol":"tcp","FromPort":22,"ToPort":22,"IpRanges":[{"CidrIp":ssh_cidr,"Description":"SSH"}]},
        {"IpProtocol":"tcp","FromPort":80,"ToPort":80,"IpRanges":[{"CidrIp":"0.0.0.0/0","Description":"HTTP"}]},
        {"IpProtocol":"tcp","FromPort":443,"ToPort":443,"IpRanges":[{"CidrIp":"0.0.0.0/0","Description":"HTTPS"}]}
    ]
    try:
        ec2.authorize_security_group_ingress(GroupId=sg_id, IpPermissions=perms)
        print("Ingress rules added.")
    except ClientError as e:
        if e.response["Error"]["Code"] == "InvalidPermission.Duplicate":
            print("Some ingress rules already present.")
        else:
            raise

def main():
    ensure_key()
    vpc_id = get_default_vpc()
    sg_id, created = ensure_security_group(vpc_id)
    print(f"Security Group ID: {sg_id} (created={created})")
    ip = get_public_ip()
    ssh_cidr = f"{ip}/32" if ip else "0.0.0.0/0"
    print(f"Using SSH CIDR: {ssh_cidr}")
    authorize_rules(sg_id, ssh_cidr)
    print("\nDone. Key:", KEY_FILE, "Security Group:", sg_id)

if __name__ == "__main__":
    try:
        main()
    except ClientError as e:
        print("AWS Error:", e)
        sys.exit(1)
