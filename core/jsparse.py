import re
import random
import requests
from core import regex
from core import nano





def jsparse_(url):
    if nano.rev(url).split('.')[0] == nano.rev('js') :
        try:
            user_agent=random.choice(regex.USR_AGENTS)
            headers = {'User-Agent': user_agent } 
            r = requests.get(url,headers=headers)
            resp = r.content
            if len(resp)>0:
                for a,b in regex.REGEX_JS.items():
                    mutch=re.findall(b, str(resp))
                    if(mutch):                 
                        
                        print("\033[94m[+] js file {} Contain: \033[00m".format(url))
                        for i in mutch:
                            print("\033[33m[{}]-----|\033[00m  {}".format(a.rstrip(),i))
        except:
            pass           
