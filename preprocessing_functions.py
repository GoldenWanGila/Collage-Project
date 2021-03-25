# 事故、平假日分開、尖峰離峰
from datetime import datetime

# date = '20210328'

def Weekday_decide(date):
    weekday_dict = {0:1,1:2,2:3,3:4,4:5,5:6,6:7}
    year = int(date[0:4])
    month = int(date[4:6]) if date[4] != '0' else int(date[5])
    day = int(date[6:8])
    weekday = weekday_dict[datetime(year,month,day).weekday()]
    return weekday

def Day_End(weekday):
    if weekday == 6 or weekday == 7:
        return 'weekend'
    else:
        return 'weekday'

# print(Weekday_decide(date))
# print(Day_End(Weekday_decide(date)))

# time = '09:26'

def Time_discrete(time):
    hour = int(time[0:2]) if time[0] != 0 else int(time[1])
    # EX: 5:00~5:59 --> 06
    return('0' + str(hour+1) if time[0] == 0 else str(hour+1))

# print(Time_discrete(time))

def Traintype_to_number(traintype):
    traintype_list = ['區間','區間快','自強','普悠瑪','太魯閣']
    note_number = 0
    for item in traintype_list:
        if traintype == item:
            return note_number
        note_number += 1