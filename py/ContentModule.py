import os

class testclass:
	def test(self):
		f = open('C:\Users\Administrator.test\Desktop\wifi.bat','r')
		for line in f:
			'''
			if line != '':
				line.replace("start","stop")
				'''
			print line
	
class Generate_content_directory:
	contentList = null
	directoryList = null
	def __init__(self,contentPath,directoryPath):
		contentList = os.listdir(contentPath)
		directoryList = os.listdir(directoryPath)
		
	def GenerateContentStringList(contentList):
		for content in contentList:
			c = open(os.getcwd(content),'r')
				for line in c:
					if line.contain
	
tc = testclass();
tc.test()
files = os.listdir('C:\Users\Administrator.test\Desktop');
for fi in files:
	print fi