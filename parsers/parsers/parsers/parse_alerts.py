import json

with open("sample_alerts.json", "r") as f:
    alerts = json.load(f)

counts = {}

for alert in alerts:
    user = alert["user"]
    if user in counts:
        counts[user] += 1
    else:
        counts[user] = 1

for user, count in counts.items():
    print(f"{user}: {count} alerts")
