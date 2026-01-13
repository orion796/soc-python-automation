import json

HIGH_ONLY = True  # change to False to count all alerts

with open("sample_alerts.json", "r") as f:
    alerts = json.load(f)

counts = {}

for alert in alerts:
    if HIGH_ONLY and alert.get("severity") != "High":
        continue

    user = alert.get("user", "unknown")
    counts[user] = counts.get(user, 0) + 1

for user, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    mode = "HIGH" if HIGH_ONLY else "ALL"
    print(f"[{mode}] {user}: {count} alerts")
