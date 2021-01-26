from getjson import getjson
from config import ACTIVE, URL_TEMPLATE, mw

if __name__ == '__main__':
    for category in ACTIVE.keys():
        for handle, player in ACTIVE[category].items():
            url = URL_TEMPLATE.replace('HANDLE', handle.lower())
            data = getjson(url)
            if data is not None:
                if data.get(category):
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
                    print(player+ ' has never played '+category)
            else:
                print(url)
           
      
