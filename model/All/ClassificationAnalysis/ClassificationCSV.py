import pandas as pd

path = 'model/inputs/railway.csv'
data = pd.read_csv(path)

value_lists = []
label_list = data.columns.tolist()
for label in data.columns:
    value_lists.append(data[label].tolist())

type_dict = dict(zip(['A','B','C','D'],[1,2,3,4]))

table_dict = dict(zip(label_list,value_lists))
for index in range(len(table_dict['direction'])):
    table_dict['direction'][index] = 0 if table_dict['direction'][index]==0 else 1
    table_dict['time'][index]
    if int(table_dict['time'][index][0:2]) >= 6 and int(table_dict['time'][index][0:2]) < 9:
        table_dict['time'][index] = '1'
    elif int(table_dict['time'][index][0:2]) >= 17 and int(table_dict['time'][index][0:2]) < 20:
        table_dict['time'][index] = '2'
    else:
        table_dict['time'][index] = '0'
    table_dict['type'][index] = type_dict[table_dict['type'][index]]


store = pd.DataFrame(table_dict, columns=label_list)
print(store.head())

store.to_csv('model/ClassificationAnalysis/inputs/railway.csv',index_label=False)