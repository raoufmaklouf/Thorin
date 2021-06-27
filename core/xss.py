import re 
import requests
import random
from core import regex
from core import nano

from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  
mt='InKgg67\[2s4h7jT67HF5)o[>,j'

def xss_(link):
    
    if nano.reflection(link) == True:
        for url in nano.injecter(link,mt):
            for rg,p in regex.XSS.items():
                user_agent=random.choice(regex.USR_AGENTS)
                headers = {'User-Agent': user_agent } 
                url1=url.replace(mt,p)
                try:
                    r = requests.get(url1 ,headers=headers ,verify=False,timeout=13 )       
                    resp = r.content
                    ContentType=r.headers.get('Content-Type')
                    x = re.findall(rg, str(resp))
                    if (x):
                        if 'text/html' in str(ContentType):
                            print('\033[91mPossibly XSS vulnerability\033[00m  '+url1)
                            break
                        else:
                            print('\033[33;1mWarning can be false positives \033[00m')
                            print('\033[91mPossibly XSS vulnerability\033[00m  '+url1)
                            break
                    else:
                        r = requests.post(url1 ,headers=headers ,verify=False,timeout=13 )
                        resp = r.content 
                        ContentType=r.headers.get('Content-Type')   
                        x2 = re.findall(rg, str(resp))
                        if (x2):
                            if 'text/html' in str(ContentType):
                                print('\033[91mPossibly POST XSS vulnerability  POST\033[00m  '+url1)
                                break
                            else:
                                print('\033[33;1mWarning can be false positives \033[00m')
                                print('\033[91mPossibly POST XSS vulnerability  POST\033[00m  '+url1)

                                
                        pay={'X=GtR"Nv>Yt':'&X=GtR%22Nv>Yt','X=Gt"RNbv>DR':'&X%3DGt%22RNbv%DR','XGt"RNbv>DR':'&XGt%22RNbv%DR'}
                        for rg,p in pay.items():
                            user_agent=random.choice(regex.USR_AGENTS)
                            headers = {'User-Agent': user_agent }
                            url2=url.replace(mt,p)
                            try:
                                r = requests.get(url2 ,headers=headers ,verify=False,timeout=13 )
                                resp = r.content 
                                ContentType=r.headers.get('Content-Type')   
                                x1 = re.findall(rg, str(resp))
                                if (x1):
                                    if 'text/html' in str(ContentType):
                                        print('\033[91mPossibly XSS vulnerability\033[00m  '+url2)
                                        break
                                    else:
                                        print('\033[33;1mWarning can be false positives \033[00m')
                                        print('\033[91mPossibly XSS vulnerability\033[00m  '+url2)
                                        break
                                else:
                                    r = requests.post(url2 ,headers=headers ,verify=False,timeout=13 )
                                    resp = r.content 
                                    ContentType=r.headers.get('Content-Type')   
                                    x2 = re.findall(rg, str(resp))
                                    if (x2):
                                        if 'text/html' in str(ContentType):
                                            print('\033[91mPossibly POST XSS vulnerability  POST\033[00m  '+url2)
                                            break
                                        else:
                                            print('\033[33;1mWarning can be false positives \033[00m')
                                            print('\033[91mPossibly POST XSS vulnerability  POST\033[00m  '+url2)
                                
                            except:
                                pass     
                except:
                    pass

