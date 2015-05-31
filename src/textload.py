#Text loading module

def loadtext(inFile):
	content = inFile.read()
	return content

#Result writing function. Used for testing
def writetext(content, outFile):
	for sentence in content:
		outFile.write(sentence)
		outFile.write('\n')
#Make a copy of the given text without commas. Used for testing
def loadwritetextNC(inFile):
	content = inFile.read()
	content = content.replace(",", "")
	outFile = open('testi/testoutNC.txt', 'w')
	outFile.write(content)
	outFile.close()

#Load the text and pass it on without commas. Used for testing
def loadtextNC(inFile):
	#read the file into "content"
	content = inFile.read()
	#remove commas from content
	content = content.replace(",", "")
	return content
