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

URL_TEMPLATE = 'https://api.chess.com/pub/player/PLAYER/stats'
CATEGORIES = ['chess_blitz', 'chess_bullet']

if __name__ == '__main__':
    # Chess.Com ratings
    for category in CATEGORIES:
        for handle, player in PLAYERS.items():
            url = URL_TEMPLATE.replace('PLAYER', handle)
            data = getjson(url)
            try:
                value = data[category]['last']['rating']
                name = category + '_' + player + '.json'
                print( (name, value, mw.set(name=name,value=value) ) )
            except:
                print(data)

      
