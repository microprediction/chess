from microprediction import MicroWriter
import json
import os 

# Microprediction writer 
write_key = os.environ.get('WRITE_KEY')    # GitHub action needs to set env variable. You need to create a GitHub secret called WRITE_KEY
if write_key is None:
   raise Exception('The write key was not injected into the environment ... this needs to be done by github actions perhaps')
print(write_key)
mw = MicroWriter(write_key=write_key)
assert mw.key_difficulty(mw.write_key)>=12, "You need a key of difficulty 12 to create a stream"
print(mw.animal)

# Chess.com 
URL_TEMPLATE = 'https://api.chess.com/pub/player/HANDLE/stats'
CATEGORIES = ['chess_blitz', 'chess_bullet']


# Streams
STREAM_URL_TEMPLATE = 'https://www.microprediction.org/stream_dashboard.html?stream=chess_CATEGORY_TYPE_HANDLE
STREAM_TYPES = ['daily','level','change']
ANALYSIS_DIR = 'analysis'

def stream_url(category,stream_type,handle):
     return STEAM_URL_TEMPLATE.replace('CATEGORY',category).replace('TYPE',stream_type).replace('HANDLE',handle)

   
# Active players
# (Try not to add if it will just create a constant stream)
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
          'chess_bullet':{'Hikaru': 'hikaru nakamura',
                   'Firouzja2003': 'alireza firouzja',
                   'DanielNaroditsky': 'daniel naroditsky',
                   'penguingm1':'andrew tang',
                    'wonderfultime':'tuan minh le',
                    'PinIsMightier':'peter cotton',
                    'FarOctopus':'morgan lu',
                     'sshivaji':'shivkumar shivaji',
                      '9epoch':'nathan szeitli',
                          'erik':'erick allebest',
                          'Trilobe8':'nik sykiotis'
                   },
          'chess_rapid':{'Hikaru': 'hikaru nakamura',
                         'Firouzja2003': 'alireza firouzja',
                         'GMWSO': 'wesley so',
                         'LyonBeast': 'maxime vachier lagrave',
                         'nihalsarin': 'nihal sarin',
                         'DanielNaroditsky': 'daniel naroditsky'}
                       }

if __name__=='__main__':
   from pprint import pprint
   pprint(ACTIVE)
   with open('players.json','wt') as f:
       json.dump(ACTIVE,f)
  
          
