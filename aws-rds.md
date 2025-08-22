# AWS CLI – RDS Guide

## Table of Contents
1. [Overview](#overview)
2. [DB Instances](#1-db-instances)
3. [Snapshots](#2-snapshots)
4. [Parameter Groups](#3-parameter-groups)
5. [Security Groups](#4-security-groups)
6. [Subnet Groups](#5-subnet-groups)
7. [Multi-AZ & Read Replicas](#6-multi-az--read-replicas)
8. [Monitoring & Logs](#7-monitoring--logs)
9. [Best Practices](#8-best-practices)
10. [Troubleshooting](#9-troubleshooting)

---

## Overview
Amazon RDS provides managed relational database services supporting MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, and Amazon Aurora. The CLI enables comprehensive database lifecycle management including instance creation, backups, monitoring, and maintenance operations. This guide covers essential RDS operations for database administration.

---

## 1. DB Instances

### Create DB Instance (MySQL Example)
````bash
aws rds create-db-instance \
  --db-instance-identifier xxxxxxxx \  # user input here (DB instance identifier)
  --db-instance-class xxxxxxxx \  # user input here (instance class, e.g., db.t3.micro)
  --engine xxxxxxxx \  # user input here (engine, e.g., mysql, postgres, oracle-ee)
  --master-username xxxxxxxx \  # user input here (master username)
  --master-user-password xxxxxxxx \  # user input here (master password)
  --allocated-storage xxxxxxxx \  # user input here (storage in GB)
  --vpc-security-group-ids xxxxxxxx \  # user input here (security group ID)
  --db-subnet-group-name xxxxxxxx  # user input here (subnet group name)
````

### Create DB Instance with Encryption
````bash
aws rds create-db-instance \
  --db-instance-identifier xxxxxxxx \  # user input here (DB instance identifier)
  --db-instance-class xxxxxxxx \  # user input here (instance class)
  --engine xxxxxxxx \  # user input here (database engine)
  --master-username xxxxxxxx \  # user input here (master username)
  --master-user-password xxxxxxxx \  # user input here (master password)
  --allocated-storage xxxxxxxx \  # user input here (storage in GB)
  --vpc-security-group-ids xxxxxxxx \  # user input here (security group ID)
  --db-subnet-group-name xxxxxxxx \  # user input here (subnet group name)
  --storage-encrypted \
  --kms-key-id xxxxxxxx  # user input here (KMS key ID, optional)
````

### List DB Instances
````bash
aws rds describe-db-instances
````

### Get Specific DB Instance Details
````bash
aws rds describe-db-instances --db-instance-identifier xxxxxxxx  # user input here (DB instance identifier)
````

### Modify DB Instance
````bash
aws rds modify-db-instance \
  --db-instance-identifier xxxxxxxx \  # user input here (DB instance identifier)
  --db-instance-class xxxxxxxx \  # user input here (new instance class)
  --allocated-storage xxxxxxxx \  # user input here (new storage size in GB)
  --apply-immediately
````

### Start DB Instance (if stopped)
````bash
aws rds start-db-instance --db-instance-identifier xxxxxxxx  # user input here (DB instance identifier)
````

### Stop DB Instance
````bash
aws rds stop-db-instance --db-instance-identifier xxxxxxxx  # user input here (DB instance identifier)
````

### Reboot DB Instance
````bash
aws rds reboot-db-instance --db-instance-identifier xxxxxxxx  # user input here (DB instance identifier)
````

### Delete DB Instance
````bash
aws rds delete-db-instance \
  --db-instance-identifier xxxxxxxx \  # user input here (DB instance identifier)
  --skip-final-snapshot
````

### Delete DB Instance with Final Snapshot
````bash
aws rds delete-db-instance \
  --db-instance-identifier xxxxxxxx \  # user input here (DB instance identifier)
  --final-db-snapshot-identifier xxxxxxxx  # user input here (final snapshot identifier)
````

---

## 2. Snapshots

### Create Manual Snapshot
````bash
aws rds create-db-snapshot \
  --db-instance-identifier xxxxxxxx \  # user input here (DB instance identifier)
  --db-snapshot-identifier xxxxxxxx  # user input here (snapshot identifier)
````

### List DB Snapshots
````bash
aws rds describe-db-snapshots
````

### List Snapshots for Specific Instance
````bash
aws rds describe-db-snapshots --db-instance-identifier xxxxxxxx  # user input here (DB instance identifier)
````

### Get Specific Snapshot Details
````bash
aws rds describe-db-snapshots --db-snapshot-identifier xxxxxxxx  # user input here (snapshot identifier)
````

### Restore DB Instance from Snapshot
````bash
aws rds restore-db-instance-from-db-snapshot \
  --db-instance-identifier xxxxxxxx \  # user input here (new DB instance identifier)
  --db-snapshot-identifier xxxxxxxx \  # user input here (source snapshot identifier)
  --db-instance-class xxxxxxxx \  # user input here (instance class)
  --vpc-security-group-ids xxxxxxxx \  # user input here (security group ID)
  --db-subnet-group-name xxxxxxxx  # user input here (subnet group name)
````

### Copy Snapshot
````bash
aws rds copy-db-snapshot \
  --source-db-snapshot-identifier xxxxxxxx \  # user input here (source snapshot identifier)
  --target-db-snapshot-identifier xxxxxxxx  # user input here (target snapshot identifier)
````

### Copy Snapshot to Another Region
````bash
aws rds copy-db-snapshot \
  --source-db-snapshot-identifier arn:aws:rds:xxxxxxxx:xxxxxxxx:snapshot:xxxxxxxx \  # user input here (source region, account ID, snapshot identifier)
  --target-db-snapshot-identifier xxxxxxxx \  # user input here (target snapshot identifier)
  --source-region xxxxxxxx  # user input here (source region)
````

### Delete Snapshot
````bash
aws rds delete-db-snapshot --db-snapshot-identifier xxxxxxxx  # user input here (snapshot identifier)
````

### Configure Automated Backups
````bash
aws rds modify-db-instance \
  --db-instance-identifier xxxxxxxx \  # user input here (DB instance identifier)
  --backup-retention-period xxxxxxxx \  # user input here (retention period in days, 0-35)
  --preferred-backup-window "xxxxxxxx"  # user input here (backup window, e.g., "03:00-04:00")
````

---

## 3. Parameter Groups

### Create Parameter Group
````bash
aws rds create-db-parameter-group \
  --db-parameter-group-name xxxxxxxx \  # user input here (parameter group name)
  --db-parameter-group-family xxxxxxxx \  # user input here (family, e.g., mysql8.0, postgres13)
  --description "xxxxxxxx"  # user input here (description)
````

### List Parameter Groups
````bash
aws rds describe-db-parameter-groups
````

### Get Parameter Group Details
````bash
aws rds describe-db-parameter-groups --db-parameter-group-name xxxxxxxx  # user input here (parameter group name)
````

### List Parameters in Group
````bash
aws rds describe-db-parameters --db-parameter-group-name xxxxxxxx  # user input here (parameter group name)
````

### Modify Parameter
````bash
aws rds modify-db-parameter-group \
  --db-parameter-group-name xxxxxxxx \  # user input here (parameter group name)
  --parameters "ParameterName=xxxxxxxx,ParameterValue=xxxxxxxx,ApplyMethod=pending-reboot"  # user input here (parameter name and value)
````

### Apply Parameter Group to Instance
````bash
aws rds modify-db-instance \
  --db-instance-identifier xxxxxxxx \  # user input here (DB instance identifier)
  --db-parameter-group-name xxxxxxxx  # user input here (parameter group name)
````

### Reset Parameter Group
````bash
aws rds reset-db-parameter-group \
  --db-parameter-group-name xxxxxxxx  # user input here (parameter group name)
````

### Delete Parameter Group
````bash
aws rds delete-db-parameter-group --db-parameter-group-name xxxxxxxx  # user input here (parameter group name)
````

---

## 4. Security Groups

### Create DB Security Group (EC2-Classic)
````bash
aws rds create-db-security-group \
  --db-security-group-name xxxxxxxx \  # user input here (security group name)
  --db-security-group-description "xxxxxxxx"  # user input here (description)
````

### Authorize Security Group Ingress
````bash
aws rds authorize-db-security-group-ingress \
  --db-security-group-name xxxxxxxx \  # user input here (security group name)
  --cidrip xxxxxxxx/xx  # user input here (CIDR block)
````

### For VPC (use EC2 security groups instead):
````bash
aws ec2 authorize-security-group-ingress \
  --group-id xxxxxxxx \  # user input here (VPC security group ID)
  --protocol tcp \
  --port xxxxxxxx \  # user input here (database port, e.g., 3306 for MySQL)
  --cidr xxxxxxxx/xx  # user input here (CIDR block)
````

---

## 5. Subnet Groups

### Create DB Subnet Group
````bash
aws rds create-db-subnet-group \
  --db-subnet-group-name xxxxxxxx \  # user input here (subnet group name)
  --db-subnet-group-description "xxxxxxxx" \  # user input here (description)
  --subnet-ids xxxxxxxx xxxxxxxx xxxxxxxx  # user input here (subnet IDs from different AZs)
````

### List Subnet Groups
````bash
aws rds describe-db-subnet-groups
````

### Get Subnet Group Details
````bash
aws rds describe-db-subnet-groups --db-subnet-group-name xxxxxxxx  # user input here (subnet group name)
````

### Modify Subnet Group
````bash
aws rds modify-db-subnet-group \
  --db-subnet-group-name xxxxxxxx \  # user input here (subnet group name)
  --subnet-ids xxxxxxxx xxxxxxxx xxxxxxxx  # user input here (updated subnet IDs)
````

### Delete Subnet Group
````bash
aws rds delete-db-subnet-group --db-subnet-group-name xxxxxxxx  # user input here (subnet group name)
````

---

## 6. Multi-AZ & Read Replicas

### Enable Multi-AZ
````bash
aws rds modify-db-instance \
  --db-instance-identifier xxxxxxxx \  # user input here (DB instance identifier)
  --multi-az \
  --apply-immediately
````

### Create Read Replica
````bash
aws rds create-db-instance-read-replica \
  --db-instance-identifier xxxxxxxx \  # user input here (read replica identifier)
  --source-db-instance-identifier xxxxxxxx \  # user input here (source DB instance identifier)
  --db-instance-class xxxxxxxx  # user input here (instance class)
````

### Create Cross-Region Read Replica
````bash
aws rds create-db-instance-read-replica \
  --db-instance-identifier xxxxxxxx \  # user input here (read replica identifier)
  --source-db-instance-identifier arn:aws:rds:xxxxxxxx:xxxxxxxx:db:xxxxxxxx \  # user input here (source region, account ID, source DB identifier)
  --db-instance-class xxxxxxxx  # user input here (instance class)
````

### Promote Read Replica
````bash
aws rds promote-read-replica --db-instance-identifier xxxxxxxx  # user input here (read replica identifier)
````

### Failover Multi-AZ Instance
````bash
aws rds reboot-db-instance \
  --db-instance-identifier xxxxxxxx \  # user input here (DB instance identifier)
  --force-failover
````

---

## 7. Monitoring & Logs

### Enable Enhanced Monitoring
````bash
aws rds modify-db-instance \
  --db-instance-identifier xxxxxxxx \  # user input here (DB instance identifier)
  --monitoring-interval xxxxxxxx \  # user input here (interval in seconds, e.g., 60)
  --monitoring-role-arn arn:aws:iam::xxxxxxxx:role/xxxxxxxx  # user input here (account ID and monitoring role name)
````

### Enable Performance Insights
````bash
aws rds modify-db-instance \
  --db-instance-identifier xxxxxxxx \  # user input here (DB instance identifier)
  --enable-performance-insights \
  --performance-insights-retention-period xxxxxxxx  # user input here (retention period in days, 7-731)
````

### Get DB Log Files
````bash
aws rds describe-db-log-files --db-instance-identifier xxxxxxxx  # user input here (DB instance identifier)
````

### Download Log File Portion
````bash
aws rds download-db-log-file-portion \
  --db-instance-identifier xxxxxxxx \  # user input here (DB instance identifier)
  --log-file-name xxxxxxxx  # user input here (log file name)
````

### Get DB Instance Metrics
````bash
aws cloudwatch get-metric-statistics \
  --namespace AWS/RDS \
  --metric-name CPUUtilization \
  --dimensions Name=DBInstanceIdentifier,Value=xxxxxxxx \  # user input here (DB instance identifier)
  --statistics Average \
  --start-time 2025-01-01T00:00:00Z \
  --end-time 2025-01-02T00:00:00Z \
  --period 3600
````

### Get Database Connections
````bash
aws cloudwatch get-metric-statistics \
  --namespace AWS/RDS \
  --metric-name DatabaseConnections \
  --dimensions Name=DBInstanceIdentifier,Value=xxxxxxxx \  # user input here (DB instance identifier)
  --statistics Average,Maximum \
  --start-time 2025-01-01T00:00:00Z \
  --end-time 2025-01-02T00:00:00Z \
  --period 3600
````

---

## 8. Best Practices

- **Enable encryption at rest** for sensitive data using KMS keys
- **Use parameter groups** for consistent database configurations across environments
- **Implement Multi-AZ** for high availability in production environments
- **Set appropriate backup retention** periods based on recovery requirements
- **Use read replicas** to scale read workloads and reduce primary instance load
- **Enable Enhanced Monitoring** for detailed instance-level metrics
- **Configure security groups** to allow access only from necessary sources
- **Use subnet groups** to control network placement and availability zones
- **Monitor key metrics** like CPU, memory, connections, and IOPS
- **Implement proper maintenance windows** for automated patching and updates
- **Use Performance Insights** to identify and resolve database performance issues
- **Tag resources consistently** for cost allocation and management
- **Regularly test backup and restore** procedures

---

## 9. Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| **Connection timeout** | Security group or network configuration | Verify security group rules and network connectivity |
| **Authentication failed** | Wrong credentials or expired password | Check username/password; reset if needed |
| **Out of storage** | Allocated storage exhausted | Increase allocated storage or enable auto-scaling |
| **High CPU utilization** | Inefficient queries or insufficient resources | Optimize queries or upgrade instance class |
| **Connection pool exhausted** | Too many concurrent connections | Increase max_connections parameter or use connection pooling |
| **Backup failure** | Insufficient permissions or storage | Check IAM permissions and available storage |
| **Read replica lag** | High write volume or network issues | Monitor replica lag; consider upgrading network or instance |
| **Parameter changes not applied** | Requires instance restart | Reboot instance to apply static parameter changes |
| **Multi-AZ failover slow** | Large transaction logs or checkpoints | Monitor failover times; optimize checkpoint settings |
| **Storage IOPS exhausted** | High I/O workload exceeding limits | Upgrade to higher IOPS storage or optimize queries |

### Debugging Commands

Check instance status:
````bash
aws rds describe-db-instances \
  --db-instance-identifier xxxxxxxx \  # user input here (DB instance identifier)
  --query 'DBInstances[0].{Status:DBInstanceStatus,Engine:Engine,Class:DBInstanceClass}'
````

List recent events:
````bash
aws rds describe-events \
  --source-identifier xxxxxxxx \  # user input here (DB instance identifier)
  --source-type db-instance \
  --max-items 10
````

Check parameter group status:
````bash
aws rds describe-db-instances \
  --db-instance-identifier xxxxxxxx \  # user input here (DB instance identifier)
  --query 'DBInstances[0].DBParameterGroups[0].{Name:DBParameterGroupName,Status:ParameterApplyStatus}'
````

Get connection information:
````bash
aws rds describe-db-instances \
  --db-instance-identifier xxxxxxxx \  # user input here (DB instance identifier)
  --query 'DBInstances[0].{Endpoint:Endpoint.Address,Port:Endpoint.Port,AZ:AvailabilityZone}'
````

Check backup configuration:
````bash
aws rds describe-db-instances \
  --db-instance-identifier xxxxxxxx \  # user input here (DB instance identifier)
  --query 'DBInstances[0].{BackupRetention:BackupRetentionPeriod,BackupWindow:PreferredBackupWindow,MaintenanceWindow:PreferredMaintenanceWindow}'
````

---