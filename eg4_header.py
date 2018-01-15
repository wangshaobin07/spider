import urllib
import urllib2

url = 'http://www.server.com/login'

user_agent = 'Mozill:a/4.0 (compatible; MSIE 5.5; Windows NT)'
header = {'User-Agent': user_agent, 'Refer': 'http://www.zhihu.com/articles'}

values = {'username': 'xxx', 'password': 'xxx'}
data = urllib.urlencode(values)

request = urllib2.Request(url, data, header)

response = urllib2.urlopen(request)

page = response.read()

