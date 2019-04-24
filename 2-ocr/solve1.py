#!/usr/bin/env python
import re
from urllib2 import *

html = urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()

data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]

print "".join(re.findall("[A-Za-z]", data))
