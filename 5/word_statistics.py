#coding=utf8

from collections import Counter
import re

with open('./file.test') as f:
	words = re.split('\W+', f.read())
	c = Counter(words))
	print(c)
	print(c.keys())
	print(c.items())
