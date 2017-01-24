import sys, os

foldPath = sys.argv[1]
files = os.listdir(foldPath)
savePath = sys.argv[2]
save_file_name = sys.argv[3]
default_file_name = "Navigator_content.json"
if save_file_name == "":
    json = open(savePath+os.path.sep+default_file_name,"w")
else:
    json = open(savePath+os.path.sep+save_file_name,"w")
string = "[\n\t"
index = 1
for f in files:
    if (len(f.split('.')) == 1):
        string += '{' + str(index) + ':\"'+f+'\"},\n\t'
        index+=1
string = string[0:len(string)-3]
string += "\n]"
json.write(string)
json.flush()
json.close()
