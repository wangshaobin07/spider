import urllib2
enable_proxy = True

proxy_handler = urllib2.ProxyHandler({'http': 'http://some-proxy.com:8080'})

proxy_handler_null = urllib2.ProxyHandler({})

if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(proxy_handler_null)

urllib2.install_opener(opener)

