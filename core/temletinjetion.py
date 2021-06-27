import requests
import re
from core import nano
from core import regex

from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


test1="58784"
test2='32110'
mt='InKgg67\[2s4h7jT67HF5)o[>,j'
def ssti_(url):
   
    try:
        for link in nano.injecter(url,mt):
            for x in regex.payload_ssti_1:
                url1=link.replace(mt,x)
                r = requests.get(url1,verify=False,timeout=13)
                cont1 = r.content
                if(re.search(test1, str(cont1))):
                    for i in regex.payload_ssti_2:
                        url2=url1=link.replace(mt,i)
                        r = requests.get(url2,verify=False,timeout=13)
                        cont2 = r.content
                        if(re.search(test2, str(cont2))):
                            print("\033[91m Possibly SS template injection vulnerability\033[00m\t"+url2)
                            break
                        else:
                            pass
    except:
        pass
        

        




