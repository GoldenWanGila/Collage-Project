from bs4 import BeautifulSoup
import requests
import openpyxl
import time


station_name = ['台中']
station_num = ['467490']

"""儲存檔案要用的相關參數"""
wb = openpyxl.Workbook()
row = 1
column = 0
ws = wb.create_sheet(station_name[0], 0)

"""用於設定要爬取的日期(crawlDate)和儲存檔案要用的日期(fileDate)"""
local_time = time.localtime()
date = {"year": str(local_time.tm_year), "month": str(local_time.tm_mon), "day": str(local_time.tm_mday - 1)}
date["month"] = "0" + date["month"] if len(date["month"]) == 1 else date["month"]
date["day"] = "0" + date["day"] if len(date["day"]) == 1 else date["day"]
fileDate = date["year"] + date["month"] + date["day"]
crawlDate = date["year"] + "-" + date["month"] + "-" + date["day"]

url = 'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=%s&stname=%s&datepicker=%s' %(station_num[0], '%25E8%2587%25BA%25E4%25B8%25AD', crawlDate)

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

all_tr = soup.find('tbody').find_all('tr')

for index2 in range(3, 27):
    td_in_tr = all_tr[index2].find_all('td')
    for td in td_in_tr:
        column += 1
        td_reformat = td.get_text() - ' ' if ' ' in td.get_text() else td.get_text()
        ws.cell(row=row, column=column, value=td_reformat)
    if column == 17:
        row += 1
        column = 0

wb.save(r"Data\Weather\Data collector %s.xlsx" %crawlDate)