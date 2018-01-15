import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from html.parser import HTMLParser

class NewParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = False
        self.datas = []

    def handle_attr(self, attrlist, attrname):
        for attr in attrlist:
            if attr[0] == attrname:
                return attr[1]
        return None

    def handle_starttag(self, tag, attrs):
        if tag == 'p' and self.handle_attr(attrs, 'class') == 'p_font':
            self.flag = True

    def handle_endtag(self, tag):
        if tag == 'p': 
            self.flag = False 

    def handle_data(self, data):
        if self.flag == True:
            self.datas.append(data)
    
    def get_datas(self):
        return self.datas




if __name__ == '__main__':
    html = ''
    with open('test.html', 'r') as f:
        for line in f:
            html += line

    parser = NewParser()
    parser.feed(html)
    parser.close()

    datas = parser.get_datas()
    for each in datas:
        print each
