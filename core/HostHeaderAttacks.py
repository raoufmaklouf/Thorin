import re 
import http.client
import requests
import threading
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




def task2(url):
    base_domain=url.split('/')[2]
    if 'http://' in base_domain:
        base_domain=base_domain.replace('http://','')
    elif 'https://' in base_domain:
        base_domain=base_domain.replace('https://','')

    try:
        headersN={'Host': base_domain }
        normalR=requests.get(url ,headers=headersN ,verify=False )
        normalStatusCode=normalR.status_code
        normalCont=normalR.content
    except:
        pass

    headers1 = {'Host': 'omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net' } 
    try:    
        r1 = requests.get(url ,headers=headers1 ,verify=False )
        rs1=r1.status_code
        cont1 = r1.content
        if 'omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net' in str(cont1):
            print('\033[33minteresting host header handling !  \033[00m\n'+url+'\nhost header value "omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net"  reflection in response\nHost: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\n')
        elif 'k6unx4pudf8k5itoapaxjwzjigz' in str(cont1):
            if r1.history:
                print('\033[94mPossibly open redirection vulnerability with host header injection\033[00m  \n'+url+'\nHost: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\n')
            else:
                print('\033[91mPossibly SSRF vulnerability with host header injection\033[00m\n'+url+'\nHost: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\n')
               
        else:
            pass
    except:
        pass

    headers2 = {'Host': base_domain,'Host': 'omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net' }
    try:
        r2 = requests.get(url ,headers=headers2 ,verify=False )
        rs2=r2.status_code
        cont2 = r2.content
        if 'omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net' in str(cont2):
            print('\033[33minteresting host header handling !  \033[00m\n'+url+'\nHost: '+str(base_domain)+'\nHost: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\nhost header value "omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net"  reflection in response \n')
        elif 'k6unx4pudf8k5itoapaxjwzjigz' in str(cont2):
            if r2.history:
                print('\033[94mPossibly open redirection vulnerability with host header injection\033[00m  \n'+url+'\nHost: '+base_domain+' \nHost: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net \n')
            else:
                print('\033[91mPossibly SSRF vulnerability with host header injection\033[00m\n'+url+'\nHost: '+base_domain+'\nHost: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net \n')

        else:
            pass
    except:
        pass

    headers3 = {'Host': base_domain+':omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net' }
    try:
        r3 = requests.get(url ,headers=headers3 ,verify=False )
        rs3=r3.status_code
        cont3 = r3.content
        if 'omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net' in str(cont3):
            print('\033[33minteresting host header handling !  \033[00m\n'+url+'\nHost: '+str(base_domain)+':omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\n host header value "omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net" reflection in response\n')
        elif 'k6unx4pudf8k5itoapaxjwzjigz' in str(cont3):
            if r3.history:
                print('\033[94mPossibly open redirection vulnerability with host header injection\033[00m  \n'+url+'\nHost: '+str(base_domain)+':omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net \n')
            else:
                print('\033[91mPossibly SSRF vulnerability with host header injection\033[00m\n'+url+'\nHost: '+str(base_domain)+':omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net \n')
        else:
            pass
    except:
        pass



def task3(url):
    base_domain=url.split('/')[2]
    if 'http://' in base_domain:
        base_domain=base_domain.replace('http://','')
    elif 'https://' in base_domain:
        base_domain=base_domain.replace('https://','')

    prot=url.split('/')[0]
    try:
        headersN={'Host': base_domain }
        normalR=requests.get(url ,headers=headersN ,verify=False )
        normalStatusCode=normalR.status_code
        normalCont=normalR.content
    except:
        pass

    if prot=='http:':
        link=url.replace('http://','')
        conn = http.client.HTTPConnection(link)
    elif prot=='https:':
        link=url.replace('https://','')
        conn = http.client.HTTPSConnection(link)
    base_domain=str(base_domain)
    prot=str(prot)    
    link=prot+'//'+link
    
    conn1=conn
    conn2=conn
    try:
        conn1.request("GET",link,headers={'Host':'omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net'})
        res1 = conn1.getresponse()      
        data1 = res1.read().decode('utf-8')
        x1 = re.search('k6unx4pudf8k5itoapaxjwzjigz',data1)
        if 'omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net' in data1 :
            print('\033[33minteresting host header handling !  \033[00m\nhost header value "omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net"  reflection in response\n '+url+'\nrequest {\nGET '+str(base_domain)+' HTTP/1.1\nHost: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\n}\n')
            
        if (x1):
            print('\033[91mPossibly SSRF vulnerability with host header injection\033[00m\n'+url+'request {\nGET '+str(url)+' HTTP/1.1\nHost: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\n}\n')
            
        else:
            pass
         
    
        conn2.request("GET", 'http://omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net')
        res2 = conn2.getresponse()      
        data2 = res2.read().decode('utf-8')
    
        x2 = re.search('k6unx4pudf8k5itoapaxjwzjigz',data2)
        if 'omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net' in data2 :
            print('\033[33minteresting host header handling !  \033[00m\nvalue "omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net" reflection in response\n'+url+'\nrequest {\nGET '+str(prot)+'//omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net HTTP/1.1\nHost: '+str(base_domain)+'\n}\n')
        if (x2):
            print(url+'\n\033[91mPossibly SSRF vulnerability with host header injection\033[00m\n'+'request {\nGET http://omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net HTTP/1.1\nHost: '+str(base_domain)+'\n}\n')
            
        else:
            pass
    except:
        pass
    

def task4(url):
    base_domain=url.split('/')[2]
    if 'http://' in base_domain:
        base_domain=base_domain.replace('http://','')
    elif 'https://' in base_domain:
        base_domain=base_domain.replace('https://','')

    try:
        headersN={'Host': base_domain }
        normalR=requests.get(url ,headers=headersN ,verify=False )
        normalStatusCode=normalR.status_code
        normalCont=normalR.content
    except:
        pass

    headers1 = {'Host':base_domain,'X-Forwarded-Host':'omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net','X-Host':'omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net',
    'X-Forwarded-Server':'omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net','X-HTTP-Host-Override':'omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net',
    'Forwarded':'omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net'}
    try:
        r1 = requests.get(url ,headers=headers1 ,verify=False )
        rs1=r1.status_code
        cont1 = r1.content
        if 'omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net' in str(cont1):
            print('\033[33minteresting  header handling !  \033[00m\n'+url+'\nheader value "omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net"  reflection in response\n'+'Host '+str(base_domain)+'\nX-Forwarded-Host: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\nX-Host: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\nX-Forwarded-Server: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\nX-HTTP-Host-Override: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\nForwarded: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\n')
           
        elif 'k6unx4pudf8k5itoapaxjwzjigz' in str(cont1):
            if r1.history:
                print('\033[94mPossibly open redirection vulnerability with  header injection\033[00m\n'+url+'\nHost '+str(base_domain)+'\nX-Forwarded-Host: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\nX-Host: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\nX-Forwarded-Server: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\nX-HTTP-Host-Override: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\nForwarded: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\n')
            else:
                print('\033[91mPossibly SSRF vulnerability with  header injection\033[00m\n'+url+'\nHost '+str(base_domain)+'\nX-Forwarded-Host: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\nX-Host: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\nX-Forwarded-Server: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\nX-HTTP-Host-Override: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\nForwarded: omeg0ivn7k95wloyezah7zcqghm7aw.burpcollaborator.net\n')


        else:
            pass
    except:
        pass

def hostheader_(url):
    
    t2 = threading.Thread(target=task2,args=(url,))
    t3 = threading.Thread(target=task3,args=(url,))
    t4 = threading.Thread(target=task4,args=(url,))
    
    t2.start()
    t3.start()
    t4.start()
    
    t2.join(timeout=5)
    t3.join(timeout=5)
    t4.join(timeout=5)



    
          
