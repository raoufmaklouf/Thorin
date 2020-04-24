import requests
import re
import random
from core import nano
from core import regex

from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def inject(link,pay):
    b_link=link.split('?')[0]
    params=link.split('?')[1]
    if len(params) >0:
        param_list=[]
        Plenth=params.split('&')
        for z in Plenth:
            param=z.split('=')[0]
            val=z.split('=')[1]
            if param not in param_list:
                param_list.append(param)
            payload=(b_link+'?')
            for y in param_list:
                payload=(payload+y+'='+val+pay+'&')
            payload=payload[:-1]
        return payload



def response_time(url):
    user_agent=random.choice(regex.USR_AGENTS)
    headers = {'User-Agent': user_agent } 
    r = requests.get(url,headers=headers)   
    r_time = int(r.elapsed.total_seconds())
    return r_time



def error_base(url):
    state=False
    for god,bad in regex.SQL_INJECTION_ERROR_BASE.items():
        god_r=requests.get(inject(url,god)).text
       
        bad_r=requests.get(inject(url,bad)).text
        if len(god_r) != len(bad_r):
            state=True
            if nano.reflection(nano.inject_param(url,'SRtbT5lOuEg')) != True:
                print("\033[91mPossibly SQL injection vulnerability\033[00m  ")
                print(inject(url,god)+' | Response lenth:'+str(len(god_r))+'\n'+inject(url,bad)+' | Response lenth:'+str(len(bad_r)))
                break
            else:
                print('\033[33;1mWarning can be false positives\033[00m')
                print("\033[91mPossibly SQL injection vulnerability\033[00m  ")
                print(inject(url,god)+' | Response lenth:'+str(len(god_r))+'\n'+inject(url,bad)+' | Response lenth:'+str(len(bad_r)))
                break
    return state


def blind_base(url):
    state=False
    for x in regex.SQL_INJECTION_BLIND_BASE:
        
        r1=inject(url,str(x).format('0'))
        rs1=response_time(r1)
        r2=inject(url,str(x).format('1'))
        rs2=response_time(r2)
        r3=inject(url,str(x).format('3'))
        rs3=response_time(r3)
        if int(rs1) < int(rs2) and int(rs2) < int(rs3):
            state=True
            print("\033[91mPossibly SQL injection  vulnerability\033[00m  ")
            print(r1+' | Response time:'+str(rs1)+'\n'+r2+' | Response time:'+str(rs2)+'\n'+r3+' | Response time:'+str(rs3))
            break
    return state
  

def semple(url):
    state=False
    user_agent=random.choice(regex.USR_AGENTS)
    headers = {'User-Agent': user_agent } 

    try:
        r = requests.get(url,headers=headers,verify=False)
        cont = r.content
    except:
        pass
    
    for x in regex.SQL_ERROR:
        if(re.search(x, str(cont))):
            state=True
            print("\033[91mPossibly SQL injection vulnerability\033[00m  "+url)
            break
    return state
                
                

def sqlinjection_(url):
    task1=semple(nano.inject_param(url,"x'"))
    if task1 == False:
        task2=semple(nano.inject_param(url,'x"'))
        if task2 == False:
            task3=error_base(url)
            if task3 == False:
                blind_base(url)
