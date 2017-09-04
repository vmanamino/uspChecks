from html.parser import HTMLParser

class uspHtmlParser(HTMLParser):
    flag = False
    pre_data = False
    def __init__(self):
        HTMLParser.__init__(self)  

    def handle_starttag(self, tag, attrs): 
        if tag == 'i':
            self.flag = True
        else:   
            self.tags.append(tag)
        	       
    def handle_data(self, data):
        if self.flag:
            print(self.flag, end=' ')
            print('tag data:'+ data)
            self.flag = False
            if self.pre_data:
                last_element = self.output[-1]
                new_last_element = last_element +' '+data
                self.output[-1] = new_last_element
        else:
            self.pre_data = True    
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

special_tags = "<p>You will be told each step of the way, not only <i>how</i> to use Excel, but also <i>why</i> you are doing each step – so you can learn the techniques to apply Excel beyond this book</p><p>You will learn both how to write statistical formulas and how to use drop-down menus to have Excel create formulas for you</p>"
print(special_tags)        
# divTag = '<div>usp1</div><div>usp2</div><div>usp3</div>'
# divTag2 = '<div>usp1</div>'
# brTag = """USP 1<br>USP II<br>USP-3"""
# liTag_divWrapped_target = """<div><ul><li>USP 1</li><li>USP 2</li><li>USP-3</li></ul></div>"""
# divTag_wrap = """<div>USP 1</div><div><br></div><div>USP 2</div><div><br></div><div>USP-3</div><div><br></div><div>USP 4</div>"""
# none = """USP 1  USP2  USP-3"""
parser = uspHtmlParser()
# data = parser.feed(none)
# print(parser.output)
# print(len(parser.tags))
# usp = usp.USP()

parser.feed(special_tags)
# print(parser.usps_parsed())
print(parser.tags)
print(parser.output)








