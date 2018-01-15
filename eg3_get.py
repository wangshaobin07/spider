import urllib
import urllib2

values = {'username': 'wangshaobin07@163.com', 'password': 'xxxx'}
data = urllib.urlencode(values)
url = 'https://mail.163.com/'
geturl = url + '?' + data
request = urllib2.Request(geturl)

response = urllib2.urlopen(request)

print response.read()
