# Data Attribute Expalanation
#### 本檔案用於說明 railway.csv 以及 weather.csv 中的 attributes
****
****
* ## railway.csv
    * ### station：準備發車的車站
    * ### direction：火車的順逆行(0->逆行；1->順行)
    * ### id：當日的發車編號
    * ### date：當日日期
    * ### time：火車的預計離站時間(沒有包含誤點)
    * ### num：列車車次
    * ### dest：此班列車的終點站
    * ### delay：火車確實離站時間-預計離站時間
    * ### type：火車車種(A->(普悠瑪、太魯閣)；B->(自  強、復興)；C->莒光；D->(區間、區間快))
* ## weather.csv
    * ### Date：當日日期
    * ### Obs time：資料紀錄時間
    * ### Stn Pres：測站氣壓(hPa)
    * ### Sea Pres：海平面氣壓(hPa)
    * ### Temperature：溫度(C)
    * ### Td_Dew_point：露點溫度(C)
    * ### RH：相對溼度(%)
    * ### WS：風速(m/s)
    * ### WD：風向(360 degree)
    * ### WSGust：最大陣風風速(m/s)
    * ### WDGust：最大陣風風向(m/s)
    * ### Precp：降水量(mm)
    * ### Precp Hour：降水時數(hrs)
    * ### Sun Shine：日照時數(hrs)
    * ### Globl Rad：全天空日射量(MJ/m*m)
    * ### Visb：能見度(km)
    * ### UVI：紫外線指數
    * ### Cloud Amount：總雲量(0~10)