import requests
import re
from core import regex
from core import nano




def trace_(url):
    
   
    for a,b in regex.REGEX_URL.items():
        mutch=re.search(b, url)
        #for i in mutch:
            #print(i)
        
        if(mutch): 
            mutch_=mutch.group()
            
            
            try:
                resp = requests.get(url)
                scode=resp.status_code
                if '2' in str(scode) :
                    r="\033[32m[{}]\033[00m".format(str(scode))
                elif  '3' in str(scode):
                    r="\033[36m[{}]\033[00m".format(str(scode))
                elif '4' in  str(scode) :
                    r="\033[95m[{}]\033[00m".format(str(scode))
                elif '5' in str(scode) :
                    r="\033[35m[{}]\033[00m".format(str(scode))
                else:
                    r=scode
                print("\033[94m[INFO]\033[00m\033[33m[{}]\033[00m{}  {}".format(a.rstrip(),r,nano.search_color(str(mutch_),url)))
            except:
                pass
        else:
            pass
if __name__=="__main__":
     trace_("http://belbana.com/scripts/swfobject.sql")
           
            
            
