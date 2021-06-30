import requests
import re
import random
import nano
import regex

from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

mt='InKgg67\[2s4h7jT67HF5)o[>,j'
def response_time(url):
    user_agent=random.choice(regex.USR_AGENTS)
    headers = {'User-Agent': user_agent } 
    try:
        r = requests.get(url,headers=headers,verify=False)   
        r_time = int(r.elapsed.total_seconds())
        return r_time
    except:
        pass
    



def bolian_base(url):
    state=False
  
    try:
        r1=requests.get(nano.inject(url,'test'),verify=False,timeout=13).text
        r2=requests.get(nano.inject(url,'test'),verify=False,timeout=13).text
        if len(r1)==len(r2) :
            for god,bad in regex.SQL_INJECTION_ERROR_BASE.items():
                for link in nano.injecter(url,mt):
                    r1=requests.get(link.replace(mt,god),verify=False,timeout=13)
                    god_r=r1.content
                    sr1=r1.status_code
                    r2=requests.get(link.replace(mt,bad),verify=False,timeout=13)
                    bad_r=r2.content
                    sr2=r2.status_code
                    if len(god_r) != len(bad_r) and sr1 == sr2:
                        state=True
                        print("\033[91mPossibly SQL injection vulnerability\033[00m  ")
                        print(nano.inject(url,god)+' | response Length:'+str(len(god_r))+'\n'+nano.inject(url,bad)+' | response Length:'+str(len(bad_r)))
                        break
                    
    except:
        pass
    return state


def time_base(url): 
        
    try:
        for x in regex.SQL_INJECTION_BLIND_BASE:
            for link in nano.injecterWithOrginKey(url,mt):
                
                r1=link.replace(mt,str(x).format('3'))
               
                rs1=response_time(r1)
                
                r2=link.replace(mt,str(x).format('6'))
               
                rs2=response_time(r2)
               
                r3=link.replace(mt,str(x).format('9'))
                
                rs3=response_time(r3)
                
              
                if int(rs1) < int(rs2) and int(rs1) < int(rs3):
                    if int(rs2) > int(rs1) and int(rs2) < int(rs3):
                           if int(rs3) > int(rs1) and int(rs3) > int(rs2):
                                rr=link.replace(mt,str(x).format('0'))
                                rs=response_time(rr)
                                if int(rs) < int(rs1)  and int(rs) <  int(rs2) and int(rs) < int(rs3):
                                    t=bolian_base(url)
                                    if t==True:
                                        print(r1+' | Response time:'+'\033[32m'+str(rs1)+'\033[00m'+'\n'+r2+' | Response time:'+'\033[32m'+str(rs2)+'\033[00m'+'\n'+r3+' | Response time:'+'\033[32m'+str(rs3)+'\033[00m')
                                        break
                           
                                    else:
                                        print('\033[33;1mWarning can be false positives\033[00m') 
                                        print("\033[91mPossibly SQL injection vulnerability\033[00m  ")
                                        print(r1+' | Response time:'+'\033[32m'+str(rs1)+'\033[00m'+'\n'+r2+' | Response time:'+'\033[32m'+str(rs2)+'\033[00m'+'\n'+r3+' | Response time:'+'\033[32m'+str(rs3)+'\033[00m')
                                    break
    except:
        pass
    
def semple(url):
    state=False
    done=0
    user_agent=random.choice(regex.USR_AGENTS)
    headers = {'User-Agent': user_agent } 
    payloads=["x'","x%27",'x"',"x%22","x;","x#","x-","x--","x--+"]
    
    for i in payloads: 
        if done ==1 :
            break
        try:
            for link in nano.injecter(url,i):
                r = requests.get(link,headers=headers,verify=False,timeout=13)
                cont = r.content
                for x in regex.SQL_ERROR:
                    if(re.search(x, str(cont))):
                        r_ = requests.get(url,headers=headers,verify=False,timeout=13)
                        cont_ = r_.content
                        if not (re.search(x, str(cont_))):
                            state=True
                            print("\033[91mPossibly SQL injection vulnerability\033[00m  "+link)
                            done=1
                            break
                        
                        else:
                            pass
                        
        except:
            pass
               
    return state
                
                
def sqlinjection_(url):
    task1=semple(url)
    if task1 == False:
        time_base(url)

