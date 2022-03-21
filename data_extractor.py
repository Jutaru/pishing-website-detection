import re
from bs4 import BeautifulSoup
import urllib
import urllib.request

url = "https://shadetreetechnology.com/V4/validation/a111aedc8ae390eabcfa130e041a10a4"

sensitive_words = "confirm|account|banking|secure|ebyisapi|webscr|signin|mail|install|toolbar|backup|paypal|password|username"


shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                      r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                      r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                      r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                      r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                      r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                      r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                      r"tr\.im|link\.zip\.net"


def haveIP(url):
     result = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",url)
     if(result != None):
         return 1
     return 0

def haveAt(url):
    result = re.search("@", url)
    if (result != None):
        return 1
    return 0

def nbDots(url):
    result = url.count(".")
    return result

def prefix(url):
    segm = url.split('/')
    result = segm[2].find('-')
    if result == -1:
        return 0
    return 1

def redirection(url):
    result = url.count("//")
    if result > 1 :
        return 1
    return 0


def httpToken(url):
    segm = url.split(':')
    if segm[0] == "http":
        return 0
    return 1

def tinyURL(url):
    match=re.search(shortening_services,url)
    if match:
        return 1
    return 0

def getLength(url):
  if len(url) < 54:
    length = 0
  else:
    length = 1
  return length

def depthURL(url):
    result = url.count('/');
    return result - 2

def sensitiveWord(url):
    match = re.search(sensitive_words, url)
    if match:
        return 1
    return 0

def web_traffic(url):
  try:
    url = urllib.parse.quote(url)
    rank = BeautifulSoup(urllib.request.urlopen("http://data.alexa.com/data?cli=10&dat=s&url=" + url).read(), "xml").find(
        "REACH")['RANK']
    rank = int(rank)
  except :
        return 1
  if rank > 100000:
    return 1
  else:
    return 0




