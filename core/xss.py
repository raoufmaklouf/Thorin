import re 
import requests
import random
from core import regex
from core import nano

    
def xss_(link):
    
    if nano.reflection(link) == True:
        for rg,p in regex.XSS.items():
            user_agent=random.choice(regex.USR_AGENTS)
            headers = {'User-Agent': user_agent } 
            url=nano.inject_param(link,p)
            try:
                r = requests.get(url ,headers=headers ,verify=False )       
                resp = r.content
                x = re.findall(rg, str(resp))
                if (x):
                    print('\033[91m Possibly XSS vulnerability\033[00m  '+url)
                    break
                else: 
                    pass
            except:
                pass
        pay={'X=GtRNv>':'&X=GtRNv>','X=GtRNbv>':'&X%3DGtRNbv%3E'}
        for rg,p in pay.items():
            user_agent=random.choice(regex.USR_AGENTS)
            headers = {'User-Agent': user_agent }
            url=link+p
            try:
                r = requests.post(url ,headers=headers ,verify=False )       
                resp = r.content
                x = re.findall(rg, str(resp))
                if (x):
                    print('\033[91m Possibly XSS vulnerability\033[00m  '+url)
                else:
                    pass
            except:
                pass
        
    else:
        pass

def xss_dir(link):
    payload="TrSAF45"
    try:
        url=link.replace('uNiq_stRiNg',payload)
        r = requests.get(url ,verify=False )
        resp = r.content
        ref = re.findall("TrSAF45", str(resp))
        if (ref):
            for rg,p in regex.XSS.items():
                user_agent=random.choice(regex.USR_AGENTS)
                headers = {'User-Agent': user_agent } 
                url=link.replace('uNiq_stRiNg',p)
                r = requests.get(url,headers=headers ,verify=False )       
                resp = r.content
                x = re.findall(rg, str(resp))
                if (x):
                    print('\033[91m Possibly XSS vulnerability\033[00m  '+url)
                else:
                    pass
    except:
        pass




        

