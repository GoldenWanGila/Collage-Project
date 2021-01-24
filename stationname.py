import pandas as pd

df = pd.read_json('http://ods.railway.gov.tw/tra-ods-web/ods/download/dataResource/0518b833e8964d53bfea3f7691aea0ee')
df.to_excel('stationname.xlsx')