# Thorin
The tool collects endpoints from web archive and analyzes it and scan it from many vulnerabilities
## Features 
**Vulnerability:** 
* xss 
* open redirection 
* sql injection simple and blind and error base 
* local file inclusion 
* server-side template injection 
* crlf 
* os comman injection  
* HTTP PUT Method Enabled
* cross-origin resource sharing

**Other features:**
* Detect sensitive url like: .git or .svn folder/ Backup file like .back or .save or .old / token or api keys in url  like(slack,twilio,heroku,mailchamp,amazon,...)
* Detect base64 in url 
* Detect js files and and searching for data that might be sensitive, such as links or tokens or api keys 

## Usage
**Install:**

`git clone https://github.com/raoufmaklouf/Thorin.git`

`cd Thorin`

`pip3 install -r requirements.txt
`

**Run:**

`python3 thorin domain.com
`

`python3 thorin sub.domain.com
`

![Alt text](https://raw.githubusercontent.com/raoufmaklouf/Thorin/master/pictures/Screenshot%20at%202020-04-20%2014-50-45.jpg?raw=true "Title")

![Alt text](https://raw.githubusercontent.com/raoufmaklouf/Thorin/master/pictures/Screenshot%20at%202020-04-26%2016-04-30.jpg?raw=true "Title")


# **Author** #
*raouf maklouf*
* Facebook: [https://www.facebook.com/raouf.maklouf]
* Linkedin: [https://www.linkedin.com/in/raouf-maklouf-505a061a0/]
