import urllib
import urllib2

values = {'username': 'wangshaobin07@163.com', 'password': 'xxxx'}
data = urllib.urlencode(values)
url = 'https://mail.163.com/'
request = urllib2.Request(url, data)

response = urllib2.urlopen(request)

print response.read()
