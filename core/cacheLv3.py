# cache poisining scanner v 1.1.7 creat by raouf maklouf 
import re 
import requests
import random
import string
import os
import http.client
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



USR_AGENTS=[
'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaE51-1/220.34.37; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413', 
'Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95/11.0.026; Profile MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413', 
'Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 Nokia5630d-1/012.020; Profile MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413', 
'Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 NokiaN78-1/12.046; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413', 
'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-3/21.2.045; Profile/MIDP-2.1 Configuration/CLDC-1.1;) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.4', 
'Mozilla/5.0 (SymbianOS/9.4; U; Series60/5.0 Nokia5530c-2/10.0.050; Profile MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Safari/525', 
'Mozilla/5.0 (SymbianOS/9.4; U; Series60/5.0 Nokia5800d-1/31.0.101; Profile MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413', 
'Mozilla/5.0 (webOS/1.4.0; U; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Version/1.0 Safari/532.2 Pre/1.0', 
'Mozilla/5.0 (webOS/Palm webOS 1.2.9; U; en-US) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/1.0 Safari/525.27.1 Pixi/1.0', 
'Mozilla/5.0 (Windows; U; Win98; en-US; rv:0.9.2) Gecko/20010726 Netscape6/6.1', 
'Mozilla/5.0 (Windows; U; Win98; en-US; rv:x.xx) Gecko/20030423 Firebird Browser/0.6', 
'Mozilla/5.0 (Windows; U; Win9x; en; Stable) Gecko/20020911 Beonex/0.8.1-stable', 
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.153.1 Safari/525.19', 
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.5) Gecko/20060731 Firefox/1.5.0.5 Flock/0.7.4.1', 
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.1) Gecko/2008092215 Firefox/3.0.1 Orca/1.1 beta 3', 
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:x.x.x) Gecko/20041107 Firefox/x.x', 
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:x.xx) Gecko/20030504 Mozilla Firebird/0.6', 
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:x.xxx) Gecko/20041027 Mnenhy/0.6.0.104', 
'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9b5) Gecko/2008032620 Firefox/3.0b5', 
'Mozilla/5.0 (Windows; U;XMPP Tiscali Communicator v.10.0.1; Windows NT 5.1; it; rv:1.8.1.3) Gecko/20070309 Firefox/2.0.0.3', 
'Mozilla/5.0 (X11; Linux i686; U;rv: 1.7.13) Gecko/20070322 Kazehakase/0.4.4.1', 
'Mozilla/5.0 (X11; U; Linux 2.4.2-2 i586; en-US; m18) Gecko/20010131 Netscape6/6.01', 
'Mozilla/5.0 (X11; U; Linux armv7l; en-GB; rv:1.9.2b6pre) Gecko/20100318 Firefox/3.5 Maemo Browser 1.7.4.8 RX-51 N900', 
'Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.8.0.2) Gecko/20060309 SeaMonkey/1.0', 
'Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.7.6) Gecko/20050405 Epiphany/1.6.1 (Ubuntu) (Ubuntu package 1.0.2)', 
'Mozilla/5.0 (X11; U; Linux i686; en-US; Nautilus/1.0Final) Gecko/20020408', 
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801', 
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.2b) Gecko/20021007 Phoenix/0.3', 
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040413 Epiphany/1.2.1', 
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 SnapPreviewBot', 
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061129 BonEcho/2.0', 
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)', 
'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9a8) Gecko/2007100619 GranParadiso/3.0a8', 
]





resolt=[]


    
def random_char(n):
       return ''.join(random.choice(string.ascii_letters) for x in range(n))
       
def random_number():
       return ''.join(random.choice('123456789') for x in range(random.randint(1, 4)))
                 
def make_url(url):

    if '?' in url :
        params=url.split('?')[1]
        if '&' in params:
            pr='?'
            params.split('&')
            for x in params:
                pr+=x+random_char(2)+'&'
            link=url.replace(params,pr)+random_char(7)+'=1234'
        else:
            link=url+random_char(2)+'&'+random_char(7)+'=1234'   
    else:
        link=url+'?'+random_char(7)+'=1234'
    return link


def scan1(link):
    randoSTR=random_char(5)
    
    port=':'+random_number()
    if '?' in link:
       BU=link.split('?')[0]
    else:
       BU=link
    user_agent=random.choice(USR_AGENTS)   
    base_domain=BU.split('/')[2]
    headers={'host':base_domain+port,'User-Agent':user_agent}
    r1=requests.get(link,headers=headers,verify=False,timeout=5)
    resp1 = r1.content  
    
    x1 = re.findall(base_domain+port, str(resp1))
    if (x1):
        r2=requests.get(link,verify=False,headers={'User-Agent':user_agent},timeout=5)
        resp2 = r2.content
        xx=re.findall(base_domain+port, str(resp2))
        if (xx):
        
                 
                  print('-----------------------------------------------------------------------------')
                  print('\033[91mPossibly cache poisoning vulnerability\033[00m  '+link+'\npoisoning request: host: '+base_domain+port+' \033[32mpoisoning response\033[00m\nnormal request: host: '+base_domain+' \033[32mpoisoning response\033[00m')
                  print('-----------------------------------------------------------------------------')
                  
                  return 1
                  
    
    r3=requests.get(link,headers={'host':randoSTR+'.'+base_domain,'User-Agent':user_agent},verify=False,timeout=5)
    resp3 = r3.content  
    
    x3 = re.findall(base_domain+port, str(resp3))
    if (x3):
        r4=requests.get(link,verify=False,headers={'User-Agent':user_agent},timeout=5)
        resp4 = r4.content
        xxx=re.findall(randoSTR+'.'+base_domain, str(resp4))
        if (xxx):
            
            print('-----------------------------------------------------------------------------')
            print('\033[91mPossibly cache poisoning vulnerability\033[00m  '+link+'\npoisoning request: host: '+randoSTR+'.'+base_domain+' \033[32mpoisoning response\033[00m\nnormal request: host: '+base_domain+' \033[32mpoisoning response\033[00m')
            print('-----------------------------------------------------------------------------')
            return 1


def scan2(link):
    
    user_agent=random.choice(USR_AGENTS)
    
    if '?' in link:
       BU=link.split('?')[0]
    else:
       BU=link
    base_domain=BU.split('/')[2]




 
    Headers=[
        'X-Forwarded-Host',
        'HTTP_FORWARDED',
        'HTTP_CLIENT_IP',
        'HTTP_FORWARDED_FOR',
        'HTTP_X_FORWARDED',
        'HTTP_X_FORWARDED_FOR',
        'X-Originating-IP',
        'X-Forwarded-For',
        'X-Remote-IP',
        'X-Remote-Addr',
        'X-Client-IP',
        'WL-Proxy-Client-IP',
        'Z-Forwarded-For',
        'Source-IP',
        'True-Client-IP',
        'X-Real-IP',
        'X-Host',
        'X-Forwarded-Server',
        'X-HTTP-Host-Override',
        'Forwarded',
        'x-forwarded-port',
        ]
       
    for z in Headers:
        url=make_url(link)
        headers={z:'your_hackerz_site.com','User-Agent':user_agent}
        
        for x in range(5):
              r1=requests.get(url,headers=headers,verify=False,timeout=5)
    
    
        r2=requests.get(url,headers={'User-Agent':user_agent},verify=False,timeout=5)
        resp2 = r2.content
        xx=re.findall('your_hackerz_site.com', str(resp2))
        if (xx):
              print(resp2.decode('utf-8'))
            
              print('-----------------------------------------------------------------------------')
              print('\033[91mPossibly cache poisoning vulnerability\033[00m  '+url+'\npoisoning request: '+z+' : your_hackerz_site.com  \033[32mpoisoning response\033[00m\nnormal request:   \033[32mpoisoning response\033[00m')
              print('-----------------------------------------------------------------------------')

   
    prt=random_number()
    headers2={'x-forwarded-port': prt,'User-Agent':user_agent}
    for z in range(1,5):
        
        r1=requests.get(link,headers=headers2,verify=False,timeout=3)

    r3=requests.get(link,verify=False,headers={'User-Agent':user_agent},timeout=3)
    resp3 = r3.content
    xx=re.findall(base_domain+':'+prt, str(resp3))
    if (xx):
             
             print('-----------------------------------------------------------------------------')
             print('\033[91mPossibly cache poisoning vulnerability\033[00m  '+link+'\npoisoning request: x-forwarded-port: '+str(prt)+'  \033[32mpoisoning response\033[00m\nnormal request: x-forwarddd-port: '+str(prt)+'  \033[32mpoisoning response\033[00m')
             print('-----------------------------------------------------------------------------')



def scan3(link):
    user_agent=random.choice(USR_AGENTS)
    if '?' in link:
       BU=link.split('?')[0]
    else:
       BU=link
    base_domain=BU.split('/')[2]
    
    for z in range(1,5):
        r1=requests.get(link,headers={'Host': base_domain,'Host':'your_hackerz_site.bom','User-Agent':user_agent},verify=False,timeout=5)

    r2=requests.get(link,verify=False,headers={'User-Agent':user_agent},timeout=5)
    resp2 = r2.content
    xx=re.findall('your_hackerz_site.com', str(resp2))
    if (xx):
              print('-----------------------------------------------------------------------------')
              print('\033[91mPossibly cache poisoning vulnerability\033[00m  '+link+'\npoisoning request: Host: '+str(base_domain)+' Host: your_hackerz_site.bom  \033[32mpoisoning response\033[00m\nnormal request: Host: '+str(base_domain)+'  \033[32mpoisoning response\033[00m')
              print('-----------------------------------------------------------------------------')

def scan4(link):
    user_agent=random.choice(USR_AGENTS)
    prot=link.split('/')[0]
    url= link.split('/')[2]
    path=link.replace(prot,'')
    path=path.replace(url,'')
    if prot=='http:':
        conn = http.client.HTTPConnection(url)
    elif prot=='https:':
        conn = http.client.HTTPSConnection(url)
    for x in range(1,5):
        conn.request("GET", link,headers={'Host':'your_hackerz_site.com','User-Agent':user_agent})

    r3=requests.get(link,verify=False,headers={'User-Agent':user_agent},timeout=5)
    resp3 = r3.content
    xxx=re.findall('your_hackerz_site.com', str(resp3))
    if (xxx):
        print('-----------------------------------------------------------------------------')
        print('\033[91mPossibly cache poisoning vulnerability\033[00m  '+link+'\npoisoning request: GET '+str(link)+' Host: your_hackerz_site.bom  \033[32mpoisoning response normal request: poisoning response')
        print('-----------------------------------------------------------------------------')


def scan5():

    #with socket 
    # GET /?duplicate-host-headers-line-wrap HTTP/1.1
    # {}Host: xrcr0x4a.com
    # Host: {{Hostname}}
    # User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
    # Accept: */*
    # Connection: close
    pass
def run(url):
            try:
                for x in range(1,5):
                        if scan1(make_url(url)) == 1:
                          break
                        scan2(make_url(url))
                        scan3(make_url(url))
                        #scan4(make_url(url))
                
            except:
                pass


    



    






