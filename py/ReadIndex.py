fw = open('..\Index_gai.html','wb')

f = open('..\Index.html','r')
for line in f:
	if line.find("article-content"):
		l = line.replace("article-content","content")
		print l
		fw.write(l)
	else:
		print "o_O!!!"
f.close()
fw.close()

