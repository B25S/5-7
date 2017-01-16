class readfile:
	def __init__(self,filename):
		self.fn = filename
	def dosomething(fn):
		fw = open('..\Index.html','wb')

		f = open('..\'.append(fn),'r')
		for line in f:
			if line.find("article-content"):
				l = line.replace("article-content","content")
				print l
				fw.write(l)
			else:
				print "o_O!!!"
		f.close()
		fw.close()