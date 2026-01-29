1️⃣ Kërkesat paraprake (Prerequisites)

Sigurohuni që në kompjuterin tuaj janë instaluar:

Python 3.9 ose më i ri

Git

(Opsionale por e rekomanduar) Virtual Environment / Conda

Kontrolloni instalimin:

python --version
git --version

2️⃣ Klonimi i projektit nga GitHub

Hapni Command Prompt / Terminal dhe ekzekutoni:

git clone https://github.com/xhulianoageja-create/MinistryOfFinance_ALB.git


Pastaj hyni në folderin e projektit:

cd MinistryOfFinance_ALB

3️⃣ Krijimi i Virtual Environment
Windows (cmd / PowerShell):
python -m venv venv
venv\Scripts\activate

macOS / Linux:
python3 -m venv venv
source venv/bin/activate


Kur aktivizohet, do shihni (venv) në terminal.

4️⃣ Instalimi i paketave të nevojshme

Të gjitha libraritë janë të deklaruara në requirements.txt.

Instalimi bëhet me një komandë:

pip install -r requirements.txt


📦 Paketat që instalohen:

requests

pandas

matplotlib

feedparser

beautifulsoup4

5️⃣ Struktura e projektit
MinistryOfFinance_ALB/
│
├── scrape_ministry.py          # Scraping i njoftimeve nga Ministria e Financave
├── world_bank_api.py           # API e Bankës Botërore (GDP Albania)
├── eu_open_data_api.py         # API e BE-së për projekte financiare
├── wikipedia_api.py            # Wikipedia API (informacion për ministrinë)
├── visualize_data.py           # Grafika dhe analiza vizuale
│
├── njoftime_financa.csv
├── world_bank_gdp.csv
├── eu_finance_projects.csv
├── wikipedia_finance.txt
│
├── requirements.txt
└── README.md

6️⃣ Ekzekutimi i skripteve (rend i saktë)

⚠️ Skripti duhet ekzekutuar në këtë rend, sepse disa krijojnë të dhëna që përdoren më pas.

6.1 Scraping i njoftimeve
python scrape_ministry.py


✔️ Krijon: njoftime_financa.csv

6.2 Marrja e të dhënave nga World Bank API
python world_bank_api.py


✔️ Krijon: world_bank_gdp.csv

6.3 Marrja e të dhënave nga EU Open Data API
python eu_open_data_api.py


✔️ Krijon: eu_finance_projects.csv

6.4 Marrja e informacionit nga Wikipedia API
python wikipedia_api.py


✔️ Krijon: wikipedia_finance.txt

7️⃣ Vizualizimi grafik i të dhënave
python visualize_data.py


📊 Ky skript:

lexon CSV-të e krijuara

gjeneron grafikë me ngjyra

analizon trendet ekonomike dhe institucionale

Nëse përdorni PyCharm:

grafikët hapen automatikisht në dritare