import re 
import requests
import random
from core import regex
from core import nano
from core import bot
from core import config
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 


def ssrf_(i):
    
    try:
        for url in nano.injecter(i,config.ssrf_link):
      
            user_agent=random.choice(regex.USR_AGENTS)
            headers = {'User-Agent': user_agent } 
            r = requests.get(url ,headers=headers ,verify=False,timeout=13 )       
            resp = r.content
            x = re.findall(config.ssrf_regix, str(resp))
            if (x):
                print('\033[91mPossibly SSRF vulnerability\033[00m  '+url)
                msg="Possibly SSRF vulnerability "+url
                bot.telegram_bot_sendtext(msg)
    except:
        pass
                       
