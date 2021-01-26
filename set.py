import os
from getjson import getjson
from microprediction import MicroWriter
from config import ACTIVE, URL_TEMPLATE, CATEGORIES

write_key = os.environ.get('WRITE_KEY')    # GitHub action needs to set env variable. You need to create a GitHub secret called WRITE_KEY
mw = MicroWriter(write_key=write_key)
assert mw.key_difficulty(mw.write_key)>=12, "You need a key of difficulty 12 to create a stream"

if __name__ == '__main__':
    for category in CATEGORIES:
        for handle, player in ACTIVE[category].items():
            url = URL_TEMPLATE.replace('HANDLE', handle.lower())
            data = getjson(url)
            if data is not None:
                current_value = int(data[category]['last']['rating'])
                level_name = category + '_level_'  + handle + '.json'         # Name of stream with rating level
                previous_value = mw.get_current_value(name=level_name)
                if previous_value is None:
                    print('No previous value for '+level_name)
                    print( mw.set(name=level_name,value=current_value) )
                else:
                    if int(float(previous_value)) != int(float(current_value)):  
                        print( mw.set(name=level_name,value=current_value) ) 
                        print( level_name+' updated to '+str(current_value) )
                    else:
                        print( (level_name, current_value, ' is unchanged') )
                        print( mw.touch(name=level_name) ) 
            else:
                print(url)
           
      
