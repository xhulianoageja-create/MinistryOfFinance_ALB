import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import feedparser

RSS_URL = "https://financa.gov.al/feed/"  # Nëse ka RSS
HTML_URL = "https://financa.gov.al/njoftime/"

records = []

# 1️⃣ RSS Feed
try:
    feed = feedparser.parse(RSS_URL)
    if len(feed.entries) > 0:
        for entry in feed.entries:
            records.append({
                "title": entry.get("title", None),
                "link": entry.get("link", None),
                "date": entry.get("published", None)
            })
    else:
        raise Exception("RSS bosh")
except:
    print("⚠️ RSS feed nuk është i disponueshëm, provoni HTML scraping")
    # 2️⃣ HTML scraping
    try:
        response = requests.get(HTML_URL, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        njoftime = soup.select("div.njoftime-item")  # ndrysho sipas faqes reale

        for item in njoftime:
            title = item.find("h2").text.strip() if item.find("h2") else None
            link = item.find("a")["href"] if item.find("a") else None
            date = item.find("time").text.strip() if item.find("time") else None
            records.append({"title": title, "link": link, "date": date})

        if len(records) == 0:
            raise Exception("HTML scraping nuk gjeti asnjë njoftim")
    except:
        print("⚠️ HTML scraping nuk funksionoi, krijojmë CSV mock")
        # 3️⃣ Mock fallback
        records = [
            {"title": "Njoftim për buxhetin 2026", "link": "#", "date": "2026-01-10"},
            {"title": "Raport vjetor i Financës", "link": "#", "date": "2025-12-20"},
            {"title": "Vendim mbi taksat", "link": "#", "date": "2025-12-05"},
        ]

# DataFrame final
df = pd.DataFrame(records)
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["year"] = df["date"].dt.year

df.to_csv("njoftime_financa.csv", index=False, encoding="utf-8")
print("✅ CSV për njoftime përfundoi")
print(df.head())
