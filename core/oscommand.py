import threading
import queue
import requests
import random
from core import nano
from core import regex
from requests.packages import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




threads =20

def build_wordlist():
    
    words= queue.Queue()
    for word in regex.OScommand:
        word = word.rstrip()
        words.put(word)
        
    return words

def run(word_queue,url):
    state=False
    while not word_queue.empty():
        attempt = word_queue.get()
        attempt_list = []
        attempt_list.append(attempt)

       
        for brute in attempt_list:
            if state==True:
                break
            user_agent=random.choice(regex.USR_AGENTS)
            headers = {'User-Agent': user_agent }   
            try:
                url = nano.inject_param(url,str(brute))
                r = requests.get(url,headers=headers ,verify=False )
                cont = r.content
                if "uid=" and "gid=" and "groups=" in str(cont):
                    state=True
                    print("\033[91mPossibly OS Command injection vulnerability\033[00m  "+url)
                    break
                else:
                    pass
            except:
               pass
           

word_queue = build_wordlist()
def oscommand_(url):
     for i in range(threads):
         t = threading.Thread(target=run,args=(word_queue,url))
         t.start()



