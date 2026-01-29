import requests
import pandas as pd

url = "https://data.europa.eu/api/hub/search/search"
params = {"q": "finance Albania", "limit": 20}

response = requests.get(url, params=params)
results = response.json()["result"]["results"]

records = []
for r in results:
    records.append({
        "title": r.get("title"),
        "publisher": r.get("publisher"),
        "year": r.get("issued", "")[:4]
    })

df = pd.DataFrame(records)
df.to_csv("eu_finance_projects.csv", index=False)
print("✅ EU Open Data u ruajt")
