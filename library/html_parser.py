from html.parser import HTMLParser
import usp

class MyHTMLParser(HTMLParser):

    def __init__(self, usp):
        HTMLParser.__init__(self)  
        self.start = ''
        self.end = ''
        self.data = ''
        self.usps = []	       
    def handle_starttag(self, tag, attrs):
        self.start = tag
        usp.start_tag = tag
    def handle_endtag(self, tag):
        self.end = tag
        usp.end_tag = tag
    def handle_data(self, data):
        self.data = data
        usp.data = data
        self.usps.append(usp)
divTag = '<div>usp1</div><div>usp2</div><div>usp3</div>'


usp = usp.USP()
parser = MyHTMLParser(usp)
parser.feed(divTag)
print(parser.usps[1].data)



