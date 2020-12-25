from core import archiveurl
from core import xss
from core import redirect
from core import sqlinjection
from core import temletinjetion
from core import lfi
from core import crlf
from core import nano
from core import trace
from core import jsparse
from core import oscommand
from core import put_methode
from core import cors
from core import ssrf
from core import base_64
from core import dirvulscan
from multiprocessing import Process
from alive_progress import alive_bar
import sys
import os
from time import sleep


urlslist=[]
if sys.argv[1] =='-f':
    file_=sys.argv[2]
    f=open(file_,'r')
    for x in f :
        x=x.rstrip()
        urlslist.append(x)
    urls=urlslist
elif sys.argv[1] =='-d':
    url=sys.argv[2]
    urls= archiveurl.waybackurls(url)
     
    
else:
    print('''usage: python3 thorin.py -f endpoint.txt
       python3 thorin.py -d www.site.com      
    ''')
    sys.exit()

   

paramlink=[] 
uniqlink=[]
def xssF(i):
    xss.xss_(i)

def open_redirectionF(i):
    redirect.redirect_(i)
    
def sqlscanF(i):
    sqlinjection.sqlinjection_(i)

def lfiscanF(i):
    lfi.lfi_(i)

def sstiscanF(i):
    temletinjetion.ssti_(i)
    
def crlfscanF(i):
    crlf.crlf_(i)

def traceF(i):
    trace.trace_(i)

def jsparseF(i):
    jsparse.jsparse_(i)

def oscommandF(i):
    oscommand.oscommand_(i)

def put_methodeF(i):
    put_methode.putmethode_(i)

def corsF(i):
    cors.cors_(i)

def ssrfF(i):
    ssrf.ssrf_(i)
    
def base64F(i):
    base_64.Base64_(i)

def dirvulscanF(i):
    dirvulscan.run(i)


 

with alive_bar(len(urls)) as bar:
    for i in urls:
        bar()
        i=i.rstrip()
        p1 = Process(target=traceF, args=(i,))
        p1.start()
        p2 = Process(target=jsparseF, args=(i,))
        p2.start()
        p4 = Process(target=base64F, args=(i,))
        p4.start()

        if "?" in i:
            path=i.split('?')[0]
            for dlink in nano.inject_dir(path):
                if dlink not in uniqlink :
                    uniqlink.append(dlink)
                    url=dlink
                    px = Process(target=dirvulscanF, args=(url,))
                    px.start()
                    sleep(2)
                else:
                    pass
                   


            plink=nano.inject_param(i,'yaTi8CP7Efh')
            if plink not in paramlink:
                 paramlink.append(plink)
                 url=plink
                 p6 = Process(target=xssF, args=(url,))
                 p6.start()
                 sleep(0.5)
                 p7 = Process(target=open_redirectionF, args=(url,))
                 p7.start()
                 sleep(0.5)
                 p8 = Process(target=sqlscanF, args=(url,))
                 p8.start()
                 sleep(0.5)
                 p9= Process(target=sstiscanF, args=(url,))
                 p9.start()
                 sleep(0.5)
                 p10 = Process(target=lfiscanF, args=(url,))
                 p10.start()
                 sleep(1)
                 p11 = Process(target=crlfscanF, args=(url,))
                 p11.start()
                 sleep(0.5)
                 p12 = Process(target=oscommandF, args=(url,))
                 p12.start()
                 sleep(0.5)
                 p13 = Process(target=ssrfF, args=(url,))
                 p13.start()
                 sleep(0.5)
            else:
                pass
        else:
            for dlink in nano.inject_dir(i):
                if dlink not in uniqlink :
                    uniqlink.append(dlink)
                    url=dlink
                    px = Process(target=dirvulscanF, args=(url,))
                    px.start()
                    sleep(2)
                else:
                    pass
        
            
                    
        
