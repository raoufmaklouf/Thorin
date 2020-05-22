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
from core import base_64
from multiprocessing import Process
from alive_progress import alive_bar
import sys
import os
from time import sleep


url=sys.argv[1]
os.system('resize -s 25 120 > /dev/null')
connter=[] 
uniq=[]
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
    
def base64F(i):
    base_64.Base64_(i)

def redirection_dirF(i):
    redirect.redirect_dir(i)

def xss_dirF(i):
    xss.xss_dir(i)

def lfi_dirF(i):
    lfi.lfi_dir(i)

def crlf_dirF(i):
    crlf.crlf_dir(i)

 
urls= archiveurl.waybackurls(url)
with alive_bar(len(urls)) as bar:
    for i in urls:
        for uniq_url in nano.inject_dir(i,"uNiq_stRiNg"):
             if uniq_url not in uniq:
                 uniq.append(uniq_url)
        if "?" in i:
            uniq_link=nano.inject_param(i,'yaTi8CP7Efh')
   
        else:
            uniq_link=i
            
        
        bar()
        i=i.rstrip()
        p1 = Process(target=traceF, args=(i,))
        p1.start()
        p2 = Process(target=jsparseF, args=(i,))
        p2.start()
        p4 = Process(target=base64F, args=(i,))
        p4.start()
        if '?' not in i:
            sleep(0.2)
        else:
            pass
        
        
        
        
        if uniq_link not in connter:
            connter.append(uniq_link)
            if '?' in i:
                p6 = Process(target=xssF, args=(i,))
                p6.start()
                p7 = Process(target=open_redirectionF, args=(i,))
                p7.start()
                
                p8 = Process(target=sqlscanF, args=(i,))
                p8.start()
                p9= Process(target=sstiscanF, args=(i,))
                p9.start()
                p10 = Process(target=lfiscanF, args=(i,))
                p10.start()
                p11 = Process(target=crlfscanF, args=(i,))
                p11.start()
                p12 = Process(target=oscommandF, args=(i,))
                p12.start()
                sleep(0.5)

with alive_bar(len(uniq)) as bar:
    for i in uniq:
        sleep(1.2)
        i=i.rstrip()
        bar()
        p5 = Process(target=corsF, args=(i,))
        p5.start()
        p3 = Process(target=put_methodeF, args=(i,))
        p3.start()
        p14 = Process(target=redirection_dirF, args=(i,))
        p14.start()
        p15 = Process(target=xss_dirF, args=(i,))
        p15.start()
        p16 = Process(target=lfi_dirF, args=(i,))
        p16.start()
        p17 = Process(target=crlf_dirF, args=(i,))
        p17.start()
