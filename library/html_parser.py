from html.parser import HTMLParser

class uspHtmlParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)  
        	       
    def handle_data(self, data):
        self.output.append(data)
        
    def feed(self, data):        
        self.output = []

        HTMLParser.feed(self, data)
        
divTag = '<div>usp1</div><div>usp2</div><div>usp3</div>'
divTag2 = '<div>usp1</div>'
brTag = """USP 1<br>USP II<br>USP-3"""
divTag_wrap = """<div>USP 1</div><div><br></div><div>USP 2</div><div><br></div><div>USP-3</div><div><br></div><div>USP 4</div>"""
none = """USP 1  USP2  USP-3"""
# usp = usp.USP()






