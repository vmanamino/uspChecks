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
        
        if tag == 'b' or tag == 'i' or tag == 'em' or tag == 'sup' or tag == 'strong' or tag == 'sub':
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
        lonely_lowercases = []
        # p_newline = re.compile('^\n+$')
        p_whitespace = re.compile('^\s+$')   
        for each_usp in self.output:
            joined = False
            usp = ''
            if not re.findall(p_whitespace, each_usp):
                usp_length = len(each_usp.split())                
                if usp_length is 1 and each_usp.islower():                    
                    usp_lonely = each_usp
                    lonely_lowercases.append(usp_lonely)
                    if len(usps_parsed) is not 0:
                        joined = True
                        usp_incomplete = usps_parsed[-1]
                        usp = usp_incomplete +' '+usp_lonely
                    else:
                        usp = usp_lonely
                else:
                    usp = each_usp
                if joined:
                    usps_parsed[-1] = usp
                else:
                    usps_parsed.append(usp)               
        return usps_parsed, lonely_lowercases        
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
        one_count_lowercase = []
        for each_usp in usps_parsed:
            usp_length = len(each_usp.split())
            count_list.append(usp_length)
            # if usp_length is 1 and each_usp.islower():
                # one_count_lowercase.append(each_usp)
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




# parser = uspHtmlParser()

# parser.feed(newlines)

# print(len(parser.output))

# usps = parser.usps_parsed()

# print(usps)
# print(len(usps))

# print(parser.usps_as_string(usps))

# print(parser.word_count_summary(usps))

# nother hidden one
# hidden2 ="""<p>Implements a novel integrated method for detecting the wellness of individuals</p><p>Presents new developments and advancements in wireless sensors for the field of ambient assisted living</p><p> </p><p>Examines emerging applications in a broad range of fields</p>

# <p>&nbsp;</p>"""

# hidden3 = """<p>Presents exact analytical solutions for second order differential equations of any order of nonlinearity, with many examples</p><p>Features original approximate solving methods for strong nonlinear differential equations</p><p> </p><p>Also considers strong nonlinear oscillators with one and two degrees of freedom, but also continuous vibrating systems</p><p>Stresses the potential for applications of the method described in engineering</p><p>Contains examples for better learning</p><p>Supplies the mathematical basics in the supplement&nbsp;</p>"""

# print(hidden3)

# single_word = "<p>Aktuell</p><p>Innovativ </p><p>Kompakt</p>"

# single_word = "<p>Includes clear explanations of fundamentals for correct application</p><p>Contains key notes, experiences and implementation advice from</p><p>experts</p><p>Covers relevant and current topics including Drug Metabolizing Enzymes and Transporters</p>"

# parser = uspHtmlParser()
# parser.feed(single_word)
# usps_parsed, one_count_lowercase = parser.usps_parsed()
# print(usps_parsed)
# print(one_count_lowercase)
# print(parser.word_count_summary(usps_parsed))
# print(parser.word_count_summary(usps_parsed))

# special = "Der Kindler kompakt-Band bietet eine Auswahl von ca. 60 Texten zu Märchen und Märchensammlungen aus allen Zeiten und Nationen, angefangen bei&nbsp;Tausendundeine Nacht über die deutschen, nordischen und russischen Märchen der Romantik bis hin zu den Endes, Lindgrens, Rowlings unserer Tage<div>Ein Einleitung des Herausgebers gibt eine kompakte und unterhaltsame Einführung in das Genre</div>"
# # print(special)
# parser = uspHtmlParser()
# parser.feed(special)
# usps_parsed = parser.usps_parsed()
# print(parser.usps_parsed())
# print(len(parser.tags))

# strong = "<ul><li><em>Numerical Python</em><strong> </strong>by <strong>Robert Johansson</strong> shows you how to leverage the numerical and mathematical modules in Python and its Standard Library.</li><li>It covers the popular open source numerical Python packages like NumPy, FiPy, Pillow, matplotlib and more.</li><li>Applications include those from business management, big data/cloud computing, financial engineering and games.</li></ul>"

# parser = uspHtmlParser()
# parser.feed(strong)
# usps_parsed = parser.usps_parsed()
# print(parser.usps_parsed())
# print(len(parser.tags))

# sub = "<p>Gathers 30 years of experimental research on trees, beginning at the elemental/molecular scale and extending to the tree-stand scale</p><p>Presents the latest experimental findings about the effects of climate change on the mineral content of trees, carbohydrate allocation, tree anatomy, tree growth, leaf longevity, and gas exchange in soil–litter–plant systems</p><p>Investigates the interactive effects of relatively small, realistic increases in temperature and CO<sub>2</sub> concentration&nbsp;</p>"
# parser = uspHtmlParser()
# parser.feed(sub)
# usps_parsed = parser.usps_parsed()
# print(parser.usps_parsed())
# print(len(parser.tags))