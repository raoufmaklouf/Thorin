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
    url=str(url)
    for x in regex.parameters_OR:
            param=(x+"=")
            if param url:
                try:
                    base_link=url.split(param)[0]
                except:
                    pass
                f_link=base_link+param
                while not word_queue.empty():
                    attempt = word_queue.get()
                    attempt_list = []
                    attempt_list.append(attempt)
        
                    for brute in attempt_list:
                        user_agent=random.choice(regex.USR_AGENTS)
                        headers = {'User-Agent': user_agent } 
                        url = f_link+brute
                        
                       
                        try:         
                            r = requests.get(url, headers=headers,verify=False)
                            resp=r.content       
                            if len(r.history)>0 and "<title>Google</title>" in str(resp) :
                                print('\033[91m Possibly open redirection vulnerability\033[00m\t'+url)
                                break
                            else:
                                pass
                        except :
                            pass
           
word_queue = build_wordlist()
def redirect_(url):
    for i in range(threads):
        t = threading.Thread(target=run,args=(word_queue,url))
        t.start()
        

threads_dir =20

def build_wordlist_dir():
  
    words= queue.Queue()
    for word in regex.payloads_OR_d:
        word = word.rstrip()
        words.put(word)
        
    return words

def run_dir(word_queue,url):
     
    while not word_queue.empty():
        attempt = word_queue.get()
        attempt_list = []
        attempt_list.append(attempt)
        
        for brute in attempt_list:
            user_agent=random.choice(regex.USR_AGENTS)
            headers = {'User-Agent': user_agent } 
            url=str(url).replace('uNiq_stRiNg',str(brute))
            try:
                r = requests.get(url,headers=headers,verify=False)
                resp=r.content       
                if len(r.history)>0 and "<title>Google</title>" in str(resp) :
                    print('\033[91m Possibly open redirection vulnerability\033[00m  '+url)
                    break
                else:
                    pass
            except :
                pass
           
word_queue_dir = build_wordlist_dir()
def redirect_dir(url):
    for i in range(threads_dir):
        t = threading.Thread(target=run_dir,args=(word_queue_dir,url))
        t.start()
       

