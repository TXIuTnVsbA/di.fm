# -*- coding: utf-8 -*-
import requests
import re
requests.packages.urllib3.disable_warnings()
if __name__ == "__main__":
    url="https://www.di.fm/tracks/2902342"
    tmp = requests.get(url).text
    print(re.findall(r'\"url\":\"//(.*?)\"',tmp))
