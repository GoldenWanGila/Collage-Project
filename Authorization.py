from bs4 import BeautifulSoup
import requests
from time import mktime
from datetime import datetime
from wsgiref.handlers import format_date_time
import hmac
from hashlib import sha1
import base64

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
                'Accept - Encoding': 'gzip, deflate'}