from microprediction import MicroWriter
import json
import os 

# Microprediction writer 
write_key = os.environ.get('WRITE_KEY')    # GitHub action needs to set env variable. You need to create a GitHub secret called WRITE_KEY
mw = MicroWriter(write_key=write_key)
assert mw.key_difficulty(mw.write_key)>=12, "You need a key of difficulty 12 to create a stream"

# Chess.com 
URL_TEMPLATE = 'https://api.chess.com/pub/player/HANDLE/stats'
CATEGORIES = ['chess_blitz', 'chess_bullet']

# Active players
ACTIVE = {'chess_blitz':{'Hikaru': 'hikaru_nakamura',
                    'Firouzja2003': 'alireza_firouzja',
                    'nihalsarin':'nihal_sarin',
                    'DanielNaroditsky': 'daniel_naroditsky',
                    'FarOctopus':'morgan_lu',
                    'viswanath270':'viswanath thatha',
                     'sshivaji':'shivkumar shivaji',
                    'viswanath270':'viswanath thatha',
                          'caldyc':'chris calderwood',
                          'swamijs':'swamijs',
                         '9epoch':'nathan szeitli',
                         'erik':'erick allebest',    # Founder of chess.com 
                         'Trilobe8':'nik sykiotis'
                  },
          'chess_bullet':{'Hikaru': 'hikaru_nakamura',
                   'Firouzja2003': 'alireza_firouzja',
                   'DanielNaroditsky': 'daniel_naroditsky',
                   'penguingm1':'andrew_tang',
                    'wonderfultime':'tuan_minh_le',
                    'PinIsMightier':'peter_cotton',
                    'FarOctopus':'morgan_lu',
                     'sshivaji':'shivkumar shivaji',
                      '9epoch':'nathan szeitli',
                          'erik':'erick allebest',
                          'Trilobe8':'nik sykiotis'
                   },
          'chess_rapid':{'Hikaru': 'hikaru_nakamura',
                         'Firouzja2003': 'alireza_firouzja',
                         'GMWSO': 'wesley_so',
                         'LyonBeast': 'maxime_vachier_lagrave',
                         'nihalsarin': 'nihal_sarin',
                         'DanielNaroditsky': 'daniel_naroditsky',
                         'PinIsMightier': 'halloween_gambit'}
                       }

if __name__=='__main__':
   # Ensures no syntax errors
   from pprint import pprint
   pprint(ACTIVE)
   with open('players.json') as f:
       json.dump(ACTIVE,f)
