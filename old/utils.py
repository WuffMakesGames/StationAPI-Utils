import os

def writefile(filename, s):
	file = open(filename, "w")
	file.write(s)
	file.close()

def removefile(filename):
	os.remove(filename)
