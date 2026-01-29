import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib
matplotlib.use("TkAgg")  # ndrysho backend
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

njoftime = pd.read_csv(os.path.join(BASE_DIR, "njoftime_financa.csv"))
world_bank = pd.read_csv(os.path.join(BASE_DIR, "world_bank_gdp.csv"))
eu = pd.read_csv(os.path.join(BASE_DIR, "eu_finance_projects.csv"))

# 1️⃣ Numri i njoftimeve sipas viteve
njoftime_per_year = njoftime["year"].value_counts().sort_index()
plt.figure(figsize=(8,5))
njoftime_per_year.plot(kind="bar", color="#3498db")  # blu profesional
plt.title("Numri i Njoftimeve për Ministrinë e Financave")
plt.xlabel("Viti")
plt.ylabel("Numri i Njoftimeve")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# 2️⃣ GDP per capita (World Bank)
plt.figure(figsize=(8,5))
plt.plot(world_bank["year"], world_bank["gdp_per_capita"], marker="o", color="#2ecc71", linewidth=2)
plt.title("GDP per Capita Shqipëri (World Bank)")
plt.xlabel("Viti")
plt.ylabel("GDP per Capita (USD)")
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# 3️⃣ Projekte EU sipas viteve
eu["year"] = pd.to_numeric(eu["year"], errors="coerce")
eu_projects = eu["year"].value_counts().sort_index()
plt.figure(figsize=(8,5))
eu_projects.plot(kind="bar", color="#e67e22")  # portokalli
plt.title("Projekte të BE për Financat sipas Vitit")
plt.xlabel("Viti")
plt.ylabel("Numri i Projekteve")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
