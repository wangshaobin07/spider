# coding=utf-8
import urllib2
import cookielib

## 声明cookieJar对象
cookie = cookielib.CookieJar()

## 创建cookie处理器handler 
handler = urllib2.HTTPCookieProcessor(cookie)

## 通过handler构建opener
opener = urllib2.build_opener(handler)

## 此处的open方法同urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')

for item in cookie:
    print 'Name: ', item.name
    print 'Value: ', item.value
