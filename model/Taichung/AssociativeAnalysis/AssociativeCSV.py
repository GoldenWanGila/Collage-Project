import pandas as pd
from datetime import datetime

path = r'model/Taichung/inputs/railway.csv'
data = pd.read_csv(path)

# print(data)
# exit()

value_lists = []
label_list = data.columns.tolist()
for label in data.columns:
    value_lists.append(data[label].tolist())

table_dict = dict(zip(label_list,value_lists))
for index in range(len(table_dict['direction'])):
    # 順逆行
    table_dict['direction'][index] = 'backward' if table_dict['direction'][index]==0 else 'forward'
    # 誤點
    if table_dict['delay'][index] == 0:
        table_dict['delay'][index] = 'no_delay'
    elif table_dict['delay'][index] <= 5:
        table_dict['delay'][index] = 'short_delay'
    else:
        table_dict['delay'][index] = 'long_delay'
    # 發車時間
    if int(table_dict['time'][index]) == 1:
        table_dict['time'][index] = 'to_work'
    elif int(table_dict['time'][index]) == 2:
        table_dict['time'][index] = 'off_work'
    else:
        table_dict['time'][index] = 'not_commuting_time'
    # 日期
    date = datetime(year=int(table_dict['date'][index][0:4]),month=int(table_dict['date'][index][5:7]),day=int(table_dict['date'][index][8:10]))
    if date.isoweekday() < 6:
        table_dict['date'][index] = 'weekday'
    else:
        table_dict['date'][index] = 'weekend'


store = pd.DataFrame(table_dict, columns=label_list)
print(store.head())

store.to_csv(r'model/Taichung/AssociativeAnalysis/inputs/railway.csv',index_label=False)