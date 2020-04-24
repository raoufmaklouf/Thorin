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
               url=url.replace("b'","")
               url=url.replace("'","")
               r = requests.get(url,headers=headers,verify=False)
               resp= r.content
               if(re.search(':x:', str(resp))):
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
         



def run_dir(word_queue,url):
    
    while not word_queue.empty():
        attempt = word_queue.get()
        attempt_list = []
        attempt_list.append(attempt)

       
        for brute in attempt_list:  
            try:
                url = str(url).replace('uNiq_stRiNg',str(brute))
                url=url.replace("b'","")
                url=url.replace("'","")
                r = requests.get(url,verify=False)
                resp= r.content
                if(re.search(':x:', str(resp))):
                    print("\033[91m Possibly LFI vulnerability\033[00m  "+url)
                    break
                else:
                    pass
            except:
                pass
           
word_queue = build_wordlist()
def lfi_dir(url):
    for i in range(threads):
        t = threading.Thread(target=run_dir,args=(word_queue,url))
        t.start()
       
