import requests

url = "https://en.wikipedia.org/api/rest_v1/page/summary/Ministry_of_Finance_(Albania)"

headers = {
    "User-Agent": "MinistryOfFinanceProject/1.0 (example@email.com)"  # Wikipedia kërkon UA
}

response = requests.get(url, headers=headers)

# Kontroll për status code
if response.status_code == 200:
    try:
        data = response.json()
        with open("wikipedia_finance.txt", "w", encoding="utf-8") as f:
            f.write(data.get("extract", ""))
        print("✅ Përshkrimi institucional u ruajt")
    except:
        print("❌ JSON nuk mund të parse-het")
else:
    print(f"❌ Request dështoi me status: {response.status_code}")
