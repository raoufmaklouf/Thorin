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
                ContentType=r.headers.get('Content-Type')
                x = re.findall(rg, str(resp))
                if (x):
                    if 'text/html' in str(ContentType):
                        print('\033[91mPossibly XSS vulnerability\033[00m  '+url)
                        break
                    else:
                        print('\033[33;1mWarning can be false positives  Content Type: {}\033[00m').format(str(ContentType))
                        print('\033[91mPossibly XSS vulnerability\033[00m  '+url)
                        break
                else:
                    pay={'X=GtR"Nv>Yt':'&X=GtR%22Nv>Yt','X=Gt"RNbv>DR':'&X%3DGt%22RNbv%DR','XGt"RNbv>DR':'&XGt%22RNbv%DR'}
                    for rg,p in pay.items():
                        user_agent=random.choice(regex.USR_AGENTS)
                        headers = {'User-Agent': user_agent }
                        url=nano.inject(link,p)
                        try:
                            r = requests.get(url ,headers=headers ,verify=False )
                            resp = r.content 
                            ContentType=r.headers.get('Content-Type')   
                            x = re.findall(rg, str(resp))
                            if (x):
                                if 'text/html' in str(ContentType):
                                    print('\033[91mPossibly XSS vulnerability\033[00m  '+url)
                                    break
                                else:
                                    print('\033[33;1mWarning can be false positives  Content Type: {}\033[00m').format(str(ContentType))
                                    print('\033[91mPossibly XSS vulnerability\033[00m  '+url)
                                    break
                            else:
                                r = requests.post(url ,headers=headers ,verify=False )
                                resp = r.content 
                                ContentType=r.headers.get('Content-Type')   
                                x = re.findall(rg, str(resp))
                                if (x):
                                    if 'text/html' in str(ContentType):
                                        print('\033[91mPossibly XSS vulnerability\033[00m  '+url)
                                        break
                                    else:
                                        print('\033[33;1mWarning can be false positives  Content Type: {}\033[00m').format(str(ContentType))
                                        print('\033[91mPossibly XSS vulnerability\033[00m  '+url)
                                
                        except:
                            pass     
            except:
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
                ContentType=r.headers.get('Content-Type')
                x = re.findall(rg, str(resp))
                if (x):
                    if 'text/html' in str(ContentType):
                        print('\033[91mPossibly XSS vulnerability\033[00m  '+url)
                    else:
                        print('\033[33;1mWarning can be false positives  Content Type: {}\033[00m').format(str(ContentType))
                        print('\033[91mPossibly XSS vulnerability\033[00m  '+url)

                else:
                    pass
    except:
        pass
