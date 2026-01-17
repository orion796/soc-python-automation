import csv
from extract_iocs import extract_iocs

SAMPLE_TEXT = """
User clicked a link to http://malicious-site.com/path?x=1
Connection to 10.10.10.10 and 8.8.8.8
Hash observed: e3b0c44298fc1c149afbf4c8996fb924
Email contact: attacker@example.com
"""

def write_iocs_to_csv(iocs: dict, filename: str) -> None:
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Type", "Value"])

        for ip in iocs["ips"]:
            writer.writerow(["IP", ip])

        for url in iocs["urls"]:
            writer.writerow(["URL", url])

        for h in iocs["hashes"]:
            writer.writerow(["Hash", h])

        for e in iocs["emails"]:
            writer.writerow(["Email", e])

if __name__ == "__main__":
    iocs = extract_iocs(SAMPLE_TEXT)
    write_iocs_to_csv(iocs, "ioc_report.csv")
    print("IOC report written to ioc_report.csv")
