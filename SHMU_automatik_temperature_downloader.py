#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import re
import pandas as pd
import os
from datetime import datetime


# Aktuálny rok
rok = datetime.now().year

url = f"https://www.shmu.sk/sk/?id=klimat_operativneudaje1&identif=11816&obdobie=1991-2020&page=1&rok={rok}&sub=1"

r = requests.get(url)
r.raise_for_status()


# Vyhľadanie údajov o teplotách
zaciatok = r.text.find("wn_current_max_serie")
koniec = r.text.find("};", zaciatok)

data = r.text[zaciatok:koniec]


# Extrahovanie timestampov a teplôt
teploty = re.findall(
    r'\[(\d+),\s*(-?\d+(?:\.\d+)?)\]',
    data
)


# Vytvorenie DataFrame
df = pd.DataFrame(
    teploty,
    columns=["timestamp", "teplota"]
)


# Prevod timestampu na slovenský dátum
df["datum"] = (
    pd.to_datetime(df["timestamp"], unit="ms", utc=True)
    .dt.tz_convert("Europe/Bratislava")
    .dt.date
)


# Prevod teploty na číslo
df["teplota"] = pd.to_numeric(df["teplota"])


# Ponechanie potrebných stĺpcov
df = df[["datum", "teplota"]]


# Ak CSV už existuje, načítame existujúce údaje
if os.path.exists("teploty.csv"):

    df_existujuce = pd.read_csv("teploty.csv")

    df_existujuce["datum"] = pd.to_datetime(
        df_existujuce["datum"]
    ).dt.date

    # Spojenie starých a nových údajov
    df = pd.concat(
        [df_existujuce, df],
        ignore_index=True
    )

    # Odstránenie duplicitných dátumov
    df = df.drop_duplicates(
        subset="datum",
        keep="first"
    )

    # Zoradenie podľa dátumu
    df = df.sort_values("datum")


# Uloženie údajov do CSV
df.to_csv("teploty.csv", index=False)


# In[ ]:




