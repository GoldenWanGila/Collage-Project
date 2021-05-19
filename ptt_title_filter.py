from bs4 import BeautifulSoup
import requests
import openpyxl

keyword = ['事故','故障','落軌','外物','入侵','停駛','死傷','誤點']

url = 'https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip111/view'

responses = requests.get(url)
soup = BeautifulSoup(responses.text, "html.parser")

trainNames_soup = soup.find_all(class_='traincode_name1')
trainNames_text = []
for trainName in trainNames_soup:
    if trainName.get_text() == '民族':
        break
    else:
        trainNames_text.append(trainName.get_text())

print(trainNames_text)