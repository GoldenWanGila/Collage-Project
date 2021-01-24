import pandas as pd

df = pd.read_json('http://ods.railway.gov.tw/tra-ods-web/ods/download/dataResource/8ae4cabf6973990e0169947ed32454b9')
df.to_excel('everydayeverystation.xlsx')