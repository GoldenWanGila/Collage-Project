from bs4 import BeautifulSoup
import requests
from time import mktime
from datetime import datetime
from wsgiref.handlers import format_date_time
import hmac
from hashlib import sha1
import base64

APPID = "ea4357a24c3d4072a3b2d1b538f19984"
APPKEY = '5krzdQvXot_vms6ciqpR4emxoHE'

class Auth():

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def get_header(self):
        xdate = format_date_time(mktime(datetime.now().timetuple()))
        hashed = hmac.new(self.app_key.encode('utf8'), ('x-date: %s' %xdate).encode('utf8'), sha1)
        signature = base64.b64encode(hashed.digest()).decode()

        authorization = 'Authorization: hmac username="%s", algorithm="hmac-sha1", headers="x-date", signature="%s"' %(self.app_id, signature)

        return {'Authorization': authorization,
                'x-date': xdate,
                'Accept - Encoding': 'gzip'}

a = Auth(APPID, APPKEY)

URL = "https://ptx.transportdata.tw/MOTC/v2/Rail/TRA/LiveTrainDelay?$top=30&$format=XML"
myheaders = a.get_header()

response = requests.get(URL, headers = myheaders)
soup = BeautifulSoup(response.text, "html.parser")

print(response.status_code)
print(soup)