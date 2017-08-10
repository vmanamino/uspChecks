import unittest
import re
import sys
sys.path.append('C:\\Code\\uspChecks\\library')
from regexs import tag_count


# target = 3

pTag_target = """<p>USP 1 </p><p>USP2
 		</p><p>USP-3</p>"""

# two spaces between each USP
tag_none = """USP 1  
			USP2  
			USP-3"""

pTag_one_less = """<p>USP 1 </p><p>USP2	</p>"""

pTag_one_more = """<p>USP 1 </p><p>USP2
 		</p><p>USP-3</p><p>USP 4</p>"""

divTag_target = """<div>USP 1 </div><div>USP2
 		</div><div>USP-3</div>"""

divTag_one_less = """<div>USP 1 </div><div>USP2</div>"""

divTag_one_more = """<div>USP 1 </div><div>USP2
 		</div><div>USP-3</div><div>USP 4</p>"""

'''
div tag for usp, but also containing nothing, and wrapping other html tag (<br>)
which in other cases, is also used for usp
'''

divTag_wrap_target = """<div>USP 1</div><div><br></div><div>USP 2</div><div><br></div>
		<div>USP 2</div><div><br></div><div>USP-3</div>""" # currently my script interprets this as 10 USPs

brTag_target = """USP 1<br>USP II<br>USP-3"""

brTag_one_less = """USP 1<br>USP II"""

brTag_one_more = """USP 1<br>USP II<br>USP-3<br>USP 4"""

# br tag in XHTML is different <br/>, need test cases




liTag_divWrapped_target = """<div><ul><li>USP 1</li><li>USP 2</li><li>USP-3</li></ul></div>"""

class isTagTests(unittest.TestCase):	
	
	def test_vanilla_One(self):
		self.assertTrue(tag_count(pTag_target) is 3)
		self.assertTrue(tag_count(divTag_target) is 3)
		self.assertTrue(tag_count(brTag_target) is 3)

	def test_vanilla_Two(self):
		self.assertFalse(tag_count(pTag_one_less) is 3)
		self.assertFalse(tag_count(divTag_one_less) is 3)
		self.assertFalse(tag_count(brTag_one_less) is 3)

	def test_vanilla_Three(self):
		self.assertFalse(tag_count(pTag_one_more) is 3)
		self.assertFalse(tag_count(divTag_one_more) is 3)
		self.assertFalse(tag_count(brTag_one_more) is 3)

	def test_vanilla_Four(self):
		self.assertFalse(tag_count(pTag_target) is not 3)
		self.assertFalse(tag_count(divTag_target) is not 3)
		self.assertFalse(tag_count(brTag_target) is not 3)


def main():
    unittest.main()

if __name__ == '__main__':
    main()