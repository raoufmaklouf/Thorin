import requests
import random
import sys
import threading
import queue

pay=[
'//wp-content/debug.log',
'/assets/npm-debug.log',
'/content/debug.log',
'/data/debug/',
'/debug',
'/debug_error.jsp',
'/debug-output.txt',
'/debug.inc',
'/debug.log',
'/debug.php',
'/debug.py',
'/debug.txt',
'/debug.xml',
'/debug/',
'/mysql_debug.sql',
'/npm-debug.log',
'/wp-content/debug.log'
]

def debug_(i):
     try:
       testlink=i+'/uniq_Str.log'
       test_r = requests.get(testlink,verify=False)
       test_scode=test_r.status_code
         
       for x in pay:
           url=i+x
           r = requests.get(url,verify=False)
           scode=r.status_code
           if str(scode)[0] == '2' or str(scode)[0] == '3' :
                if str(scode) != str(test_scode):
                    print("\033[94m[+] Possibly debug page or file disclosure :\033[00m  "+url)
     except:
        pass
          



