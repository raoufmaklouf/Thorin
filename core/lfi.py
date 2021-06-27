import threading
import queue
import requests
import re
import random
from core import nano
from core import regex
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


threads =30
rg1="root:[x*]:0:0:"
rg2="\\[(font|extension|file)s\\]"
def build_wordlist():
    
    words= queue.Queue()
    for word in regex.LFI:
        word = word.rstrip()
        words.put(word)
        
    return words

def run(word_queue,url):
    
    while not word_queue.empty():
        attempt = word_queue.get()
        attempt_list = []
        attempt_list.append(attempt)

       
        for brute in attempt_list:  
            user_agent=random.choice(regex.USR_AGENTS)
            headers={'User-Agent':user_agent }
            try: 
                for link in nano.injecter(url,brute):
                    r = requests.get(link,headers=headers,verify=False,timeout=13)
                    resp= r.content
                    x1 = re.findall(rg1, str(resp))
                    x2 = re.findall(rg2, str(resp))
                    if (x1) or (x2):
                       print('\033[91mPossibly LFI vulnerability\033[00m  '+link)
 
                    else:
                        pass
            except:
               pass
           

word_queue = build_wordlist()
def lfi_(url):
     for i in range(threads):
         t = threading.Thread(target=run,args=(word_queue,url))
         t.start()
         t.join()
         



