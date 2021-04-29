import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)

type_dict = {'普悠瑪':'A','太魯閣':'A','自強':'B','復興':'B','莒光':'C','區間':'D','區間快':'D'}
station_name_chinese = ['七堵','二水','三義','大甲','中壢','內灣','六家','斗六','斗南','北湖','民雄',
                        '永康','田中','后里','汐止','竹北','竹東','竹南','志學','沙崙','沙鹿','車埕',
                        '宜蘭','松山','枋寮','知本','花蓮','南港','南澳','屏東','苗栗','員林','桃園',
                        '高雄','基隆','通霄','善化','湖口','新烏日','新左營','新營','新竹','楊梅','壽豐',
                        '彰化','瑞芳','嘉義','福隆','臺中','臺北','臺北-環島','臺東','臺南','鳳林','銅鑼',
                        '潮州','樹林','豐原','雙溪','蘇澳','蘇澳新','鶯歌','太原','板橋','潭子']
station_name_english = ['Qidu','Ershui','Sanyi','Dajia','Zhongli','Neiwan','Liujia','Douliu','Dounan','Beihu','MinXiong',
                        'Yongkang','Tianzhong','Houli','Xizhi','Zhubei','Zhudong','Zhunan','Zhixue','Shalun','Shalu',
                        'Checheng','Yilan','Songshan','Farliao','Zhiben','Hualien','Nangang','Nan ao','Pingtung','Miaoli',
                        'Yuanlin','Taoyuan','Kaohsiung','Keelung','Tongxiao','Shanhua','Hukou','Xinwuri','Xinzuoying',
                        'Xinying','Hsinchu','Yangmei','Shoufeng','Changhua','Ruifang','Chiayi','Fulong','Taichung','Taipei',
                        'Taipei Surround Island','Taitung','Tainan','Fenglin','Tongluo','Chaozhou','Shulin','Fengyuan','Shuaxgxi',
                        'Su ao','Su aoxin','Yingge','Taiyuan','Banqiao','Tanzi']

station_name_dict = dict(zip(station_name_chinese,station_name_english))
direction_dict = {'逆行':'0','順行':'1'}

weather_path = 'model/inputs/weather.json'
railway_path = 'model/inputs/railway.json'

weather_df = pd.read_json(weather_path)
railway_df = pd.read_json(railway_path)
weather_attribute = list(weather_df.data[2][0].keys())
weather_attribute.insert(0,'Date')
railway_attribute = list(railway_df.data[2][0].keys())
railway_attribute.insert(0,'Station')
railway_attribute.insert(1,'direction')

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
        data[-1] = type_dict[data[-1]]
        data[-3] = station_name_dict[data[-3]]
        data.insert(0,railway_df.name[i])
        data.insert(1,railway_df.name[i])
        data[0] = station_name_dict[data[0][:-4]]
        data[1] = direction_dict[data[1][-3:-1]]
        railway_input_list.append(data)

weather_input_df = pd.DataFrame(weather_input_list, columns=weather_attribute)
railway_input_df = pd.DataFrame(railway_input_list, columns=railway_attribute)

weather_input_df.to_csv('model/inputs/weather.csv', index_label=False)
railway_input_df.to_csv('model/inputs/railway.csv', index_label=False)