import {
  EC2Client,
  CreateKeyPairCommand,
  CreateSecurityGroupCommand,
  AuthorizeSecurityGroupIngressCommand,
  DescribeVpcsCommand
} from "@aws-sdk/client-ec2";
import fs from "fs";

const KEY_NAME = "MySDKKey";
const SG_NAME = "MySDKSecurityGroup";
const client = new EC2Client({});

async function defaultVpc() {
  const resp = await client.send(new DescribeVpcsCommand({
    Filters: [{ Name: "isDefault", Values: ["true"] }]
  }));
  if (!resp.Vpcs || resp.Vpcs.length === 0) throw new Error("No default VPC");
  return resp.Vpcs[0].VpcId;
}

async function main() {
  try {
    const keyResp = await client.send(new CreateKeyPairCommand({ KeyName: KEY_NAME }));
    fs.writeFileSync(`${KEY_NAME}.pem`, keyResp.KeyMaterial, { mode: 0o400 });
    console.log("Key saved.");
  } catch (e) {
    if (e.name === "InvalidKeyPair.Duplicate") console.log("Key already exists.");
    else throw e;
  }

  const vpcId = await defaultVpc();
  let sgId;
  try {
    const sgResp = await client.send(new CreateSecurityGroupCommand({
      GroupName: SG_NAME,
      Description: "SDK created",
      VpcId: vpcId
    }));
    sgId = sgResp.GroupId;
    console.log("Created SG:", sgId);
  } catch (e) {
    if ((e.name || "").includes("InvalidGroup.Duplicate")) {
      console.log("Security group already exists (lookup omitted).");
      return;
    } else throw e;
  }

  await client.send(new AuthorizeSecurityGroupIngressCommand({
    GroupId: sgId,
    IpPermissions: [
      { IpProtocol: "tcp", FromPort: 22, ToPort: 22, IpRanges: [{ CidrIp: "0.0.0.0/0" }] },
      { IpProtocol: "tcp", FromPort: 80, ToPort: 80, IpRanges: [{ CidrIp: "0.0.0.0/0" }] }
    ]
  }));
  console.log("Ingress authorized.");
}

main().catch(err => {
  console.error("Error:", err);
  process.exit(1);
});
