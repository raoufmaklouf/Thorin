import re
import base64
import binascii
from core import nano
from core import regex

def dir_(url):
    try:
        
        Dir=str(url).split('/')
        for item in Dir:
            if item not in regex.Base_64_white_list and len(item) > 10:
                mutch=re.search("^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)$",item)
                if(mutch):
                    m=mutch.group()

                
                    try:
                        decodebs64=base64.b64decode(m)
                        try:
    
                            if "\\x" not in str(decodebs64):
                                print("\033[94m[INFO] Possibly base64 on url:\033[00m {} ".format(nano.search_color(str(m),url)))
                                print("\033[32m[decode is] ----------|\033[00m "+str(decodebs64))
                        
                        except UnicodeError:
                            pass

                    except binascii.Error:
                        pass
    except:
        pass

def param_(url):
    try:
        basedir=url.split('?')[1]
        item=basedir.split('&')
        c=''
        for x in item:
            if nano.rev(x)[0] == '=':
                c+='='
                if nano.rev(x)[1] == '=':
                    c+='='
                    if nano.rev(x)[2] == '=':
                        c+='='
                        
            fstring=x.split('=')[1]
            fstring+=c
            if fstring not in regex.Base_64_white_list and len(fstring) > 10:
                mutch=re.search("^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)$",fstring)
                if(mutch):
                    m=mutch.group()

                    try:
                        decodebs64=base64.b64decode(m)
                        try:
                        
                            if "\\x" not in str(decodebs64):
                                print("\033[94m[INFO] Possibly base64 on url:\033[00m {} ".format(nano.search_color(str(m),url)))
                                print("\033[32m[decode is] ----------|\033[00m "+str(decodebs64))
                        
                        except UnicodeError:
                            pass
               
                    except binascii.Error:
                        pass

    except:
        pass



def Base64_(url):
    dir_(url)
    param_(url)
