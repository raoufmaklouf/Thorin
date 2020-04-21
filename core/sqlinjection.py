import requests
import re
import random
from core import nano
from core import regex

from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def response_time(url):
    r = requests.get(url)   
    r_time = int(r.elapsed.total_seconds())
    return r_time



def error_base(url):
    for god,bad in regex.SQL_INJECTION_ERROR_BASE.items():
        god_r=requests.get(url+god).text
        bad_r=requests.get(url+bad).text
        if len(god_r) != len(bad_r):
            if nano.reflection(nano.inject_param(url,'SRtbT5lOuEg')) != True:
                print("\033[91mPossibly SQL injection error base vulnerability\033[00m  ")
                print(url+god+'\n'+url+bad)
                break
            else:
                print('\033[33;1mWarning can be false positives\033[00m')
                print("\033[91mPossibly SQL injection error base vulnerability\033[00m  ")
                print(url+god+'\n'+url+bad)
                break


def blind_base(url):
    for x in regex.SQL_INJECTION_BLIND_BASE:
        r1=url+str(x).format('0')
        rs1=response_time(r1)
        r2=url+str(x).format('1')
        rs2=response_time(r2)
        r3=url+str(x).format('3')
        rs3=response_time(r3)
        if int(rs1) < int(rs2) and int(rs2) < int(rs3):
            print("\033[91mPossibly blind SQL injection  vulnerability\033[00m  ")
            print(r1+'\n'+r2+'\n'+r3)
            break

  

def semple(url):
    user_agent=random.choice(regex.USR_AGENTS)
    headers = {'User-Agent': user_agent } 

    try:
        r = requests.get(url,headers=headers,verify=False)
        cont = r.content
    except:
        pass
    try:
        for x in regex.SQL_ERROR:
            if(re.search(x, str(cont))):
                print("\033[91mPossibly SQL injection vulnerability\033[00m  "+url)
                
                
    except:
        pass

def sqlinjection_(url):
    
    semple(nano.inject_param(url,"'"))
    semple(nano.inject_param(url,'"'))
    error_base(url)
    blind_base(url)
        

