<h1 align="center">
Thorin
</h1>

![alt text](https://github.com/raoufmaklouf/Thorin/blob/master/pictures/thorin2.png)

💬 description
-----
web application scanner Focuses on checking inputs and misconfiguration

💪 Features
-----

* collects endpoints from web archive and scan it
* scan file list of endpoints
* scan one url

**Vulnerability:** 
* xss 
* ssrf
* open redirection 
* sql injection  
* local file inclusion 
* server-side template injection 
* crlf 
* os comman injection  
* cross-origin resource sharing
* host header attacks

**Other features:**
* Detect sensitive url like: .git or .svn folder/ Backup file like .back or .save or .old / token or api keys in url  like(slack,twilio,heroku,mailchamp,amazon,...)
* Detect base64 in url 
* Detect Sensitive data such as links or tokens or api keys in source code
* Brute Force Backup File

![alt text](https://github.com/raoufmaklouf/Thorin/blob/master/pictures/Screenshot%20at%202021-01-31%2015-04-16.png)

## Usage
**Install:**

`git clone https://github.com/raoufmaklouf/Thorin.git`

`cd Thorin`

`pip3 install -r requirements.txt
`

**Run:**

`python3 thorin.py -d domain.com` & `python3 thorin.py -d sub.domain.com`


 `python3 thorin.py -f endpointfile.txt`
 
 
 `python3 thorin.py -r http://sub.domain.com/index.php?p=fuzz`



# **Author** #
*raouf maklouf*
* Facebook: [https://www.facebook.com/raouf.maklouf]
* Linkedin: [https://www.linkedin.com/in/raouf-maklouf-505a061a0/]
