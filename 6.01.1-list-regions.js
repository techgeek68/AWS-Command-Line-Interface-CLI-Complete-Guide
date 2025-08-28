// List AWS EC2 regions using aws-sdk v3 (ESM).
import { EC2Client, DescribeRegionsCommand } from "@aws-sdk/client-ec2";

const client = new EC2Client({}); // Region from env/profile
const res = await client.send(new DescribeRegionsCommand({}));
console.log("Regions:", res.Regions.map(r => r.RegionName));
