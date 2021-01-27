from bs4 import BeautifulSoup
import requests
import openpyxl
import time
import re

"""儲存檔案要用的相關參數"""
wb = openpyxl.Workbook()
row = 1
column = 0
sheet_position = 0

"""欲爬取的站號與站名"""
station_num = ["3230","3280","3300","3350","3340","3360","3390","0900","0960","1000","1020","1080","1100","1250","3160","3470","4080","4220","4340","4400"]
station_name = ["豐原","太原","臺中","潭子","新烏日","彰化","員林","基隆","汐止","臺北","板橋","桃園","中壢","竹南","苗栗","斗六","嘉義","臺南","新左營","高雄"]

"""用於設定要爬取的日期(rideDate)和儲存檔案要用的日期(fileDate)"""
local_time = time.localtime()
date = {"year": str(local_time.tm_year), "month": str(local_time.tm_mon), "day": str(20)}
rideDate = date["year"] + "/" + date["month"] + "/" + date["day"]
# 為了將檔案格式統一化，所以對month和day進行調整
date["month"] = "0" + date["month"] if len(date["month"]) == 1 else date["month"]
date["day"] = "0" + date["day"] if len(date["day"]) == 1 else date["day"]
fileDate = date["year"] + date["month"] + date["day"]

"""主要執行的程式"""
for index in range(len(station_num)):
    url_byStation = ("https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybystationblank?rideDate=%s&station=%s-%s" %(rideDate, station_num[index], station_name[index]))
    # print(url_byStation)        # For test

    responses = requests.get(url_byStation)
    soup_byStation = BeautifulSoup(responses.text, "html.parser")

    all_tbody = soup_byStation.find_all(class_="tab-pane")
    # all_tbody[index] : index = 0       --> 順行
    #                    index = 1       --> 逆行

    # 順行
    ws = wb.create_sheet("%s(順行)" % station_name[index], sheet_position)
    all_item = all_tbody[0].find_all("td")
    # all_item[index] : index = 6C      --> 排序編號
    #                   index = 1+6C    --> 車種+車次(起點->終點)
    #                   index = 2+6C    --> 預計進站時間
    #                   index = 3+6C    --> 終點站站名 
    #                   index = 4+6C    --> 此班列車行駛狀態
    #                   index = 5+6C    --> 台鐵實際進站狀態
    for item in all_item:
        column += 1
        ws.cell(row = row, column = column, value = item.get_text())
        if column == 6:
            row += 1
            column = 0
    row = 1

    #逆行
    ws = wb.create_sheet("%s(逆行)" % station_name[index], sheet_position+1)
    all_item = all_tbody[1].find_all("td")
    sheet_position += 2
    
    for item in all_item:
        column += 1
        ws.cell(row = row, column = column, value = item.get_text())
        if column == 6:
            row += 1
            column = 0
    row = 1

wb.save(r"Data\Railway\Data collector %s.xlsx" %fileDate)
