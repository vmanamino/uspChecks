from html.parser import HTMLParser
import re

class uspHtmlParser(HTMLParser):

    flag = False
    pre_data = False
    post_data = False

    def __init__(self):
        HTMLParser.__init__(self)  

    def handle_starttag(self, tag, attrs): 
        
        # self.pre_data = False
        
        if tag == 'b' or tag == 'i' or tag == 'em':
            # print('inside startag first condition', end=' ')
            # print(tag)                       
            self.flag = True
        else:
            # print('inside startag second else', end=' ')
            # print(tag)      
            self.pre_data = False         
            self.tags.append(tag)
        	       
    def handle_data(self, data):
        # print('this is my data: '+ data)
        # print('this is my tag flag: ', end="")
        # print(self.flag)
        if self.flag:            
            self.flag = False
            # print("pre data flag: ", end='')
            # print(self.pre_data)
            # print('this is my post data flag: ', end='')
            # print(self.post_data)
            if self.pre_data and self.output:
                last_element = self.output[-1]
                new_last_element = last_element +' '+data
                self.output[-1] = new_last_element
                self.post_data = True
            else:
                self.output.append(data)
                self.pre_data = True
                self.post_data = True
        else:
            # print('this is my pre data flag: ', end='')
            # print(self.pre_data)
            # print('this is my post data flag: ', end='')
            # print(self.post_data)
            if not self.pre_data: 
                self.pre_data = True    
                self.output.append(data)
            else:
                if self.post_data:
                    # print('my output', end=' ')
                    # print(self.output)
                    if data and self.output:
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
        usps_parsed = []
        p_newline = re.compile('^\n+$')
        for usp in self.output:
            if not re.findall(p_newline, usp):
                usps_parsed.append(usp)               
        return usps_parsed        
            # count += 1
            # stri += usp
            # if count < output_length:
            #     # here check for hidden characters such as newline and space.  
            #     # remove those usps from the output list
            #     # at the same time, put out the string of parsed usps
            #     stri += ' |'
        # return stri
    @staticmethod
    def usps_as_string(usps_parsed):
        stri = ''
        count = 0
        length = len(usps_parsed)
        for usp in usps_parsed:
            count += 1
            stri += usp
            if count < length:
                stri += ' |'
        return stri


    @staticmethod
    def word_count_summary(usps_parsed):
        count_list = []
        for each_usp in usps_parsed:
            usp_length = len(each_usp.split())
            count_list.append(usp_length)
        return count_list

# special_tags = "<p>You will be told each step of the way, not only <i>how</i> to use Excel, but also <i>why</i> you are doing each step – so you can learn the techniques to apply Excel beyond this book</p><p>You will learn both how to write statistical formulas and how to use drop-down menus to have Excel create formulas for you</p>"
# special_tags2 = "<p>You will be told each step of the way, not only <i>how</i> to use Excel, but also <i>why</i> you are doing each step – so you can learn the techniques to apply Excel beyond this book</p><p>You will be told each step of the way, not only <i>how</i> to use Excel, but also <i>why</i> you are doing each step – so you can learn the techniques to apply Excel beyond this book</p>"
# special_tags3 = "<p><b>In der Krise lesbar</b>: Wissenschaftlich fundiert und verständlich formuliert</p><p><b>Erfahrenes Autorenteam</b>: Beteiligt Praktikerin, Betroffene, Wissenschaftler</p><p><b>Beratung</b>: Kurze Übersicht mit praktischen Hinweisen</p><p><b>Menschlich</b>: Nicht medizinisch auf Krebsarten bezogen, sondern auf die Ressource Menschlichkeit</p>"
# swirlytags = "<p>You will be told each step of the way, not only <i>how</i> to use Excel, but also <i>why</i> you are doing each step – so you can learn the techniques to apply Excel beyond this book</p><p><b>Erfahrenes Autorenteam</b>: Beteiligt Praktikerin, Betroffene, Wissenschaftler</p><p><em>Beratung</em>: Kurze Übersicht mit praktischen Hinweisen</p>"
# print(special_tags3)
# print(special_tags2)        
# divTag = '<div>usp1</div><div>usp2</div><div>usp3</div>'
# divTag2 = '<div>usp1</div>'
# brTag = """USP 1<br>USP II<br>USP-3"""
# liTag_divWrapped_target = """<div><ul><li>USP 1</li><li>USP 2</li><li>USP-3</li></ul></div>"""
# divTag_wrap = """<div>USP 1</div><div><br></div><div>USP 2</div><div><br></div><div>USP-3</div><div><br></div><div>USP 4</div>"""
# none = """USP 1  USP2  USP-3"""
# parser = uspHtmlParser()
# print(special_tags)
# parser.feed(special_tags)
# print(parser.tags)
# print(parser.output)
# count_summ = parser.word_count_summary()
# if all(i <= 36 for i in count_summ):
#     print(count_summ)
# data = parser.feed(none)
# print(parser.output)
# print(len(parser.tags))
# usp = usp.USP()
# vanilla = "<p>USP 1</p><p>USP 2</p><p>USP-3</p>"
# parser.feed(vanilla)
# print(parser.usps_parsed())
# print(parser.tags)
# print(parser.output)
# newlines = """<p>Ergänzende Aufgabensammlung zum Werk Technische Mechanik 1, 2, 3 </p><p>Die meisten Beispiele entsprechen in Art und Umfang den Aufgaben, die in Diplomvorprüfungen zu den Fächern Technische Mechanik 1 bis 3 gestellt werden </p>

# <p>Besonders wertvoll für Studierende, die sich auf die jeweiligen Prüfungen vorbereiten </p>

# Das Aufgabenbuch zu den Bestseller-Lehrbüchern der Technischen Mechanik"""

# print(newlines)

# parser = uspHtmlParser()

# parser.feed(newlines)

# print(len(parser.output))

# usps = parser.usps_parsed()

# print(usps)
# print(len(usps))

# print(parser.usps_as_string(usps))

# print(parser.word_count_summary(usps))
