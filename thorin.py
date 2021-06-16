from core import archiveurl
from core import xss
from core import redirect
from core import sqlinjection
from core import temletinjetion
from core import lfi
from core import crlf
from core import nano
from core import trace
from core import oscommand
from core import cors
from core import ssrf
from core import base_64
from core import credentialsFond
from core import HostHeaderAttacks 
from core import dirvulscan
from core import regex
from core import debug

import threading
from alive_progress import alive_bar
import sys
from time import sleep
import signal
import os



urlslist=[]
try:
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
     
    
    elif sys.argv[1] =='-r':
        url=sys.argv[2]
        urlslist.append(url)
        urls=urlslist 
    elif sys.argv[1] =='-h':
        print('''usage: python3 thorin.py -f endpoint.txt
       python3 thorin.py -d www.site.com 
       python3 thorin.py -r http://sub.domain.com/index.php?p=fuzz
            
        ''')
        sys.exit()
        
    
    else:
        print('''usage: python3 thorin.py -f endpoint.txt
           python3 thorin.py -d www.site.com 
           python3 thorin.py -r http://sub.domain.com/index.php?p=fuzz
            
        ''')
        sys.exit()
        
except:
    print('''usage: python3 thorin.py -f endpoint.txt
       python3 thorin.py -d www.site.com 
       python3 thorin.py -r http://sub.domain.com/index.php?p=fuzz
            
        ''')
    sys.exit()
    

   

paramlink=[] 
uniqlink=[]

def HostHeaderAttacksF(i):
    HostHeaderAttacks.hostheader_(i)

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

def oscommandF(i):
    oscommand.oscommand_(i)

def corsF(i):
    cors.cors_(i)

def ssrfF(i):
    ssrf.ssrf_(i)
    
def base64F(i):
    base_64.Base64_(i)

def dirvulscanF(i):
    dirvulscan.run(i)

def credentialsFondF(i):
    credentialsFond.CredentialsFond_(i)

def debugF(i):
    debug.debug_(i)
   


    
rootdomain=[]
static=[]
with alive_bar(len(urls)) as bar:
    for i in urls:
        i=i.rstrip()
        
        try:
           i=i.replace(':80', '')
        except:
           pass
        bar()
        
        
        protocol=i.split(":")[0]
        baselink=i.split("/")[2]
        rootdom=protocol+'://'+baselink
        
        if rootdom not in rootdomain:
            rootdomain.append(rootdom)
            if nano.isAlive(rootdom) == True:
                pxx = threading.Thread(target=HostHeaderAttacksF, args=(rootdom,))
                pxx.start()
                pz = threading.Thread(target=corsF, args=(rootdom,))
                pz.start() 
                py=threading.Thread(target=debugF, args=(rootdom,))
                py.start()   
                pxx.join(timeout=5)
                pz.join(timeout=5)
                py.join(timeout=5)
            else:
                pass

       

        


        if '?' in i:
            chekUrl=i.split('?')[0]
            
        else:
            chekUrl=i

        
        for x in regex.STATIC_EXT:
            if chekUrl.endswith(x):
                static.append(chekUrl)
        
        if chekUrl not in static:
            if nano.isAlive(i) == True:
                p1 = threading.Thread(target=traceF, args=(i,))
                p1.start()
        
                p2 = threading.Thread(target=credentialsFondF, args=(i,))
                p2.start()      
        
                p4 = threading.Thread(target=base64F, args=(i,))
                p4.start()

                p2.join(timeout=5)
                p1.join(timeout=5)
                p4.join(timeout=5)
        


                if "?" in i:
                    path=i.split('?')[0]
                    for dlink in nano.inject_dir(path):
                        if dlink not in uniqlink :
                            uniqlink.append(dlink)
                            url=dlink
                       
                            px = threading.Thread(target=dirvulscanF, args=(url,))
                            px.start()                     
                            px.join(timeout=10)                 
                        
                        else:
                            pass
                   

                    plink=nano.inject_param(i,'yaTi8CP7Efh')
                    if plink not in paramlink:
                        paramlink.append(plink)
                        url=plink
                    
                        p6 = threading.Thread(target=xssF, args=(url,))
                        p6.start()                 
                 
                        p7 = threading.Thread(target=open_redirectionF, args=(url,))
                        p7.start() 
                 
                        p8 = threading.Thread(target=sqlscanF, args=(url,))
                        p8.start()
                 
                        p9= threading.Thread(target=sstiscanF, args=(url,))
                        p9.start()                 
                 
                        p10 = threading.Thread(target=lfiscanF, args=(url,))
                        p10.start()                 
                 
                        p11 = threading.Thread(target=crlfscanF, args=(url,))
                        p11.start()                 
                 
                        p12 = threading.Thread(target=oscommandF, args=(url,))
                        p12.start()                 
                 
                        p13 = threading.Thread(target=ssrfF, args=(url,))
                        p13.start()                 
                 
                        p13.join(timeout=5)
                        p12.join(timeout=5)
                        p11.join(timeout=5)
                        p10.join(timeout=10)
                        p9.join(timeout=5)
                        p6.join(timeout=5)                
                        p7.join(timeout=5)                 
                        p8.join(timeout=5)
                    else:
                        pass
                else:
                    for dlink in nano.inject_dir(i):
                        if dlink not in uniqlink :
                            uniqlink.append(dlink)
                            url=dlink
                            px = threading.Thread(target=dirvulscanF, args=(url,))
                            px.start() 
                            px.join(timeout=10)
                        
                        else:
                            pass
sleep(60)                
os.kill(os.getpid(), signal.SIGTERM)
