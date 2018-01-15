import urllib2
response = urllib2.urlopen("http://www.baidu.com")
print response.read()

## or mk requests firstly
request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print response.read()


