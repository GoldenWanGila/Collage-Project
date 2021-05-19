import pandas

path = r'model\inputs\railway.csv'
data = pandas.read_csv(path)
data = data[0:5].copy()

print(data['time'][data[data['num']==167 and data['Station']=='Chiayi'].index])