import requests
import pandas as pd

# GDP per capita Shqipëri
url = "https://api.worldbank.org/v2/country/ALB/indicator/NY.GDP.PCAP.CD?format=json"
response = requests.get(url)
data = response.json()[1]

records = []
for item in data:
    if item["value"] is not None:
        records.append({"year": int(item["date"]), "gdp_per_capita": item["value"]})

df = pd.DataFrame(records)
df.to_csv("world_bank_gdp.csv", index=False)
print("✅ World Bank data u ruajt")

