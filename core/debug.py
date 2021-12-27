import requests
from core import nano

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
       
         
       for x in pay:
           url=i+x
           r = requests.get(url,verify=False)
           resp = r.content
           scode=r.status_code
           if str(scode)[0] == '2' or str(scode)[0] == '3' :
                r2=requests.get(url+nano.random_char(3),verify=False)
                test_scode=r2.status_code
                if str(scode) != str(test_scode):
                    print("\033[94m[+] Possibly debug page or file disclosure :\033[00m\n"+url+" scode:"+str(scode)+"length:"+len(resp))
    except:
        pass
          


