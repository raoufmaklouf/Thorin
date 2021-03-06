# Thorin v2
The tool collects endpoints from web archive and analyzes it and scan it from many vulnerabilities
## Features 
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

**Other features:**
* Detect sensitive url like: .git or .svn folder/ Backup file like .back or .save or .old / token or api keys in url  like(slack,twilio,heroku,mailchamp,amazon,...)
* Detect base64 in url 
* Detect js files and and searching for data that might be sensitive, such as links or tokens or api keys 

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



# **Author** #
*raouf maklouf*
* Facebook: [https://www.facebook.com/raouf.maklouf]
* Linkedin: [https://www.linkedin.com/in/raouf-maklouf-505a061a0/]
