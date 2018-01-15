import urllib2
import urllib
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozila/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    print content 
    #pattern = re.compile('<div.*author>.*?<a.*?<img.*?>(.*?)</a>.*
    pattern = re.compile(r'<span>(.*?)</span>', re.M)
    m = re.search(pattern, content)
    '''
    if m:
        print m.group(1)
    else:
        print 'no match'
    '''
except urllib2.URLError as e:
    if hasattr(e, 'code'):
        print e.code
    if hasattr(e, 'reason'):
        print e.reason
