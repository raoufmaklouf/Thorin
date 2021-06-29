import re
import random
import requests
from core import regex
from core import counter
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)





def CredentialsFond_(url):
    
    user_agent=random.choice(regex.USR_AGENTS)
    headers = {'User-Agent': user_agent } 
    try:
        r = requests.get(url,headers=headers,verify=False,timeout=13)
        resp = r.content
        if len(resp)>0:
           for a,b in regex.CredentialsFond_REGEX.items():
               mutch=re.search(b, str(resp))
               if(mutch):               
                   mt=mutch.group()
                   if mt not in counter.credentialsFond:
                       counter.credentialsFond.append(mt)
                       print("\033[94m[+] Possibly Sensitive data disclosure on: {} \033[00m".format(url))
                       print("\033[33m[{}]-----|\033[00m  {}".format(a.rstrip(),mt))
                                
        else:
            pass
    except:
        pass
    
                            
                                
            


