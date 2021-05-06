import pandas as pd

path = 'model/AssociativeAnalysis/inputs/railway.csv'
data = pd.read_csv(path)

# print(data.head())
# exit()

attributes = ['Station','direction','time','dest','delay','type']

def listCreator(df : pd.core.series.Series) -> list[str]:
    list = []
    for item in df:
        if item not in list:
            list.append(item)
    return list

file = open(r'Statistics\statisticResult.txt','w')
file.write('Total number of data : %s\n' %len(data))

for attribute in attributes:
    list = listCreator(data[attribute])
    file.write('\nThe number of every -%s-\n' %attribute)
    for item in list:
        file.write(str(item) + ' : %d\n' %(data[attribute].tolist().count(item)))

file = open(r'Statistics\probabilityResult.txt','w')
file.write('Total number of data : %s\n' %len(data))

for attribute in attributes:
    list = listCreator(data[attribute])
    file.write('\nThe probabilities of every -%s-\n' %attribute)
    for item in list:
        file.write(str(item) + ' : %.4f\n' %(data[attribute].tolist().count(item)/len(data)))