import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

regions = ec2.describe_regions()
print("Available regions:")
for r in regions['Regions']:
    print(f"  - {r['RegionName']}")

zones = ec2.describe_availability_zones()
print("\nAvailable zones in us-east-1:")
for z in zones['AvailabilityZones']:
    print(f"  - {z['ZoneName']} (State: {z['State']})")
