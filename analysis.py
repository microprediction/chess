# Personalized analysis... more to come
from config import ACTIVE, URL_TEMPLATE
import os

STREAM_URL_TEMPLATE = 'https://www.microprediction.org/stream_dashboard.html?stream=chess_CATEGORY_TYPE_HANDLE
TYPES = ['daily','level','change']
ANALYSIS = 'analysis'

def stream_url(category,stream_type,handle):
     return STEAM_URL_TEMPLATE.replace('CATEGORY',category).replace('TYPE',stream_type).replace('HANDLE',handle)

def summary_dump():
  for category in ACTIVE.keys():
      for handle, player in ACTIVE[category].items():
           player = {'urls':{'stats':'URL_TEMPLATE.replace('HANDLE', handle.lower())',
                    'level': stream_url(category=category,handle=handle, stream_type='level'),
                    'change':stream_url(category=category,handle=handle, stream_type='level'),
                    'daily':stream_url(category=category,handle=handle, stream_type='daily')}}
           directory = ANALYSIS+os.path.sep+handle.lower()
           summary_file = directory+os.path.sep+'summary.json'
           try:
              os.mkdirs(directory)
           except Exception as e:
              print(e)
           with open(summary_file,'wt') as f:
              json.dump(summary_file,summary)

 
if __name__=='__main__':
    dump_summary()
          
