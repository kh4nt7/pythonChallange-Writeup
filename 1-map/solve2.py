#!/usr/bin/env python
from string import maketrans
import string

raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
code = ""
alphabet = string.ascii_lowercase

for c in alphabet:
	code += chr((ord(c)+2 - ord("a"))%26+ord("a"))

table = string.maketrans(alphabet, code)

print raw.translate(table)
print
print "Next Level: {}".format("map".translate(table))
