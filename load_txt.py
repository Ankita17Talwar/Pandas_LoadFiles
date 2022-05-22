import pandas as pd

df = pd.read_csv('supermarkets/supermarkets-commas.txt')
print(df)

df = pd.read_csv('supermarkets/supermarkets-semi-colons.txt', sep=';')
print(df)

print(df.drop(df.index[0:3],0))
