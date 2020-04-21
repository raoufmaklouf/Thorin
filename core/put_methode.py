import requests
import random
from core import regex
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def putmethode_(url):
    url=url.replace("uNiq_stRiNg",'')
    user_agent=random.choice(regex.USR_AGENTS)
    data="<TFwKlsH7pVbfJ>"
    filename='poc.html'
    headers = {'User-Agent': user_agent } 
    url=url+filename


    try:
        r=requests.put(url, data, headers=headers, verify=False)
        scode=r.status_code
        if "2" in str(scode):
            re=requests.get(url,headers=headers,verify=False)
            res=re.content
            
            if "<TFwKlsH7pVbfJ>" in str(res):
                print('\033[91m Possibly PUT methode Allow vulnerability\033[00m  '+url)
            else:
                pass
        else :
            pass
    except:
        pass



