from html.parser import HTMLParser
from html.entities import name2codepoint
import requests
import re

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)  
        self.text = [] 
        self.flag = False
    
    def handle_attr(self, attrlist, attrname):
        for attr in attrlist:
            if attr[0] == attrname:
                return attr[1]
        return None

    def handle_starttag(self, tag, attrs):
        if tag == 'div' and self.handle_attr(attrs, 'class') == 'content': 
            self.flag = True

    def handle_endtag(self, tag):
        if tag == 'div':
            self.flag = False

    def handle_data(self, data):
        if self.flag == True:
            self.text.append(data)

    def get_text(self):
        return self.text
        

html = ''
with open('qsbk1.html', 'r') as f:
    for line in f:
        html += line

parser = MyHTMLParser()
parser.feed(html)
parser.close()

text = parser.get_text()
for i in range(len(text)):
    print '%d\t%s' % (i, text[i]) 
    #if not each.startswith('\n'): # and not each.endswith('\n'):
    #    print each
