from html.parser import HTMLParser

class uspHtmlParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)  

    def handle_starttag(self, tag, attrs):
    	self.tags.append(tag)
        	       
    def handle_data(self, data):
        self.output.append(data)
        
    def feed(self, data):        
        self.output = []
        self.tags = []
        HTMLParser.feed(self, data)

    
    def usps_parsed(self):
        count = 0
        stri = ''
        for usp in self.output:
            count += 1
            stri += usp
            if count < len(self.output):
                stri += ' |'
        return stri
        
# divTag = '<div>usp1</div><div>usp2</div><div>usp3</div>'
# divTag2 = '<div>usp1</div>'
# brTag = """USP 1<br>USP II<br>USP-3"""
# liTag_divWrapped_target = """<div><ul><li>USP 1</li><li>USP 2</li><li>USP-3</li></ul></div>"""
# divTag_wrap = """<div>USP 1</div><div><br></div><div>USP 2</div><div><br></div><div>USP-3</div><div><br></div><div>USP 4</div>"""
# none = """USP 1  USP2  USP-3"""
# parser = uspHtmlParser()
# parser.feed(divTag_wrap)
# print(parser.usps_parsed())
# data = parser.feed(none)
# print(parser.output)
# print(len(parser.tags))
# usp = usp.USP()






