import re

SAMPLE_TEXT = """
User clicked a link to http://malicious-site.com/path?x=1
Second link: https://example.org/login
Connection made to 192.168.1.50 and then 8.8.8.8
Suspicious hash (md5): e3b0c44298fc1c149afbf4c8996fb924
Suspicious hash (sha256): a54d88e06612d820bc3be72877c74f257b561b19c5d4a6c2a77fbe8f8f6c3f63
Email: attacker@example.com
"""

# Patterns (SOC-focused)
IP_PATTERN = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
URL_PATTERN = r"https?://[^\s\"')]+"
HASH_PATTERN = r"\b[a-fA-F0-9]{32}\b|\b[a-fA-F0-9]{64}\b"
EMAIL_PATTERN = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

def extract_iocs(text: str) -> dict:
    ips = sorted(set(re.findall(IP_PATTERN, text)))
    urls = sorted(set(re.findall(URL_PATTERN, text)))
    hashes = sorted(set(re.findall(HASH_PATTERN, text)))
    emails = sorted(set(re.findall(EMAIL_PATTERN, text)))

    return {
        "ips": ips,
        "urls": urls,
        "hashes": hashes,
        "emails": emails,
    }

def print_results(iocs: dict) -> None:
    print("IPs:")
    for ip in iocs["ips"]:
        print(f"  - {ip}")

    print("\nURLs:")
    for url in iocs["urls"]:
        print(f"  - {url}")

    print("\nHashes:")
    for h in iocs["hashes"]:
        print(f"  - {h}")

    print("\nEmails:")
    for e in iocs["emails"]:
        print(f"  - {e}")

if __name__ == "__main__":
    iocs = extract_iocs(SAMPLE_TEXT)
    print_results(iocs)
