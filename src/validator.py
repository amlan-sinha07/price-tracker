from urllib.parse import urlsplit , urlunsplit
def normalize_url(url):
    parsed=urlsplit(url.strip())
def is_valid_url(url):
    if not isinstance(url,str) or not url.split():
        return False
    if any(char.isspace() for char in url):
        return False
    try:
        parsed_url=urlsplit(url.strip())
        #validate the port fromat if one is specified
        _=parsed_url.port
        if parsed_url.scheme.lower() not in ("http","https"):
            return False
        if not parsed_url.hostname :
            return False
        return True
    except ValueError:
        return False
# how does urlsplit() works
'''
scheme= https
netloc= example.com
hostname = example.com
path= products/keyboard
'''

