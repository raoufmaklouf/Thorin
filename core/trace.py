import requests
import re
from core import regex
from core import nano




def trace_(url):
    
   
    for a,b in regex.REGEX_URL.items():
        mutch=re.search(b, url)
        if(mutch):
            mutch_=mutch.group()
            
            try:
                resp = requests.get(url)
                scode=resp.status_code
                if str(scode)[0] =='2':
                    r="\033[32m[{}]\033[00m".format(str(scode))
                elif  str(scode)[0] =='3':            
                    r="\033[36m[{}]\033[00m".format(str(scode))
                elif  str(scode)[0] =='4':
                    r="\033[95m[{}]\033[00m".format(str(scode))
                elif  str(scode)[0] =='5':
                    r="\033[35m[{}]\033[00m".format(str(scode))
                else:
                    r=scode
                print("\033[94m[INFO]\033[00m\033[33m[{}]\033[00m{}  {}".format(a.rstrip(),r,nano.search_color(str(mutch_),url)))
            except:
                pass
        else:
            pass
