from core import nano
from core import regex 
import threading
import queue
import requests
import re
import random


from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

threads =10

def build_wordlist():
  
    words= queue.Queue()

    for word in regex.payloads_OR_p:
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
            headers = {'User-Agent': user_agent } 
            
                        
                       
            try:
                url = url=nano.inject_param(url,str(brute))
                r = requests.get(url,headers=headers,verify=False)
                cont=r.content
                if 'k6unx4pudf8k5itoapaxjwzjigz' in str(cont):
                    if r.history :
                        print('\033[91m Possibly open redirection vulnerability\033[00m '+url) 
                       
                    else:
                        print('\033[91m Possibly SSRF vulnerability\033[00m '+url) 
                                                  
                                          
                            
            except :
                pass
           
word_queue = build_wordlist()
def redirect_(url):
    for i in range(threads):
        t = threading.Thread(target=run,args=(word_queue,url))
        t.start()
