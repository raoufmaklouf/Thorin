import requests
import re
from core import nano
from core import regex

from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


test1="58784"
test2='32110'

def ssti_(url):
   
    try:
        for x in regex.payload_ssti_1:
            r = requests.get(nano.inject_param(url,x),verify=False)
            cont1 = r.content
            if(re.search(test1, str(cont1))):
                for i in regex.payload_ssti_2:
                    r = requests.get(nano.inject_param(url,i),verify=False,timeout=10)
                    cont2 = r.content
                    if(re.search(test2, str(cont2))):
                         print("\033[91m Possibly SS template injection vulnerability\033[00m\t"+v)
                         break
                    else:
                         pass
    except:
        pass
        

        




