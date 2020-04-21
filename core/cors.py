import requests
import random
from core import regex
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def cors_(url):
    user_agent=random.choice(regex.USR_AGENTS)
    headers={"Origin":"https://etdbeuajsyeu.com" ,'User-Agent':user_agent }
    try:
        r=requests.get(url,headers=headers ,verify=False)
        origen=r.headers.get('Access-Control-Allow-Origin')
        credentials=r.headers.get('Access-Control-Allow-Credentials')
        if "https://etdbeuajsyeu.com" in str(origen) and 'true' in str(credentials):
            print('\033[91m Possibly CORS vulnerability\033[00m  '+url)
        else:
            pass
        r=requests.post(url, headers=headers ,verify=False)
        origen=r.headers.get('Access-Control-Allow-Origin')
        credentials=r.headers.get('Access-Control-Allow-Credentials')
        if "https://etdbeuajsyeu.com" in str(origen) and 'true' in str(credentials):
            print('\033[91m Possibly CORS vulnerability\033[00m  '+url)
        else:
            pass
    except:
        pass



