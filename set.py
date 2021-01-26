# This script is run elsewhere, so as not to tax GitHub actions

from getjson import getjson
from config import ACTIVE, URL_TEMPLATE, mw
import time

if __name__ == '__main__':
        start_time = time.time()
        for category in ACTIVE.keys():
            for handle, player in ACTIVE[category].items():
                url = URL_TEMPLATE.replace('HANDLE', handle.lower())
                data = getjson(url)
                if data is not None:
                    if data.get(category):
                        current_value = int(data[category]['last']['rating'])
                        level_name = category + '_level_'  + handle + '.json'         # Name of stream with rating level
                        change_name = category + '_change_'  + handle + '.json'       # Name of stream with rating changes
                        previous_value = mw.get_current_value(name=level_name)
                        if previous_value is None:
                            mw.set(name=level_name,value=current_value)
                            mw.set(name=change_name,value=0)
                        else:
                            if int(float(previous_value)) != int(float(current_value)):
                                mw.set(name=level_name,value=current_value)
                                mw.set(name=change_name,value=float(current_value)-float(previous_value))
                                print( level_name+' updated to '+str(current_value) )
                            else:
                                mw.touch(name=level_name)
                                mw.touch(name=change_name)
       
