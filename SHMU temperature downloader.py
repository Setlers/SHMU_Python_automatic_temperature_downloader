#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

url = "https://www.shmu.sk/sk/?id=klimat_operativneudaje1&identif=11816&obdobie=1991-2020&page=1&rok=2026&sub=1"

r = requests.get(url)

# print(r.status_code)

# TU ZAČÍNAME PRACOVAŤ S ÚDAJMI
zaciatok = r.text.find("wn_current_max_serie")
koniec = r.text.find("};", zaciatok)

data = r.text[zaciatok:koniec]

# print(data[:500])

import re

teploty = re.findall(r'\[(\d+),\s*(-?\d+(?:\.\d+)?)\]', data)

# print(teploty[:5])

import pandas as pd

df = pd.DataFrame(teploty, columns=["timestamp", "teplota"])

# print(df.head())

df["datum"] = pd.to_datetime(df["timestamp"], unit="ms")
df["teplota"] = pd.to_numeric(df["teplota"])
# print(df.head())

df["datum"] = df["datum"].dt.date

# print(df.head())

df = df[["datum", "teplota"]]

# print(df.head())

df.to_csv("teploty.csv", index=False)

df = pd.read_csv("teploty.csv")

# print(df)

df.loc[len(df)] = ["2026-09-09", 25.3]

df.to_csv("teploty.csv", index=False)

# print(df)

posledny = teploty[-1]

# print(posledny)

timestamp, teplota = posledny

datum = pd.to_datetime(int(timestamp), unit="ms").date()
teplota = float(teplota)

# print(datum, teplota)

df.loc[len(df)] = [datum, teplota]

df.to_csv("teploty.csv", index=False)

# print(df.tail())

# print(teploty[-5:])

if datum not in df["datum"].values:
    df.loc[len(df)] = [datum, teplota]
    df.to_csv("teploty.csv", index=False)

posledny = teploty[-1]

timestamp, teplota = posledny

datum = pd.to_datetime(int(timestamp), unit="ms").date()
teplota = float(teplota)

if datum not in df["datum"].values:
    df.loc[len(df)] = [datum, teplota]
    df.to_csv("teploty.csv", index=False)

