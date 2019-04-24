#!/usr/bin/env python

raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
text = ""

for c in raw:
	if c >= "a" and c <= "z":
		text += chr((ord(c)+2 - ord("a")) % 26 + ord("a"))
	else:
		text += c

print text
