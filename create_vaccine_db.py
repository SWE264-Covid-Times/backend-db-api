import sqlite3
import pandas as pd
from datetime import date

conn = sqlite3.connect("covidtimesdata.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Vaccinations")
cur.execute("DROP TABLE IF EXISTS Provider")

cur.execute("CREATE TABLE Vaccinations(date DATE, county TEXT, fips INTEGER, doses_administered INTEGER, new_doses_administered INTEGER)")
cur.execute("CREATE TABLE Provider(zipcode INTEGER, provider TEXT, address TEXT, phone TEXT)")


vaccinationInfo = pd.read_csv('cdph-vaccination-county-totals.csv')
vaccinationInfo.to_sql('Vaccinations', conn, if_exists='append', index=False)

providerInfo = pd.read_csv('irvine_vaccines.csv')
providerInfo.to_sql('Provider', conn, if_exists='append', index=False)
conn.commit()
cur.close()