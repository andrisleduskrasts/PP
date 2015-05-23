# "Pieturzīmju palīgs" development version. Author: Andris Leduskrasts
# Program is split into modules - Text loading, text splitting and grammar modules. The list of laws is connected to the grammar module.

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
	content = inFile.read()
	content = content.replace(",", "")
	return content
#Text splitting module
def textsplitter(content):
	import re

	sentences = re.findall('.*?[A-Za-z0-9āčēģīķļņšūž][.!?][][!""''()*+,.;<=>?@\^_{|}~-]*?\s?|.*?[.?!]+[^.]|.*?[.?!]+$|.*?$', content)
	#The current regex also splits situations like "tas utt. ļāva un 1997. gadā"
	for counter, sentence in enumerate(sentences):
		if re.match('[a-zāčēģīķļņšūž].*|[.]', sentence) and re.match('[a-zāčēģīķļņšūž].*|[.]', sentences[counter+1]):
			if counter != 0:
				sentences[counter-1] = sentences[counter-1]+sentence
				sentences[counter-1] = sentences[counter-1]+sentences[counter+1]
				sentences.pop(counter+1)
				sentences.pop(counter)
		elif re.match('[a-zāčēģīķļņšūž].*|[.]', sentence):
			if counter!=0:
				senteces[counter-1] = sentences[counter-1] + sentence
				sentences.pop(counter)
	#If a non-first sentence starts with lower letter, add it to the previous sentence and pop it out of the list
	return sentences


#Grammar module - sentence checker and law function calls
def grammarCheck(sentences):
	import re
	for sentencecounter, sentence in enumerate(sentences):
		wordlist = sentence.split()
		#split sentence into words
		for counter, word in enumerate(wordlist):
			#check if current word calls anything from the grammar law list
			if re.match('ka[,]?$', word):
				wordlist = ka(wordlist, counter)
			if re.match('ja[,]?$', word):
				wordlist = ja(wordlist, counter)
			if re.match('[pP]iemēram[,.?!]?$', word):
				wordlist = piemeram(wordlist, counter)
			if re.match('bet[.,?!]?$', word):
				wordlist = bet(wordlist, counter)
			if re.match('[pP]rotams[.,?!]?$', word):
				wordlist = protams(wordlist, counter)
			if re.match('[jJ]ā[.,?!]?$', word):
				wordlist = jaa(wordlist, counter)
			if re.match('[nN]ē[.,?!]?$', word):
				wordlist = nee(wordlist, counter)
			if re.match('Iespējams$', word):
				wordlist = iespejams(wordlist, counter)
			if re.match('[Gg]an[,.?!]?$', word):
				wordlist = gan(wordlist, counter)
			if re.match('kur[,.?!]?$', word):
				wordlist = kur(wordlist, counter)
			if re.match('lai[,.?!]?$', word):
				wordlist = lai(wordlist, counter)
			if re.match('jo[,.?!]?$|jo[.][.][.]', word):
				wordlist = jo(wordlist, counter)


		#result is changed back into sentence for later return
		sentences[sentencecounter] = " ".join(word for word in wordlist)
	return sentences

#Laws of grammar module
#"ka" function - first it is tested if there's not a punctuation mark previously, else the grammar law is applied
def ka(wordlist, number):
	import re
	if re.match('.*[,;:-]', wordlist[number-1]):
		return wordlist
	else:
		counter = 0
		while counter < number:
			if re.match('[Kk]a[,-]?$', wordlist[counter]):
				temp = counter +1
				while temp < number:
					if re.match('un[,-]*?|vai[,-]?$|bet[,-]?$', wordlist[temp]):
						return wordlist
					temp = temp+1
			counter = counter+1
		wordlist[number-1] = wordlist[number-1] + ','
		return wordlist
#"ja" function
def ja(wordlist, number):
	import re
	if re.match('.*[,:;-]', wordlist[number-1]):
		return wordlist
	else:
		counter = 0
		while counter < number:
			if re.match('[jJ]a[,-]?$', wordlist[counter]):
				temp = counter +1
				while temp < number:
					if re.match('un[,-]?$|vai[,-]?$|bet[,-]?$', wordlist[temp]):
						return wordlist
					temp = temp+1
			counter = counter+1
		wordlist[number-1] = wordlist[number-1] + ','
		return wordlist
#"piemēram" function
def piemeram(wordlist, number):
	import re
	if re.match('.*[(,;:-]', wordlist[number-1]) or number == 0:
		if re.match('[pP]iemēram[,.;:]|[pP]iemēram[.][.][.]', wordlist[number]):
			return wordlist
		elif re.match('-', wordlist[number+1]):
			return wordlist
		else:
			wordlist[number] = wordlist[number] + ','
			return wordlist
	else:
		wordlist[number-1] = wordlist[number-1] + ','
		if re.match('[pP]iemēram[,.;:]|[pP]iemēram[.][.][.]', wordlist[number]):
			return wordlist
		elif re.match('-', wordlist[number+1]):
			return wordlist
		else:
			wordlist[number] = wordlist[number] + ','
			return wordlist
#"bet" function
def bet(wordlist, number):
	import re
	if number == 0 or re.match('.*[(,;:-]', wordlist[number-1]):
		return wordlist
	else:
		wordlist[number-1] = wordlist[number-1] + ','
		return wordlist
#"protams" function
def protams(wordlist, number):
	import re
	if re.match('.*[(,;:-]', wordlist[number-1]) or number == 0:
		if re.match('[pP]rotams[,.;:]|[pP]rotams[.][.][.]', wordlist[number]):
			return wordlist
		elif re.match('-', wordlist[number+1]):
			return wordlist
		else:
			wordlist[number] = wordlist[number] + ','
			return wordlist
	else:
		wordlist[number-1] = wordlist[number-1] + ','
		if re.match('[pP]rotams[,.;:]|[pP]rotams[.][.][.]', wordlist[number]):
			return wordlist
		elif re.match('-', wordlist[number+1]):
			return wordlist
		else:
			wordlist[number] = wordlist[number] + ','
			return wordlist
#"jā" function
def jaa(wordlist, number):
	import re
	if re.match('.*[(,;:-]|[""]?[nN]u,?$|[""]?[uU]n$|[""]?[vV]ai$|[""]?[kK]a$|[""]?[jJ]o$|[""]?[bB]et$|[""]?[vV]arbūt$|[""]?[gG]an$|[""]?[tT]ad$|[""]?[kK]ur$|[Kk]uram[,.]?$|[Kk]uriem[,.]?$|[Kk]uru[,.]?$|[Kk]urām[,.]?$|[Kk]urā[,.]?$', wordlist[number-1]) or number == 0:
		if re.match('nu$', wordlist[number-1]):
			if re.match('nu,$', wordlist[number-1]):
				wordlist[number-1] = wordlist[number-1]
			else:
				if number > 1:
					if re.match('.*[,:;]', wordlist[number-2]):
						wordlist[number-2] = wordlist[number-2]
					else:
						wordlist[number-2] = wordlist[number-2] + ','
		if re.match('[jJ]ā[,.;:]|[jJ]ā[.][.][.]', wordlist[number]):
			return wordlist
		elif re.match('-$', wordlist[number+1]):
			return wordlist
		elif re.match('[uU]n$|[vV]ai$', wordlist[number+1]):
			return wordlist
		elif re.match('[gG]an', wordlist[number+1]):
			if re.match('[gG]an[-,.!?:;""'']|[gG]an[.][.][.]', wordlist[number+1]):
				return wordlist
			elif re.match('-', wordlist[number+2]):
				return wordlist
			elif re.match('[""]?[gG]an$', wordlist[number-1]) or re.match('[""]?[gG]an$', wordlist[number-2]):
				wordlist[number] = wordlist[number] + ','
				return wordlist
			else:
				wordlist[number+1] = wordlist[number+1] + ','
				return wordlist
		else:
			wordlist[number] = wordlist[number] + ','
			return wordlist
	else:
		if re.match('.*,', wordlist[number-2]) and re.match('nu$', wordlist[number-1]):
			wordlist[number-1] = wordlist[number-1]
		else:
			wordlist[number-1] = wordlist[number-1] + ','
		if re.match('[jJ]ā[,.;:]', wordlist[number]):
			return wordlist
		elif re.match('-', wordlist[number+1]):
			return wordlist
		elif re.match('[uU]n$|[vV]ai$', wordlist[number+1]):
			return wordlist
		elif re.match('[gG]an', wordlist[number+1]):
			if re.match('[gG]an[-,.!?""'']|[gG]an[.][.][.]', wordlist[number+1]):
				return wordlist
			elif re.match('-', wordlist[number+2]):
				return wordlist
			elif re.match('[""]?[gG]an$', wordlist[number-1]) or re.match('[""]?[gG]an$', wordlist[number-2]):
				wordlist[number] = wordlist[number] + ','
				return wordlist
			else:
				wordlist[number+1] = wordlist[number+1] + ','
				return wordlist
		else:
			wordlist[number] = wordlist[number] + ','
			return wordlist
#"nē" function
def nee(wordlist, number):
	import re
	if re.match('.*[(,;:-]|[""]?[nN]u,?$|[""]?[uU]n$|[""]?[vV]ai$|[""]?[kK]a$|[""]?[jJ]o$|[""]?[bB]et$|[""]?[vV]arbūt$|[""]?[gG]an$|[""]?[tT]ad$|[""]?[kK]ur$|[Kk]uram[,.]?$|[Kk]uriem[,.]?$|[Kk]uru[,.]?$|[Kk]urām[,.]?$|[Kk]urā[,.]?$', wordlist[number-1]) or number == 0:
		if re.match('nu$', wordlist[number-1]):
			if re.match('nu,$', wordlist[number-1]):
				wordlist[number-1] = wordlist[number-1]
			else:
				if number > 1:
					if re.match('.*[,:;]', wordlist[number-2]):
						wordlist[number-2] = wordlist[number-2]
					else:
						wordlist[number-2] = wordlist[number-2] + ','
		if re.match('[nN]ē[,.;:]|[nN]ē[.][.][.]', wordlist[number]):
			return wordlist
		elif re.match('-$', wordlist[number+1]):
			return wordlist
		elif re.match('[uU]n$|[vV]ai$', wordlist[number+1]):
			return wordlist
		else:
			wordlist[number] = wordlist[number] + ','
			return wordlist
	else:
		if re.match('.*,', wordlist[number-2]) and re.match('nu$', wordlist[number-1]):
			wordlist[number-1] = wordlist[number-1]
		else:
			wordlist[number-1] = wordlist[number-1] + ','
		if re.match('[nN]ē[,.;:]', wordlist[number]):
			return wordlist
		elif re.match('-', wordlist[number+1]):
			return wordlist
		elif re.match('[uU]n$|[vV]ai$', wordlist[number+1]):
			return wordlist
		else:
			wordlist[number] = wordlist[number] + ','
			return wordlist
#"iespējams" function
def iespejams(wordlist, number):
	import re
	if number == 0:
		if re.match('.*t[,.!?:;]?$|.*ties[,.!?:;]?$|-$', wordlist[number+1]) or re.match('.*t[,.!?:;]?$|.*ties[,.!?:;]?$', wordlist[number+2]):
			return wordlist
		else:
			wordlist[number] = wordlist[number] + ','
			return wordlist
	else:
		return wordlist
#"gan" function
def gan(wordlist, number):
	import re
	if number == 0:
		return wordlist
	counter = number-4
	if counter < 0:
		counter = 0
	if re.match('.*[,-]$', wordlist[number-1]):
		return wordlist
	else:
		while counter < number-1:
			if re.match('[gG]an[,]?', wordlist[counter]):
				wordlist[number-1] = wordlist[number-1] + ','
				return wordlist
			counter = counter+1
	return wordlist
#"kur" function
def kur(wordlist, number):
	import re
	if number == 0:
		return wordlist
	if re.match('.*[,;:-]$', wordlist[number-1]):
		return wordlist
	else:
		counter = 0
		while counter < number:
			if re.match('[Kk]ur[,-]?$', wordlist[counter]):
				temp = counter +1
				while temp < number:
					if re.match('un[,-]?$|vai[,-]?$|bet[,-]?$', wordlist[temp]):
						return wordlist
					temp = temp+1
			counter = counter+1
		if re.match('[Uu]n[,-]?$|[Vv]ai[,-]?$|[Bb]et[,-]?$', wordlist[number-1]):
			return wordlist
		wordlist[number-1] = wordlist[number-1] + ','
		return wordlist
#"lai" function
def lai(wordlist, number):
	#regex method import
	import re
	#checking of punctuation in the previous word
	if re.match('.*[,;:-]', wordlist[number-1]):
		return wordlist
	else:
		counter = 0
		testword = 0
		#"lai arī", "un" and "lai" interaction 
		while counter < number:
			if re.match('[Ll]ai[,-]?$', wordlist[counter]):
				temp = counter +1
				if re.match('[Aa]rī[,:-]?$', wordlist[temp]):
					testword = temp
					counter = counter+1
				else:
					while temp < number:
						if re.match('un[,-]*?$|vai[,-]?$|bet[,-]?$', wordlist[temp]):
							return wordlist
						temp = temp+1
			counter = counter+1
		if re.match('[aA]rī[,:-]?$', wordlist[number+1]) and testword > 0:
			return wordlist
		else:
			#The added exception with question words, can only happen if the position of "lai" is not at the start
			if number > 0:
				if re.match('[kK]āpēc|[kK]o$|[kK]ā$|[kK]ur$|[kK]am$', wordlist[number-1]):
					return wordlist
				elif re.match('[kK]āpēc|[kK]o$|[kK]ā$|[kK]ur$|[kK]am$', wordlist[number-2]):
					return wordlist
			#no exceptions have been met, add the punctuation mark and return the sentence
			wordlist[number-1] = wordlist[number-1] + ','
			return wordlist
#"jo" function
def jo(wordlist, number):
	import re
	if number == 0 or re.match('.*[(,;:-]', wordlist[number-1]):
		return wordlist
	else:
		if re.match('[uU]n$', wordlist[number-1]):
			return wordlist
		elif re.match('[vV]ēl$', wordlist[number-1]) and re.match('.*āk[s]?[,.!?:;-]?', wordlist[number+1]):
			return wordlist
		else:
			wordlist[number-1] = wordlist[number-1] + ','
			return wordlist

#Interface module
#specify the input file
inFile = open('testi/testjo.txt', 'r')
data = loadtext(inFile)
inFile.close()
#Split data into sentences using the sentences textsplitter() function
sentences = textsplitter(data)

#specify the output file
outFile = open('testi/testout.txt', 'w')
result = grammarCheck(sentences)
writetext(result, outFile)
outFile.close()
#for writing a copy of the file without commas:
#loadwritetextNC()

#for loading the text without commas:
#data = loadtextNC()

#for checking sentence splitting:
#sentences = textsplitter(data)
#sentenceTest = open('testi/sentences.txt', 'w')
#for sentence in sentences:
#	sentenceTest.write(sentence)
#	sentenceTest.write('\n')
#sentenceTest.close()
#writetext(data, file)
