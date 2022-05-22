import pandas as pd


df = pd.read_excel('supermarkets/supermarkets.xlsx', engine='openpyxl',sheet_name=0 )
print(df)