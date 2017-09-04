from html.parser import HTMLParser

class uspHtmlParser(HTMLParser):

    flag = False
    pre_data = False
    post_data = False

    def __init__(self):
        HTMLParser.__init__(self)  

    def handle_starttag(self, tag, attrs): 
        
        # self.pre_data = False
        
        if tag == 'b' or tag == 'i':                       
            self.flag = True
        else:      
            self.pre_data = False         
            self.tags.append(tag)
        	       
    def handle_data(self, data):
        print('this is my data: '+ data)
        print('this is my tag flag: ', end="")
        print(self.flag)
        if self.flag:            
            self.flag = False
            print("pre data flag: ", end='')
            print(self.pre_data)
            print('this is my post data flag: ', end='')
            print(self.post_data)
            if self.pre_data:
                last_element = self.output[-1]
                new_last_element = last_element +' '+data
                self.output[-1] = new_last_element
                self.post_data = True
            else:
                self.output.append(data)
                self.pre_data = True
                self.post_data = True
        else:
            print('this is my pre data flag: ', end='')
            print(self.pre_data)
            print('this is my post data flag: ', end='')
            print(self.post_data)
            if not self.pre_data: 
                self.pre_data = True    
                self.output.append(data)
            else:
                if self.post_data:
                    if data:
                        last_element = self.output[-1]
                        new_last_element = last_element +' '+data
                        self.output[-1] = new_last_element
                        self.post_data = False
                        self.pre_data = True
                else:
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
special_tags2 = "<p>You will be told each step of the way, not only <i>how</i> to use Excel, but also <i>why</i> you are doing each step – so you can learn the techniques to apply Excel beyond this book</p><p>You will be told each step of the way, not only <i>how</i> to use Excel, but also <i>why</i> you are doing each step – so you can learn the techniques to apply Excel beyond this book</p>"
special_tags3 = "<p><b>In der Krise lesbar</b>: Wissenschaftlich fundiert und verständlich formuliert</p><p><b>Erfahrenes Autorenteam</b>: Beteiligt Praktikerin, Betroffene, Wissenschaftler</p><p><b>Beratung</b>: Kurze Übersicht mit praktischen Hinweisen</p><p><b>Menschlich</b>: Nicht medizinisch auf Krebsarten bezogen, sondern auf die Ressource Menschlichkeit</p>"
swirlytags = "<p>You will be told each step of the way, not only <i>how</i> to use Excel, but also <i>why</i> you are doing each step – so you can learn the techniques to apply Excel beyond this book</p><p><b>Erfahrenes Autorenteam</b>: Beteiligt Praktikerin, Betroffene, Wissenschaftler</p>"
print(special_tags3)
# print(special_tags2)        
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

parser.feed(special_tags3)
# print(parser.usps_parsed())
print(parser.tags)
print(parser.output)








