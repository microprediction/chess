import os
from getjson import getjson
from microprediction import MicroWriter
from config import ACTIVE, mw, URL_TEMPLATE

if __name__ == '__main__':
    for category in CATEGORIES:
        for handle, player in ACTIVE.items():
            url = URL_TEMPLATE.replace('HANDLE', handle)
            data = getjson(url)
            try:
                value = data[category]['last']['rating']
                name = category + '_daily_' + handle + '.json'
                print( (name, value, mw.set(name=name,value=value) ) )
            except:
                print(data)
