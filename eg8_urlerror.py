import urllib2

req = urllib2.Request('http://blog.csdn.net/cqcr')

try:
    resp = urllib2.urlopen(req)
    print resp.read()
except urllib2.HTTPError as e:
    if hasattr(e, "code"):
        print e.code
except urllib2.URLError as e:
    print e.reason


try:
    resp = urllib2.urlopen(req)
    print resp.read()
except Exception as e:
    print e.code
    print dir(e) 
    # ['_HTTPError__super_init', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__getitem__', '__getslice__', '__hash__', '__init__', '__iter__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__unicode__', '__weakref__', 'args', 'close', 'code', 'errno', 'filename', 'fileno', 'fp', 'getcode', 'geturl', 'hdrs', 'headers', 'info', 'message', 'msg', 'next', 'read', 'readline', 'readlines', 'reason', 'strerror', 'url']

    print e.reason
    print e.info()

