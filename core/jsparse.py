import re
import requests
from core import regex
from core import nano





def jsparse_(url):
    if nano.rev(url).split('.')[0] == nano.rev('js'):
        try:
            r = requests.get(url)
            resp = r.content
            if len(resp)>0:
                for a,b in regex.REGEX_JS.items():
                    mutch=re.search(b, str(resp))
                    if(mutch):                 
                        mutch=mutch.group()
                        print("\033[94m[+] js file {} Contain: \033[00m".format(url))
                        print("\033[33m[{}]-----|\033[00m  {}".format(a.rstrip(),mutch.rstrip()))
        except:
            pass           
