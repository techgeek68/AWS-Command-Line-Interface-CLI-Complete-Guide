#!/usr/bin/env python3
"""List available EC2 regions using boto3."""
import boto3

def main():
    ec2 = boto3.client("ec2")
    regions = [r["RegionName"] for r in ec2.describe_regions()["Regions"]]
    print("Available AWS Regions:")
    for r in regions:
        print("-", r)

if __name__ == "__main__":
    main()
