import requests
import re
import random
import string
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  


def random_char(n):
       return ''.join(random.choice(string.ascii_letters) for x in range(n))
       
def random_number():
       return ''.join(random.choice('123456789') for x in range(random.randint(1, 5)))





def isAlive(url):
    try:
        r = requests.get(url ,verify=False,timeout=10 )
        resp = r.status_code
        if r :
            if str(resp) != '404' :
                return True
            else:
                return False
        else:
            return False
    except:
        pass







def inject_dir1(link,pay):
    try:
       if link[-1] =="/":
          link=link[:-1]
    except:
        pass
    else:
        pass
    inject_urls=[]
    protocol=link.split(":")[0]
    try:
        link=link.replace('http://','')
        link=link.replace('https://','')
    except:
        pass
    try:
        link=link.split('?')[0]
    except:
        pass
    main_ulr=link.split('/')[0]
    wold=protocol+'://'+main_ulr
    for x in range(1,len(link.split('/'))):
        payload=wold+'/'+pay
        wold+='/'+link.split('/')[x]
        inject_urls.append(payload)
    return inject_urls



def inject_dir(link):
    inject_urls=[]
    protocol=link.split(":")[0]
    baselink=link.split("/")[2]
    baselink=protocol+'://'+baselink
    inject_urls.append(baselink)
    try:
        if link[-1] =="/":
            link=link[:-1]
    except:
        pass
    else:
        pass
    
    protocol=link.split(":")[0]
    try:
        link=link.replace('http://','')
        link=link.replace('https://','')
    except:
        pass
    main_ulr=link.split('/')[0]
    wold=protocol+'://'+main_ulr
    for x in range(1,len(link.split('/'))):
       
        wold+='/'+link.split('/')[x]
        inject_urls.append(wold)
       # print(wold)
        
    return inject_urls



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



def inject_param(link,pay):
    b_link=link.split('?')[0]
    params=link.split('?')[1]
    if len(params) >0:
        param_list=[]
        Plenth=params.split('&')
        for z in Plenth:
            param=z.split('=')[0]
            if param not in param_list:
                param_list.append(param)
            payload=(b_link+'?')
            for y in param_list:
                payload=(payload+y+'='+pay+'&')
            payload=payload[:-1]
        return payload



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



def file_name_inject(f,pay):
    file_=f.replace(f.split('.')[0],pay)
    return file_


def search_color(key,txt):
    lenth=len(key)
    strret=""
    for a in range(len(txt)):
        fin=txt[a]
        world=''
        mov=a+lenth
        for i in range(a,mov):
            try:
                cahar=txt[i]
                world+=cahar
            except IndexError:
                pass
        if world == key:
            strret+="\033[43m{}\033[00m".format(world)
            nl=a+lenth
            break   
        else:
            strret+=fin
    try:
        for z in range(nl,len(txt)):
            fin2=txt[z]
            strret+=fin2
    except:
        pass
    if key in strret:
        return strret
    else:
        pass

            
            
def reflection(link):
    
    payload="TrSAF45"
    
    try:
        url=inject_param(link,payload)
        r = requests.get(url ,verify=False )
        resp = r.content
        x = re.findall("TrSAF45", str(resp))
        if (x):
            return True
        else:
            return False
    except:
        pass



def injecter(link,pay):
    prlst=[]
    b_link=link.split('?')[0]
    params=link.split('?')[1]
    if '&' not in link:
        try:
            paramkey=params.split('=')[1]
            finelurl=b_link+'?'+params.split('=')[0]+'='+pay
            prlst.append(finelurl)
        except:
            pass
    else:
        paramslist=params.split('&')
        for p in paramslist:
            
            key=p.split('=')[0]
            lurl=key+'='+pay+'&'
            fin=b_link+'?'
            for x in paramslist: 
                if x.split('=')[0]==key:
                    fin+=lurl
                else:
                    fin+=x+'&'    
            fin=fin[:-1]    
            prlst.append(fin)
    return prlst


def injecterWithOrginKey(link,pay):
    prlst=[]
    b_link=link.split('?')[0]
    params=link.split('?')[1]
    if '&' not in link:
        try:
            paramkey=params.split('=')[1]
        
            finelurl=b_link+'?'+params.split('=')[0]+'='+paramkey+pay
            prlst.append(finelurl)
        except:
            pass
    else:
        paramslist=params.split('&')
        for p in paramslist:
            key=p.split('=')[0]
            vul=p.split('=')[1]
           
            lurl=key+'='+vul+pay+'&'
            fin=b_link+'?'
            for x in paramslist: 
                if x.split('=')[0]==key:
                    fin+=lurl
                else:
                    fin+=x+'&'    
            fin=fin[:-1]    
            prlst.append(fin)
    return prlst


   
