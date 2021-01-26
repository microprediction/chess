from config import ACTIVE, URL_TEMPLATE, STREAM_URL_TEMPLATE, STREAM_TYPES, ANALYSIS_DIR, stream_url, HOME_TEMPLATE
import os
import json
from pprint import pprint
import errno

def dump_summary():
  CATEGORIES = ACTIVE.keys()
  for category in ACTIVE.keys():
      for handle, player in ACTIVE[category].items():
           summary = {'urls':{'stats':URL_TEMPLATE.replace('HANDLE', handle.lower() ),
                              'home':HOME_TEMPLATE.replace('HANDLE', handle.lower() ),
                              'level': stream_url(category=category,handle=handle, stream_type='level'),
                              'change':stream_url(category=category,handle=handle, stream_type='change'),
                              'daily':stream_url(category=category,handle=handle, stream_type='daily')}}
           pprint(summary)
           directory = ANALYSIS_DIR+os.path.sep+handle.lower()+os.path.sep+category
           summary_file = directory+os.path.sep+'summary.json'
            
           try:
              os.makedirs(directory)
           except OSError as e:
              if e.errno != errno.EEXIST:
                  os.makedirs(directory)
                  
           with open(summary_file,'wt') as f:
              json.dump(summary,summary_file)

 
if __name__=='__main__':
    dump_summary()
