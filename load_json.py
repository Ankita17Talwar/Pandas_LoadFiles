import pandas as pd
from geopy.geocoders import ArcGIS
import os

print(os.listdir())


df = pd.read_json('supermarkets/supermarkets.json')
print(df)

# converting address to coordinates
nom = ArcGIS()
n = nom.geocode("3995 23rd St, San Francisco, CA 94114")
print(n)
print(n.latitude)
print(n.longitude)


df['Address_new'] = df["Address"] +', ' + df['City'] +', ' + df['State'] +', ' + df['Country']
#print(df)
df['Coordinates'] = df["Address_new"].apply(nom.geocode)
print(df['Coordinates'][0].latitude)

df['Latitude']= df['Coordinates'].apply(lambda x: x.latitude if x != None else None)
print(df)
df['Longitude']= df['Coordinates'].apply(lambda x: x.longitude if x != None else None)
print(df)

