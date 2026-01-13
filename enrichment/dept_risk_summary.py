import json

# Load alerts
with open("../parsers/sample_alerts.json", "r") as f:
    alerts = json.load(f)

# Load user directory
with open("user_directory.json", "r") as f:
    directory = json.load(f)

# Count HIGH severity alerts by department
dept_counts = {}

for alert in alerts:
    if alert.get("severity") != "High":
        continue

    user = alert.get("user", "unknown")
    dept = directory.get(user, {}).get("department", "Unknown")

    dept_counts[dept] = dept_counts.get(dept, 0) + 1

# Print summary sorted by most alerts
for dept, count in sorted(dept_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{dept}: {count} high severity alerts")
