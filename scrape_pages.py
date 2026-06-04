"""
Scrape live dmedesk.ai pages and save as local HTML files.
Usage: python scrape_pages.py
"""

import urllib.request
import os

PAGES = [
    ("resources",   "https://dmedesk.ai/resources"),
    ("how-it-works","https://dmedesk.ai/how-it-works"),
    ("features",    "https://dmedesk.ai/features"),
    ("integrations","https://dmedesk.ai/integrations"),
]

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read().decode("utf-8", errors="replace")


def main():
    for slug, url in PAGES:
        filename = f"dmedesk_{slug.replace('-', '_')}_page.html"
        out_path = os.path.join(OUT_DIR, filename)
        print(f"Fetching {url} ...", end=" ", flush=True)
        html = fetch(url)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"saved → {filename}  ({len(html):,} bytes)")

    print("\nDone. All 4 pages saved.")


if __name__ == "__main__":
    main()
