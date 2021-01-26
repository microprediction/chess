from config import ACTIVE, URL_TEMPLATE, STREAM_URL_TEMPLATE, STREAM_TYPES, ANALYSIS_DIR, stream_url, HOME_TEMPLATE
import os
import json
from pprint import pprint
import errno
from json2html import *
import torsimany
from torsimany.torsimany import parseJSON

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
           summary_json_file = directory+os.path.sep+'locations.json'
           summary_html_file = directory+os.path.sep+'locations.html'
           summary_md_file = directory+os.path.sep+'locations.md'
            
           
            
           try:
              os.makedirs(directory)
           except OSError as e:
              if e.errno != errno.EEXIST:
                  os.makedirs(directory)
                  
           with open(summary_json_file,'wt') as fp:
              json.dump(summary,fp=fp)
              
           summary_html = json2html.convert(summary)
           with open(summary_html_file,'wt') as fp:
               fp.write(summary_html)
                
           summary_md = parseJSON(summary, depth=0)
           with open(summary_md_file,'wt') as fp:
               fp.write(summary_md) 

 
if __name__=='__main__':
    dump_summary()
