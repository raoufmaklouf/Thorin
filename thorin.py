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
from core import dirvulscan
from multiprocessing import Process
from alive_progress import alive_bar
import sys




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

 

with alive_bar(len(urls)) as bar:
    for i in urls:
        bar()
        i=i.rstrip()
        p1 = Process(target=traceF, args=(i,))
        p1.start()
        
        p2 = Process(target=credentialsFondF, args=(i,))
        p2.start()      
        
        p4 = Process(target=base64F, args=(i,))
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
                    px = Process(target=dirvulscanF, args=(url,))
                    px.start()                    
                    px.join(timeout=10)
                else:
                    pass
                   

            plink=nano.inject_param(i,'yaTi8CP7Efh')
            if plink not in paramlink:
                 paramlink.append(plink)
                 url=plink
                 p6 = Process(target=xssF, args=(url,))
                 p6.start()                 
                 
                 p7 = Process(target=open_redirectionF, args=(url,))
                 p7.start() 
                 
                 p8 = Process(target=sqlscanF, args=(url,))
                 p8.start()
                 
                 p9= Process(target=sstiscanF, args=(url,))
                 p9.start()                 
                 
                 p10 = Process(target=lfiscanF, args=(url,))
                 p10.start()                 
                 
                 p11 = Process(target=crlfscanF, args=(url,))
                 p11.start()                 
                 
                 p12 = Process(target=oscommandF, args=(url,))
                 p12.start()                 
                 
                 p13 = Process(target=ssrfF, args=(url,))
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
                    px = Process(target=dirvulscanF, args=(url,))
                    px.start()                    
                    px.join(timeout=10)
                else:
                    pass
        
        
        
         
                    
        
