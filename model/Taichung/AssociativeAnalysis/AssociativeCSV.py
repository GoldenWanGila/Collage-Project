import pandas as pd

path = r'model/Taichung/inputs/railway.csv'
data = pd.read_csv(path)

# print(data.head())
# exit()

value_lists = []
label_list = data.columns.tolist()
for label in data.columns:
    value_lists.append(data[label].tolist())

table_dict = dict(zip(label_list,value_lists))
for index in range(len(table_dict['direction'])):
    table_dict['direction'][index] = 'backward' if table_dict['direction'][index]==0 else 'forward'
    if table_dict['delay'][index] == 0:
        table_dict['delay'][index] = 'no_delay'
    elif table_dict['delay'][index] <= 5:
        table_dict['delay'][index] = 'short_delay'
    else:
        table_dict['delay'][index] = 'long_delay'
    table_dict['time'][index]
    if int(table_dict['time'][index]) == 1:
        table_dict['time'][index] = 'to_work'
    elif int(table_dict['time'][index]) == 2:
        table_dict['time'][index] = 'off_work'
    else:
        table_dict['time'][index] = 'not_commuting_time'


store = pd.DataFrame(table_dict, columns=label_list)
print(store.head())

store.to_csv(r'model/Taichung/AssociativeAnalysis/inputs/railway.csv',index_label=False)