# encoding: utf-8

import requests
from HTMLParser import HTMLParser
import re

class DZCrawl(object):
    def __init__(self):
        object.__init__(self)
        self.DZlist = []

    def getDZ_Page(self, page):
        s = str(page)
        url = 'http://www.tduanzi.com/tweets/?tps=1&page=%s' % s
        r = requests.get(url)
        p = DZParser()
        p.feed(r.content)
        with open('dz.txt', 'wr') as f:
            for one in p.DZList:
                f.write("*******段子******\n")
                f.write(one)
                f.write("\n\n")


class DZParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_ul = False
        self.in_div = False
        self.in_div_and_a = False
        self.pattern = re.compile(r'tweets[0-9]+')
        self.DZList = []

    def handle_starttag(self, tag, attrs):
        if tag == 'ul': # and self.pattern.match(_attrValue(attrs, 'id')):
            self.in_ul = True

        if self.in_ul and tag == 'div' and _attrValue(attrs, 'class') == 'right':
            self.in_div = True

        if self.in_ul and tag == 'a' and _attrValue(attrs, 'class') == 'black' and _attrValue(attrs, 'target') == '_blank':
            self.in_div_and_a = True

    def handle_endtag(self, tag):
        if tag == 'a':
            self.in_div_and_a = False
        if tag == 'div':
            self.in_div = False
        if tag == 'li':
            self.in_li = False

    def handle_data(self, data):
        if self.in_div_and_a:
            print("******段子******")
            print(data)
            self.DZList.append(data)


def _attrValue(attrs, attrKey):
    for attr in attrs:
        if(attr[0] == attrKey):
            return attr[1]
    return None


if __name__ == '__main__':
    DZClient = DZCrawl()
    DZClient.getDZ_Page(1)
