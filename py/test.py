import os

class readfile:
    def r(self):
        file = open('C:\\Users\\Administrator.test\\Desktop\\test.txt','r')
        boolean = False
        str = ''
        for f in file:
            if f == "drg\n":
                boolean = True
            if boolean:
                str += f
        print str
        file.close()

fi = readfile()
fi.r()