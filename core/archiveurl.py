import requests
import json
import re 



def waybackurls(host):
    cont=[]
    
    url = 'http://web.archive.org/cdx/search/cdx?url={}/*&output=json&fl=original&collapse=urlkey'.format(host)
    r = requests.get(url,headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'})
    results = r.json()
    results=results[1:]
    json_urls = json.dumps(results)
    y=str(json_urls).split()
    for x in y:
        x=x.replace('[[','')
        x=x.replace('"]]','')
        x=x.replace('["', '')
        x=x.replace('"],', '')
        x=x.replace('"', '')
        try:
            x=x.replace(':80', '')
        except:
            pass
        cont.append(x)
   
    return cont
