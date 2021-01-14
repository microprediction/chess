import os
from getjson import getjson
from microprediction import MicroWriter

write_key = os.environ.get('WRITE_KEY')    # GitHub action needs to set env variable. You need to create a GitHub secret called WRITE_KEY
mw = MicroWriter(write_key=write_key)
assert mw.key_difficulty(mw.write_key)>=12, "You need a key of difficulty 12 to create a stream"

PLAYERS = {'Hikaru': 'hikaru_nakamura',
           'Firouzja2003': 'alireza_firouzja',
           'GMWSO': 'wesley_so',
           'LyonBeast': 'maxime_vachier_lagrave',
           'nihalsarin': 'nihal_sarin',
           'DanielNaroditsky': 'daniel_naroditsky',
           'PinIsMightier': 'halloween_gambit'}

URL_TEMPLATE = 'https://api.chess.com/pub/player/HANDLE/stats'
CATEGORIES = ['chess_blitz', 'chess_bullet']

if __name__ == '__main__':
    for category in CATEGORIES:
        for handle, player in PLAYERS.items():
            url = URL_TEMPLATE.replace('HANDLE', handle.lower())
            data = getjson(url)
            if data is not None:
                current_value = int(data[category]['last']['rating'])
                level_name = category + '_level_'  + handle + '.json'         # Name of stream with rating level
                try:
                    previous_value = int(mw.get_current_value(name=level_name))
                except:
                    previous_value = None                       # Might not exist yet
                if previous_value is None:
                    print( (level_name, current_value, mw.set(name=level_name,value=current_value) ) )
                else:
                    if int(previous_value) != int(current_value):  
                        print( (level_name, current_value, mw.set(name=level_name,value=current_value) ) )
                        print( level_name+' updated to '+str(current_value) )
                    else:
                        print( (level_name, current_value, 'unchanged') )
            else:
                print(url)
           
      
