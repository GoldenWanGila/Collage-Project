import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)

weather_path = 'model/inputs/weather.json'
railway_path = 'model/inputs/railway.json'

weather_df = pd.read_json(weather_path)
railway_df = pd.read_json(railway_path)

weather_attribute = list(weather_df.data[2][0].keys())
weather_attribute.insert(0,'Date')
railway_attribute = list(railway_df.data[2][0].keys())
railway_attribute.insert(0,'Station_and_direction')

weather_input_list = []
for i in range(2,len(weather_df.name)):
    for j in range(len(weather_df.data[i])):
        data = list(weather_df.data[i][j].values())
        data.insert(0,weather_df.name[i])
        weather_input_list.append(data)

railway_input_list = []
for i in range(2,len(railway_df.name)):
    for j in range(len(railway_df.data[i])):
        data = list(railway_df.data[i][j].values())
        data.insert(0,railway_df.name[i])
        railway_input_list.append(data)

weather_input_df = pd.DataFrame(weather_input_list, columns=weather_attribute)
railway_input_df = pd.DataFrame(railway_input_list, columns=railway_attribute)

weather_input_df.to_csv('model/inputs/weather.csv')
railway_input_df.to_csv('model/inputs/railway.csv')