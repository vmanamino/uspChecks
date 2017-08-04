import re

'''
filter out one bounded string, i.e. word
'''

# def not_this_word(word, column):

'''
ups regexs
'''

def tag_count(col):
	usps = 0
	p = re.compile(r'<p>|<div>|<br>')
	m = p.findall(str(col))
	if len(m): 
		if m[0] == '<br>': # == checks value, not object
			return len(m) + 1
		else:
			return len(m)
	else:
		return 0
	# return m
	

