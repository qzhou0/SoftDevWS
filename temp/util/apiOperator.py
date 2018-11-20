import json
from urllib import request

def apiRetrieve(URL_STUB, URL_other):
    URL=URL_STUB+URL_other
    response = request.urlopen(req)
    s = response.read()

    d = json.load(s)
    return d
