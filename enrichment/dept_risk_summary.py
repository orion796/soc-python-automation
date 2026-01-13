import csv 

import json

# Load alerts
with open("../parsers/sample_alerts.json", "r") as f:
    alerts = json.load(f)

# Load user directory
with open("user_directory.json", "r") as f:
    directory = json.load(f)

# Count HIGH severity alerts by department
dept_counts = {}

if alert.get("severity") != "High" or dept not in ["HR", "Finance"]:
    continue

    user = alert.get("user", "unknown")
    dept = directory.get(user, {}).get("department", "Unknown")

    dept_counts[dept] = dept_counts.get(dept, 0) + 1

# Write summary to CSV
with open("dept_risk_report.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Department", "High Severity Alerts"])
    for dept, count in sorted(dept_counts.items(), key=lambda x: x[1], reverse=True):
        writer.writerow([dept, count])

# Print summary sorted by most alerts
for dept, count in sorted(dept_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{dept}: {count} high severity alerts")
