# AWS CLI – CloudWatch Guide

## Table of Contents
1. [Overview](#overview)
2. [Log Groups & Streams](#1-log-groups--streams)
3. [Fetching Log Events](#2-fetching-log-events)
4. [Log Insights Queries](#3-log-insights-queries)
5. [Metrics](#4-metrics)
6. [Alarms](#5-alarms)
7. [Dashboards](#6-dashboards)
8. [Events & EventBridge](#7-events--eventbridge)
9. [Best Practices](#8-best-practices)
10. [Troubleshooting](#9-troubleshooting)

---

## Overview
Amazon CloudWatch provides observability through metrics, logs, alarms, and events. The CLI facilitates log management, custom metric publishing, alarm configuration, and insights queries. CloudWatch is essential for monitoring application and infrastructure health across AWS services.

---

## 1. Log Groups & Streams

### Create Log Group
````bash
aws logs create-log-group --log-group-name xxxxxxxx  # user input here (log group name, e.g., /aws/lambda/my-function)
````

### List Log Groups
````bash
aws logs describe-log-groups
````

### List Log Groups with Filter
````bash
aws logs describe-log-groups --log-group-name-prefix xxxxxxxx  # user input here (log group prefix)
````

### Create Log Stream
````bash
aws logs create-log-stream \
  --log-group-name xxxxxxxx \  # user input here (log group name)
  --log-stream-name xxxxxxxx  # user input here (log stream name)
````

### List Log Streams
````bash
aws logs describe-log-streams --log-group-name xxxxxxxx  # user input here (log group name)
````

### Put Log Events
````bash
aws logs put-log-events \
  --log-group-name xxxxxxxx \  # user input here (log group name)
  --log-stream-name xxxxxxxx \  # user input here (log stream name)
  --log-events timestamp=$(date +%s)000,message="xxxxxxxx"  # user input here (log message)
````

### Delete Log Group
````bash
aws logs delete-log-group --log-group-name xxxxxxxx  # user input here (log group name)
````

### Delete Log Stream
````bash
aws logs delete-log-stream \
  --log-group-name xxxxxxxx \  # user input here (log group name)
  --log-stream-name xxxxxxxx  # user input here (log stream name)
````

### Set Log Retention
````bash
aws logs put-retention-policy \
  --log-group-name xxxxxxxx \  # user input here (log group name)
  --retention-in-days xxxxxxxx  # user input here (retention period in days, e.g., 30, 90, 365)
````

---

## 2. Fetching Log Events

### Get Log Events from Stream
````bash
aws logs get-log-events \
  --log-group-name xxxxxxxx \  # user input here (log group name)
  --log-stream-name xxxxxxxx  # user input here (log stream name)
````

### Get Recent Log Events
````bash
aws logs get-log-events \
  --log-group-name xxxxxxxx \  # user input here (log group name)
  --log-stream-name xxxxxxxx \  # user input here (log stream name)
  --start-time $(date -d "1 hour ago" +%s)000
````

### Filter Log Events
````bash
aws logs filter-log-events \
  --log-group-name xxxxxxxx \  # user input here (log group name)
  --filter-pattern "xxxxxxxx"  # user input here (filter pattern, e.g., "ERROR", "[timestamp, request_id, level=ERROR]")
````

### Filter Events with Time Range
````bash
aws logs filter-log-events \
  --log-group-name xxxxxxxx \  # user input here (log group name)
  --start-time $(date -d "1 hour ago" +%s)000 \
  --end-time $(date +%s)000 \
  --filter-pattern "xxxxxxxx"  # user input here (filter pattern)
````

### Tail Log Group (Live)
````bash
aws logs tail xxxxxxxx --since 5m  # user input here (log group name)
````

### Tail with Filter
````bash
aws logs tail xxxxxxxx --filter-pattern "xxxxxxxx"  # user input here (log group name and filter pattern)
````

### Export Log Data to S3
````bash
aws logs create-export-task \
  --log-group-name xxxxxxxx \  # user input here (log group name)
  --from $(date -d "1 day ago" +%s)000 \
  --to $(date +%s)000 \
  --destination xxxxxxxx \  # user input here (S3 bucket name)
  --destination-prefix xxxxxxxx  # user input here (S3 prefix)
````

---

## 3. Log Insights Queries

### Start Insights Query
````bash
aws logs start-query \
  --log-group-name xxxxxxxx \  # user input here (log group name)
  --start-time $(date -d "1 hour ago" +%s) \
  --end-time $(date +%s) \
  --query-string "xxxxxxxx"  # user input here (Insights query, e.g., "fields @timestamp, @message | sort @timestamp desc | limit 20")
````

### Get Query Results
````bash
aws logs get-query-results --query-id xxxxxxxx  # user input here (query ID from start-query response)
````

### Example Insights Queries

Count errors by time:
````sql
fields @timestamp, @message
| filter @message like /ERROR/
| stats count() by bin(5m)
````

Find slowest requests:
````sql
fields @timestamp, @requestId, @duration
| filter @type = "REPORT"
| sort @duration desc
| limit 10
````

Memory usage analysis:
````sql
fields @timestamp, @maxMemoryUsed
| filter @type = "REPORT"
| stats avg(@maxMemoryUsed), max(@maxMemoryUsed) by bin(5m)
````

---

## 4. Metrics

### Put Custom Metric
````bash
aws cloudwatch put-metric-data \
  --namespace "xxxxxxxx" \  # user input here (custom namespace, e.g., "MyApp/Performance")
  --metric-data MetricName=xxxxxxxx,Value=xxxxxxxx,Unit=xxxxxxxx  # user input here (metric name, value, unit)
````

### Put Metric with Dimensions
````bash
aws cloudwatch put-metric-data \
  --namespace "xxxxxxxx" \  # user input here (namespace)
  --metric-data MetricName=xxxxxxxx,Value=xxxxxxxx,Unit=Count,Dimensions="[{Name=xxxxxxxx,Value=xxxxxxxx}]"  # user input here (metric details and dimension)
````

### Get Metric Statistics
````bash
aws cloudwatch get-metric-statistics \
  --namespace xxxxxxxx \  # user input here (namespace, e.g., AWS/EC2, AWS/Lambda)
  --metric-name xxxxxxxx \  # user input here (metric name, e.g., CPUUtilization)
  --dimensions Name=xxxxxxxx,Value=xxxxxxxx \  # user input here (dimension name and value)
  --statistics Average,Maximum \
  --start-time 2025-01-01T00:00:00Z \
  --end-time 2025-01-01T01:00:00Z \
  --period 300
````

### List Available Metrics
````bash
aws cloudwatch list-metrics --namespace xxxxxxxx  # user input here (namespace)
````

### List Metrics with Dimensions
````bash
aws cloudwatch list-metrics \
  --namespace xxxxxxxx \  # user input here (namespace)
  --dimensions Name=xxxxxxxx,Value=xxxxxxxx  # user input here (dimension name and value)
````

---

## 5. Alarms

### Create Metric Alarm
````bash
aws cloudwatch put-metric-alarm \
  --alarm-name "xxxxxxxx" \  # user input here (alarm name)
  --alarm-description "xxxxxxxx" \  # user input here (alarm description)
  --metric-name xxxxxxxx \  # user input here (metric name)
  --namespace xxxxxxxx \  # user input here (namespace)
  --statistic Average \
  --period 300 \
  --threshold xxxxxxxx \  # user input here (threshold value)
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 2
````

### Create Alarm with SNS Action
````bash
aws cloudwatch put-metric-alarm \
  --alarm-name "xxxxxxxx" \  # user input here (alarm name)
  --alarm-description "xxxxxxxx" \  # user input here (alarm description)
  --metric-name xxxxxxxx \  # user input here (metric name)
  --namespace xxxxxxxx \  # user input here (namespace)
  --statistic Average \
  --period 300 \
  --threshold xxxxxxxx \  # user input here (threshold value)
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 2 \
  --alarm-actions arn:aws:sns:xxxxxxxx:xxxxxxxx:xxxxxxxx  # user input here (region, account ID, SNS topic name)
````

### Create Composite Alarm
````bash
aws cloudwatch put-composite-alarm \
  --alarm-name "xxxxxxxx" \  # user input here (composite alarm name)
  --alarm-description "xxxxxxxx" \  # user input here (description)
  --alarm-rule "(ALARM(xxxxxxxx) OR ALARM(xxxxxxxx))"  # user input here (alarm names in boolean expression)
````

### List Alarms
````bash
aws cloudwatch describe-alarms
````

### List Alarms by State
````bash
aws cloudwatch describe-alarms --state-value xxxxxxxx  # user input here (state: OK, ALARM, INSUFFICIENT_DATA)
````

### Get Alarm Details
````bash
aws cloudwatch describe-alarms --alarm-names xxxxxxxx  # user input here (alarm name)
````

### Delete Alarm
````bash
aws cloudwatch delete-alarms --alarm-names xxxxxxxx  # user input here (alarm name)
````

### Enable/Disable Alarm Actions
````bash
aws cloudwatch enable-alarm-actions --alarm-names xxxxxxxx  # user input here (alarm name)
aws cloudwatch disable-alarm-actions --alarm-names xxxxxxxx  # user input here (alarm name)
````

### Get Alarm History
````bash
aws cloudwatch describe-alarm-history --alarm-name xxxxxxxx  # user input here (alarm name)
````

---

## 6. Dashboards

### Create Dashboard
````bash
aws cloudwatch put-dashboard \
  --dashboard-name "xxxxxxxx" \  # user input here (dashboard name)
  --dashboard-body file://xxxxxxxx  # user input here (path to dashboard JSON file)
````

### List Dashboards
````bash
aws cloudwatch list-dashboards
````

### Get Dashboard
````bash
aws cloudwatch get-dashboard --dashboard-name xxxxxxxx  # user input here (dashboard name)
````

### Delete Dashboard
````bash
aws cloudwatch delete-dashboards --dashboard-names xxxxxxxx  # user input here (dashboard name)
````

### Example Dashboard JSON Structure
````json
{
  "widgets": [
    {
      "type": "metric",
      "properties": {
        "metrics": [
          ["AWS/EC2", "CPUUtilization", "InstanceId", "xxxxxxxx"]
        ],
        "period": 300,
        "stat": "Average",
        "region": "xxxxxxxx",
        "title": "EC2 CPU Utilization"
      }
    }
  ]
}
````

---

## 7. Events & EventBridge

### Create Event Rule
````bash
aws events put-rule \
  --name xxxxxxxx \  # user input here (rule name)
  --event-pattern '{"source":["xxxxxxxx"],"detail-type":["xxxxxxxx"]}' \  # user input here (event source and detail type)
  --state ENABLED
````

### Add Target to Rule
````bash
aws events put-targets \
  --rule xxxxxxxx \  # user input here (rule name)
  --targets "Id"="1","Arn"="arn:aws:lambda:xxxxxxxx:xxxxxxxx:function:xxxxxxxx"  # user input here (region, account ID, function name)
````

### List Rules
````bash
aws events list-rules
````

### List Targets for Rule
````bash
aws events list-targets-by-rule --rule xxxxxxxx  # user input here (rule name)
````

### Delete Rule
````bash
aws events delete-rule --name xxxxxxxx  # user input here (rule name)
````

### Put Custom Event
````bash
aws events put-events \
  --entries Source=xxxxxxxx,DetailType=xxxxxxxx,Detail='{"xxxxxxxx":"xxxxxxxx"}'  # user input here (source, detail type, and JSON detail)
````

---

## 8. Best Practices

- **Use structured logging** (JSON) for better searchability and parsing
- **Set appropriate log retention** periods to balance cost and compliance requirements
- **Create meaningful metric dimensions** for better filtering and aggregation
- **Set up alarms for critical metrics** with appropriate thresholds and actions
- **Use composite alarms** for complex alerting scenarios involving multiple conditions
- **Implement log aggregation** strategies for distributed applications
- **Monitor CloudWatch costs** by managing log retention and metric cardinality
- **Use CloudWatch Insights** for complex log analysis instead of downloading large log files
- **Tag CloudWatch resources** consistently for cost allocation and organization
- **Set up cross-region monitoring** for disaster recovery scenarios
- **Use CloudWatch Events/EventBridge** for event-driven architectures
- **Implement proper IAM permissions** for CloudWatch access and actions

---

## 9. Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| **Log events not appearing** | Wrong log group/stream or IAM permissions | Verify log group name and IAM permissions |
| **High CloudWatch costs** | Excessive log ingestion or retention | Review log retention policies and volume |
| **Alarm not triggering** | Incorrect threshold or insufficient data | Check alarm configuration and metric availability |
| **Missing metrics** | Service not publishing or wrong namespace | Verify service configuration and metric namespace |
| **Insights query timeout** | Query too complex or large dataset | Optimize query or reduce time range |
| **Export task failed** | S3 permissions or bucket policy issue | Check S3 bucket permissions and policies |
| **Dashboard not loading** | Incorrect metric references or regions | Verify widget configurations and metric names |
| **Event rule not triggering** | Wrong event pattern or target configuration | Review event pattern syntax and target permissions |
| **Metric data delayed** | Normal CloudWatch latency | Wait for metric propagation (up to 15 minutes for some services) |

### Debugging Commands

Check log group details:
````bash
aws logs describe-log-groups --log-group-name-prefix xxxxxxxx  # user input here (log group prefix)
````

Test alarm with metric data:
````bash
aws cloudwatch set-alarm-state \
  --alarm-name xxxxxxxx \  # user input here (alarm name)
  --state-value ALARM \
  --state-reason "Testing alarm"
````

Check export task status:
````bash
aws logs describe-export-tasks --task-id xxxxxxxx  # user input here (task ID)
````

List recent CloudWatch API calls (using CloudTrail):
````bash
aws logs filter-log-events \
  --log-group-name CloudTrail/CloudWatchLogs \
  --filter-pattern "{ $.eventSource = \"monitoring.amazonaws.com\" }" \
  --start-time $(date -d "1 hour ago" +%s)000
````

Get metric data points:
````bash
aws cloudwatch get-metric-data \
  --metric-data-queries file://xxxxxxxx \  # user input here (path to metric query JSON file)
  --start-time 2025-01-01T00:00:00Z \
  --end-time 2025-01-01T01:00:00Z
````

Check alarm state changes:
````bash
aws cloudwatch describe-alarm-history \
  --alarm-name xxxxxxxx \  # user input here (alarm name)
  --max-items 10
````

---