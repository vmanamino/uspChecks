import unittest
import re
import sys
sys.path.append('C:\\Code\\uspChecks\\library')
from html_tags import tag_content
from usp_parser import uspHtmlParser

parser = uspHtmlParser()

'''
Vanilla USPs
'''

pTag_target = """<p>USP 1</p><p>USP 2</p><p>USP-3</p>"""

pTag_one_less = """<p>USP 1 </p><p>USP2	</p>"""

pTag_one_more = """<p>USP 1 </p><p>USP2
 		</p><p>USP-3</p><p>USP 4</p>"""

divTag_target = """<div>USP 1 </div><div>USP2
 		</div><div>USP-3</div>"""

divTag_one_less = """<div>USP 1 </div><div>USP2</div>"""

divTag_one_more = """<div>USP 1 </div><div>USP2
 		</div><div>USP-3</div><div>USP 4</p>"""

brTag_target = """USP 1<br>USP II<br>USP-3"""

brTag_one_less = """USP 1<br>USP II"""

brTag_one_more = """USP 1<br>USP II<br>USP-3<br>USP 4"""

# br tag in XHTML is different <br/>, need test cases

'''
Swirly flavored USPs, i.e. wrapped tags
'''
liTag_divWrapped_target = """<div><ul><li>USP 1</li><li>USP 2</li><li>USP-3</li></ul></div>"""

'''
Chunky swirls, i.e. wrapped tags with random rags thrown in
'''
divTag_wrap_target = """<div>USP 1</div><div><br></div><div>USP 2</div><div><br></div><div>USP-3</div><div><br></div><div>USP 4</div>"""

'''
Squirrelly tags, i.e. tags with bold, italics, and emphasis tags
'''
special_tags = "<p>You will be told each step of the way, not only <i>how</i> to use Excel, but also <i>why</i> you are doing each step – so you can learn the techniques to apply Excel beyond this book</p><p>You will learn both how to write statistical formulas and how to use drop-down menus to have Excel create formulas for you</p>"
special_tags2 = "<p>You will be told each step of the way, not only <i>how</i> to use Excel, but also <i>why</i> you are doing each step – so you can learn the techniques to apply Excel beyond this book</p><p>You will be told each step of the way, not only <i>how</i> to use Excel, but also <i>why</i> you are doing each step – so you can learn the techniques to apply Excel beyond this book</p>"
special_tags3 = "<p><b>In der Krise lesbar</b>: Wissenschaftlich fundiert und verständlich formuliert</p><p><b>Erfahrenes Autorenteam</b>: Beteiligt Praktikerin, Betroffene, Wissenschaftler</p><p><b>Beratung</b>: Kurze Übersicht mit praktischen Hinweisen</p><p><b>Menschlich</b>: Nicht medizinisch auf Krebsarten bezogen, sondern auf die Ressource Menschlichkeit</p>"
special_tags4 = "<p>You will be told each step of the way, not only <i>how</i> to use Excel, but also <i>why</i> you are doing each step – so you can learn the techniques to apply Excel beyond this book</p><p><b>Erfahrenes Autorenteam</b>: Beteiligt Praktikerin, Betroffene, Wissenschaftler</p><p><em>Beratung</em>: Kurze Übersicht mit praktischen Hinweisen</p>"
special_tags_sub = "<p>Describes precise magnetic torque measurement using micro cantilever and local magnetization measurement using micro-Hall array </p><p>Investigates the symmetry breaking in the hidden-order phase of URu<sub>2</sub>Si<sub>2</sub> and vortex state in the superconducting phase</p><p>Covers observation of the vortex lattice melting transition in ultraclean URu<sub>2</sub>Si<sub>2</sub> single crystals at sub-Kelvin temperatures</p><p>Nominated as an outstanding contribution by Kyoto University's Physics Department in 2013</p>"
special_tags_strong = "<ul><li><em>Numerical Python</em><strong> </strong>by <strong>Robert Johansson</strong> shows you how to leverage the numerical and mathematical modules in Python and its Standard Library.</li><li>It covers the popular open source numerical Python packages like NumPy, FiPy, Pillow, matplotlib and more.</li><li>Applications include those from business management, big data/cloud computing, financial engineering and games.</li></ul>"


empty_str = ''
empty_null = None 

'''
Bland USPs, no tags
currently no tests
'''
# two spaces between each USP
tag_none = """USP 1  
			USP2  
			USP-3"""


'''
newlines
'''
newlines = """<p>USP 1 </p>

<p>USP 2 </p>

<p>USP 3 </p>

USP 4"""

whitespace1 = """<p>USP 1</p><p>USP 2</p><p> </p><p>USP 3</p>

<p>&nbsp;</p>"""

whitespace2 = """<p>USP 1</p><p>USP 2</p><p> </p><p>USP 3</p><p>USP 4</p><p>USP 4&nbsp;</p>"""

single_word = "<p>Includes clear explanations of fundamentals for correct application</p><p>Contains key notes, experiences and implementation advice from</p><p>experts</p><p>Covers relevant and current topics including Drug Metabolizing Enzymes and Transporters</p>"

# usps = parser.feed(pTag_target)
# print(parser.output)
class isUSPTests(unittest.TestCase):	
	
	def test_vanilla_One(self):
		parser.feed(pTag_target)
		self.assertTrue(len(parser.output) is 3)
		parser.feed(divTag_target)
		self.assertTrue(len(parser.output) is 3)
		parser.feed(brTag_target)
		self.assertTrue(len(parser.output) is 3)

	def test_vanilla_Two(self):
		parser.feed(pTag_one_less)
		self.assertFalse(len(parser.output) is 3)
		parser.feed(divTag_one_less)
		self.assertFalse(len(parser.output) is 3)
		parser.feed(brTag_one_less)
		self.assertFalse(len(parser.output) is 3)

	def test_vanilla_Three(self):
		parser.feed(pTag_one_more)
		self.assertFalse(len(parser.output) is 3)
		parser.feed(divTag_one_more)
		self.assertFalse(len(parser.output) is 3)
		parser.feed(brTag_one_more)
		self.assertFalse(len(parser.output) is 3)

	# tags wrapped by other tags, well formed HTML
	def test_swirl_One(self):
		parser.feed(liTag_divWrapped_target)
		self.assertTrue(len(parser.output) is 3)

	# random tags with no usp content thrown in
	def test_chunky_One(self):
		parser.feed(divTag_wrap_target)
		self.assertTrue(len(parser.output) is 4)

	def test_squirrelly_One(self):
		parser.feed(special_tags)
		self.assertTrue(len(parser.output) is 2)

	def test_squirrelly_Two(self):
		parser.feed(special_tags2)
		self.assertTrue(len(parser.output) is 2)

	def test_squirrelly_Three(self):
		parser.feed(special_tags3)
		self.assertTrue(len(parser.output) is 4)

	def test_squirrelly_Four(self):
		parser.feed(special_tags4)
		self.assertTrue(len(parser.output) is 3)

	def test_squirrelly_Five(self):
		parser.feed(special_tags_sub)
		self.assertTrue(len(parser.output) is 4)
		parser.feed(special_tags_strong)
		self.assertTrue(len(parser.output) is 3)


class isTagTests(unittest.TestCase):

	def test_vanilla_One(self):
		parser.feed(pTag_target)
		self.assertTrue(len(parser.tags) is 3)
		parser.feed(divTag_target)
		self.assertTrue(len(parser.tags) is 3)
		parser.feed(brTag_target)
		self.assertTrue(len(parser.tags) is 2)

	def test_swirl_One(self):
		parser.feed(liTag_divWrapped_target)
		self.assertTrue(len(parser.tags) is 5)

	def test_chunky_One(self):
		parser.feed(divTag_wrap_target)
		self.assertTrue(len(parser.tags) is 10)

class isContentTests(unittest.TestCase):

	def test_vanilla_One(self):
		parser.feed(pTag_target)			
		self.assertTrue(parser.usps_parsed() == (['USP 1', 'USP 2', 'USP-3'], []))

	def test_swirl_One(self):
		parser.feed(liTag_divWrapped_target)
		self.assertTrue(parser.usps_parsed() == (['USP 1', 'USP 2', 'USP-3'], []))

	def test_chunky_One(self):
		parser.feed(divTag_wrap_target)
		self.assertTrue(parser.usps_parsed() == (['USP 1', 'USP 2', 'USP-3', 'USP 4'], []))

	def test_whitespace_One(self):
		parser.feed(newlines)
		# print(parser.usps_parsed())
		self.assertTrue(parser.usps_parsed() == (['USP 1 ', 'USP 2 ', 'USP 3 ', '\n\nUSP 4'], []))

	def test_whitespace_Two(self):
		parser.feed(whitespace1)
		self.assertTrue(parser.usps_parsed() == (['USP 1', 'USP 2', 'USP 3'], []))

	def test_whitespace_Three(self):
		parser.feed(whitespace2)
		# print(parser.usps_parsed())
		self.assertTrue(parser.usps_parsed() == (['USP 1', 'USP 2', 'USP 3', 'USP 4', 'USP 4\xa0'], []))

	def test_lonely_lowercases(self):
		parser.feed(single_word) # experts
		self.assertTrue(parser.usps_parsed() == (['Includes clear explanations of fundamentals for correct application', 'Contains key notes, experiences and implementation advice from experts', 'Covers relevant and current topics including Drug Metabolizing Enzymes and Transporters'], ['experts']))

class isNotUSPTests(unittest.TestCase):

	def test_empty_string(self):
		parser.feed(empty_str)		
		self.assertTrue(len(parser.output) is 0)
		self.assertTrue(len(parser.tags) is 0)
		self.assertTrue(parser.usps_parsed() == ([], []))

	def test_empty_null(self):
		parser.feed(str(empty_null))		
		self.assertTrue(len(parser.output) is 1)
		self.assertTrue(len(parser.tags) is 0)
		self.assertTrue(parser.usps_parsed() == (['None'], []))

def main():
    unittest.main()

if __name__ == '__main__':
    main()