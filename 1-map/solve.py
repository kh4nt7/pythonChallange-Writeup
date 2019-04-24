#!/usr/bin/env python
string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
text = ""
diff = 0

for c in string:
	char = chr(ord(c)+2)
	if char=="{": char="a"
	if c==" ": char=c
	if c==".": char=c
	if c=="z": char="b"
	text += char

print text
