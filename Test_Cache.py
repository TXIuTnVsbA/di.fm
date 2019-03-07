# -*- coding: utf-8 -*-
import requests
import json
requests.packages.urllib3.disable_warnings()
if __name__ == "__main__":
    url="https://www.di.fm/_papi/v1/di/currently_playing"
    text = requests.get(url).text
    tmp= json.loads(text)
    for x in tmp:
        print(x['channel_key'] + "(" + str(x['channel_id']) + ")" + ": " +
              x['track']['display_artist'] + " - " + x['track']['display_title'] +
              "\thttps://www.di.fm/tracks/" + str(x['track']['id']))
