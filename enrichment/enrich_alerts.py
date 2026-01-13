import json

# Load alerts
with open("../parsers/sample_alerts.json", "r") as f:
    alerts = json.load(f)

# Load user directory lookup
with open("user_directory.json", "r") as f:
    directory = json.load(f)

# Enrich each alert with department/title
for alert in alerts:
    user = alert.get("user", "unknown")
    user_info = directory.get(user)

    if user_info:
        alert["department"] = user_info.get("department", "Unknown")
        alert["title"] = user_info.get("title", "Unknown")
    else:
        alert["department"] = "Unknown"
        alert["title"] = "Unknown"

# Print enriched output (simple SOC-friendly view)
for alert in alerts:
    print(f'{alert.get("alert_id")} | {alert.get("severity")} | {alert.get("user")} | {alert.get("department")} | {alert.get("device")}')
