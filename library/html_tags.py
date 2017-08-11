# import re
from html_parser import uspHtmlParser

'''
filter out one bounded string, i.e. word
'''

# def not_this_word(word, column):

'''
ups regexs
'''

def tag_content(col):	
	parser = uspHtmlParser()
	parser.feed(col)
	return parser.output


	

