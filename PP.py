# "Pieturzīmju palīgs" development version. Author: Andris Leduskrasts
# Program is split into modules - Text loading, text splitting and grammar modules. The list of laws is connected to the grammar module.

#Text loading module
import re
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

#Text splitting module
def textsplitter(content):
	sentences = re.findall('.*?[A-Za-z0-9āčēģīķļņšūž][.!?][][!""''()*+,.;<=>?@\^_{|}~-]*?\s?|.*?[.?!]+[^.]|.*?[.?!]+$|.*?$', content)
	#The current regex also splits situations like "tas utt. ļāva un 1997. gadā"
	counter = 0
	while counter + 1 < len(sentences):
		if re.match('[a-zāčēģīķļņšūž].*|[.?!]', sentences[counter]):
			if counter != 0:
				sentences[counter-1] = sentences[counter-1] + sentences[counter]
				sentences.pop(counter)
				counter = counter - 1
		counter = counter + 1
	#If a non-first sentence starts with lower letter, add it to the previous sentence and pop it out of the list
	return sentences


#Grammar module - sentence checker and law function calls
def grammarCheck(sentences):
	for sentencecounter, sentence in enumerate(sentences):
		wordlist = sentence.split()
		#split sentence into words
		for counter, word in enumerate(wordlist):
			#check if current word calls anything from the grammar law list
			if re.match('ka[,]?$|ka[.][.][.]', word):
				wordlist = ka(wordlist, counter)
			if re.match('ja[,]?$|ja[.][.][.]', word):
				wordlist = ja(wordlist, counter)
			if re.match('[(]?[pP]iemēram[,.?!]?$|piemēram[.][.][.]', word):
				wordlist = piemeram(wordlist, counter)
			if re.match('bet[.,?!]?$|bet[.][.][.]', word):
				wordlist = bet(wordlist, counter)
			if re.match('[(]?[pP]rotams[.,?!]?$|protams[.][.][.]', word):
				wordlist = protams(wordlist, counter)
			if re.match('[(]?[jJ]ā[.,?!]?$|jā[.][.][.]', word):
				wordlist = jaa(wordlist, counter)
			if re.match('[(]?[nN]ē[.,?!]?$|nē[.][.][.]', word):
				wordlist = nee(wordlist, counter)
			if re.match('[(]?Iespējams$', word):
				wordlist = iespejams(wordlist, counter)
			if re.match('gan[,.?!]?$|gan[.][.][.]', word):
				wordlist = gan(wordlist, counter)
			if re.match('kur[,.?!]?$|lai[.][.][.]', word):
				wordlist = kur(wordlist, counter)
			if re.match('lai[,.?!]?$|lai[.][.][.]', word):
				wordlist = lai(wordlist, counter)
			if re.match('jo[,.?!]?$|jo[.][.][.]', word):
				wordlist = jo(wordlist, counter)
			if re.match('kad[,.?!]?$|kad[.][.][.]', word):
				wordlist = kad(wordlist, counter)
			if re.match('tostarp[,.?]?$|tostarp[.][.][.]', word):
				wordlist = tostarp(wordlist, counter)
			if re.match('[(][Šš]ķiet$', word):
				wordlist = skiet(wordlist, counter)
			if re.match('ne[,.?!]?$|ne[.][.][.]', word):
				wordlist = ne(wordlist, counter)
			if re.match('kaut$', word):
				if len(wordlist)>counter + 1:
					if re.match('[Gg]an[,.:;!?]?$|gan[.][.][.]', wordlist[counter+1]):
						wordlist = kautgan(wordlist, counter)
					elif re.match('[Aa]rī[,.:;!?]?$|gan[.][.][.]', wordlist[counter+1]):
						wordlist = kautari(wordlist, counter)
			if re.match('kāpēc[,.:;!?]?$|kāpēc[.][.][.]', word):
				wordlist = kapec(wordlist, counter)
			if re.match('cik[,.:?!?]?$|cik[.][.][.]', word):
				wordlist = cik(wordlist, counter)
			if re.match('kā$', word):
				if len(wordlist) > counter + 1:
					if re.match('arī[,.!?]?$|arī[.][.][.]', wordlist[counter+1]):
						wordlist = kaaarii(wordlist, counter)
			if re.match('[(]?[Pp]roti[,:;""'']?[.]?[.]?$', word):
				wordlist = proti(wordlist, counter)
			if re.match('tad[.,:;""'']?[.]?[.]?$', word):
				wordlist = tad(wordlist, counter)
			if re.match('ko[.,:;""'']?[.]?[.]?$', word):
				wordlist = ko(wordlist, counter)
			if re.match('nevis[.,:;"'']?[.]?[.]?$', word):
				wordlist = nevis(wordlist, counter)
			if re.match('[rR]espektīvi[.,:;"'']?[.]?[.]?$', word):
				wordlist = respektivi(wordlist, counter)
		#result is changed back into sentence for later return
		sentences[sentencecounter] = " ".join(word for word in wordlist)
	return sentences

#Laws of grammar module
#"ka" function - first it is tested if there's not a punctuation mark previously, else the grammar law is applied
def ka(wordlist, number):
	#check previous punctuation and if its at the start of the sentence
	if not number == 0:
		if re.match('.*[,;:-]', wordlist[number-1]):
			return wordlist
		#add exceptions here
		else:
			counter = 0
			while counter < number:
				#check equal subclauses
				if re.match('[Kk]a[,-]?$', wordlist[counter]):
					temp = counter +1
					while temp < number:
						if re.match('un[,-]*?|vai[,-]?$|bet[,-]?$', wordlist[temp]):
							return wordlist
						temp = temp+1
				counter = counter+1
			wordlist[number-1] = wordlist[number-1] + ','
			return wordlist
	else:
		return wordlist
#"ja" function
def ja(wordlist, number):
	#check punctuation and position
	if not number == 0:
		if re.match('.*[,:;-—]', wordlist[number-1]):
			return wordlist
		else:
			counter = 0
			#check equal subclauses
			while counter < number:
				if re.match('[jJ]a[,-—]?$', wordlist[counter]):
					temp = counter +1
					while temp < number:
						if re.match('un[,-—]?$|vai[,—-]?$|bet[,—-]?$', wordlist[temp]):
							return wordlist
						temp = temp+1
				counter = counter+1
			wordlist[number-1] = wordlist[number-1] + ','
			return wordlist
	#add exceptions here
	else:
		return wordlist
#"piemēram" function
def piemeram(wordlist, number):
	#check position and punctuation
	if not number == 0:
		#add exceptions here
		if re.match('.*[(,;:—-]', wordlist[number-1]):
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
	else:
		return wordlist
#"bet" function
def bet(wordlist, number):
	#check if its the first word
	if number == 0:
		return wordlist
	#check previous punctuation
	if re.match('.*[(,;:-—]', wordlist[number-1]):
		return wordlist
	#add exceptions here
	else:
		wordlist[number-1] = wordlist[number-1] + ','
		return wordlist
#"protams" function
def protams(wordlist, number):
	#check previous punctuation
	#add exceptions here
	if re.match('.*[(,;:-—]', wordlist[number-1]) or number == 0:
		#check after-word punctuation
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
	#add exceptions here
	#check punctuation and exception words
	if re.match('.*[(,;:-—]|[""]?[nN]u,?$|[aA]rī$|[""]?[uU]n$|[""]?[vV]ai$|[""]?[kK]a$|[""]?[jJ]o$|[""]?[bB]et$|[""]?[vV]arbūt$|[""]?[gG]an$|[""]?[tT]ad$|[""]?[kK]ur$|[Kk]uram[,.]?$|[Kk]uriem[,.]?$|[Kk]uru[,.]?$|[Kk]urām[,.]?$|[Kk]urā[,.]?$|[kK]ad[,.]?$|[jJ]au[,.]?$', wordlist[number-1]) or number == 0:
		if len(wordlist) == 1:
			return wordlist
		if number > 0:
			#check the "nu jā" word structure
			if re.match('nu$', wordlist[number-1]):
				if re.match('nu,$', wordlist[number-1]):
					wordlist[number-1] = wordlist[number-1]
				else:
					if number > 1:
						if re.match('.*[,:;—]', wordlist[number-2]):
							wordlist[number-2] = wordlist[number-2]
						else:
							wordlist[number-2] = wordlist[number-2] + ','
		#check punctuation after the word
		if re.match('[(][jJ]ā[,.;:]|[jJ]ā[.][.][.]', wordlist[number]):
			return wordlist
		#check for exceptions after the word
		if len(wordlist) > number + 1:
			if re.match('-$', wordlist[number+1]):
				return wordlist
			if re.match('[uU]n$|[vV]ai$', wordlist[number+1]):
				return wordlist
			elif re.match('[gG]an', wordlist[number+1]):
				if re.match('[gG]an[—-,.!?""'']', wordlist[number+1]):
					return wordlist
				elif len(wordlist) > number + 2:
					if re.match('-—', wordlist[number+2]):
						return wordlist
				if number > 0:
					if re.match('[""]?[gG]an$', wordlist[number-1]):
						wordlist[number] = wordlist[number] + ','
						return wordlist
				if number > 1:
					if re.match('[""]?[gG]an$', wordlist[number-2]):
						wordlist[number] = wordlist[number] + ','
						return wordlist
				wordlist[number+1] = wordlist[number+1] + ','
				return wordlist
			wordlist[number] = wordlist[number] + ','
			return wordlist
		else:
			return wordlist
	#similar to previous checkings, only in case of adding the start punctuation marks
	else:
		if re.match('.*,', wordlist[number-2]) and re.match('nu$', wordlist[number-1]):
			wordlist[number-1] = wordlist[number-1]
		else:
			if not re.match('(', wordlist[number]):
				wordlist[number-1] = wordlist[number-1] + ','
		if re.match('[(][jJ]ā[,.;:]', wordlist[number]):
			return wordlist
		if len(wordlist) > number + 1:
			if re.match('[-—]', wordlist[number+1]):
				return wordlist
			if re.match('[uU]n$|[vV]ai$', wordlist[number+1]):
				return wordlist
			elif re.match('[gG]an', wordlist[number+1]):
				if re.match('[gG]an[-—,.!?""'']', wordlist[number+1]):
					return wordlist
				elif len(wordlist) > number + 2:
					if re.match('-', wordlist[number+2]):
						return wordlist
				if number > 0:
					if re.match('[""]?[gG]an$', wordlist[number-1]):
						wordlist[number] = wordlist[number] + ','
						return wordlist
				if number > 1:
					if re.match('[""]?[gG]an$', wordlist[number-2]):
						wordlist[number] = wordlist[number] + ','
						return wordlist
				wordlist[number+1] = wordlist[number+1] + ','
				return wordlist
			wordlist[number] = wordlist[number] + ','
			return wordlist
		return wordlist
#"nē" function
def nee(wordlist, number):
	#check all the exception words and punctuation for previous word punctuation usage
	#add exceptions here
	if re.match('.*[(,;:-—]|[""]?[nN]u,?$|[""]?[uU]n$|[""]?[vV]ai$|[""]?[kK]a$|[""]?[jJ]o$|[""]?[bB]et$|[""]?[vV]arbūt$|[""]?[gG]an$|[""]?[tT]ad$|[""]?[kK]ur$|[Kk]uram[,.]?$|[Kk]uriem[,.]?$|[Kk]uru[,.]?$|[Kk]urām[,.]?$|[Kk]urā[,.]?$|[kK]ad[,.]?$|[aA]rī[,.]?$|[jJ]au[,.]?$', wordlist[number-1]) or number == 0:
		if len(wordlist) == 1:
			return wordlist
		if number > 0:
			if re.match('nu$', wordlist[number-1]):
				if re.match('nu,$', wordlist[number-1]):
					wordlist[number-1] = wordlist[number-1]
				else:
					if number > 1:
						if re.match('.*[,:;]', wordlist[number-2]):
							wordlist[number-2] = wordlist[number-2]
						else:
							wordlist[number-2] = wordlist[number-2] + ','
		if re.match('[(]?[nN]ē[,.;:]|[(]?[nN]ē[.][.][.]', wordlist[number]):
			return wordlist
		if len(wordlist) > number + 1:
			#check if there are after-word exceptions "un" , "vai"
			if re.match('[-—]$', wordlist[number+1]):
				return wordlist
			elif re.match('[uU]n$|[vV]ai$', wordlist[number+1]):
				return wordlist
			else:
				wordlist[number] = wordlist[number] + ','
				return wordlist
		return wordlist
	else:
		if number > 0:
			#add the comma
			if not re.match('.*[,.;:]', wordlist[number-1]) and not re.match('(', wordlist[number]):
				wordlist[number-1] = wordlist[number-1] + ','
		#check punctuation and exception words that are after the word.
		if re.match('[(]?[nN]ē[,.;:]', wordlist[number]):
			return wordlist
		if len(wordlist) > number + 1:
			if re.match('[-—]', wordlist[number+1]):
				return wordlist
			elif re.match('[uU]n$|[vV]ai$', wordlist[number+1]):
				return wordlist
			else:
				wordlist[number] = wordlist[number] + ','
				return wordlist
		return wordlist
#"iespējams" function
def iespejams(wordlist, number):
	if number == 0:
		#check if there are -t or -ties words locally
		if len(wordlist) > 1:
			if re.match('.*t[,.!?:;]?$|.*ties[,.!?:;]?$|[-—]$', wordlist[number+1]):
				return wordlist
		if len(wordlist)>2:
			if re.match('.*t[,.!?:;]?$|.*ties[,.!?:;]?$', wordlist[number+2]):
				return wordlist
		#add exceptions here
		wordlist[number] = wordlist[number] + ','
		return wordlist
	else:
		return wordlist
#"gan" function
def gan(wordlist, number):
	if number == 0:
		return wordlist
	counter = 0
	temp = 0
	#check "kaut gan" and punctuation
	if re.match('.*[,:-—]$|[kK]aut$', wordlist[number-1]):
		return wordlist
	else:
		#add exceptions here
		#check if another gan exists, that isn't combined with "gan"
		while counter < number-1:
			if re.match('[gG]an[,]?$', wordlist[counter]):
				if counter > 0:
					if re.match('[kK]aut$', wordlist[counter-1]):
						temp = counter
				if temp < 1:
					wordlist[number-1] = wordlist[number-1] + ','
					return wordlist
			counter = counter+1
		return wordlist
#"kur" function
def kur(wordlist, number):
	if number == 0:
		return wordlist
	#check punctuation and exception words
	if re.match('.*[,;:—-]$', wordlist[number-1]):
		return wordlist
	#check "kaut kur" and "diez kur", the words are checked for both registers for testing purposes
	if re.match('[kK][Aa][Uu][Tt]$|[dD][iI][eE][zZ]$', wordlist[number-1]):
		return wordlist
	else:
		counter = 0
		#check equal subclause possibilities
		while counter < number:
			if re.match('[Kk]ur[,-—]?$', wordlist[counter]):
				temp = counter +1
				while temp < number:
					if re.match('un[,-—]?$|vai[,-—]?$|bet[,-—]?$', wordlist[temp]):
						return wordlist
					temp = temp+1
			counter = counter+1
		#check other exception words
		if re.match('[Uu]n[,—-]?$|[Vv]ai[,-—]?$|[Bb]et[,—-]?$', wordlist[number-1]):
			return wordlist
		wordlist[number-1] = wordlist[number-1] + ','
		return wordlist
#"lai" function
def lai(wordlist, number):
	#regex method import
	#checking of punctuation in the previous word
	if len(wordlist) < number + 1:
		return wordlist
	if re.match('.*[,;:—-]', wordlist[number-1]):
		return wordlist
	else:
		counter = 0
		testword1 = 0
		testword2 = 0
		#"lai arī", "un" and "lai" interaction 
		if len(wordlist) == number + 1:
			return wordlist
		while counter < number:
			if re.match('[Ll]ai[,-—]?$', wordlist[counter]):
				temp = counter +1
				if re.match('[Aa]rī[,:-—]?$', wordlist[temp]):
					testword1 = temp
					counter = counter+1
				elif re.match('[gG]an[,:—-]?$', wordlist[temp]):
					testword2 = temp
				else:
					while temp < number:
						if re.match('un[,—-]*?$|vai[,-—]?$|bet[,—-]?$', wordlist[temp]):
							return wordlist
						temp = temp+1
			counter = counter+1
		if re.match('[aA]rī[,:—-]?$', wordlist[number+1]) and testword1 > 0:
			return wordlist
		if re.match('[gG]an[,:-—]?$', wordlist[number+1]) and testword2 > 0:
			return wordlist
		else:
			#The added exception with question words, can only happen if the position of "lai" is not at the start
			if number > 0:
				if re.match('[kK]āpēc|[kK]o$|[kK]ā$|[kK]ur$|[kK]am$|[kK]ad$', wordlist[number-1]):
					return wordlist
				elif re.match('[kK]āpēc|[kK]o$|[kK]ā$|[kK]ur$|[kK]am$|[kK]ad$', wordlist[number-2]):
					return wordlist
			#add more exceptions here
			#no exceptions have been met, add the punctuation mark and return the sentence
			wordlist[number-1] = wordlist[number-1] + ','
			return wordlist
#"jo" function
def jo(wordlist, number):
	if number == 0 or re.match('.*[(,;:-—]', wordlist[number-1]):
		return wordlist
	else:
		#check the exception words
		if len(wordlist)>number + 1:
			if re.match('[uU]n$', wordlist[number-1]):
				return wordlist
				#check the "vēl jo -āks" word structure
			elif re.match('[vV]ēl$', wordlist[number-1]) and re.match('.*āk[s]?[,.!?:;—-]?', wordlist[number+1]):
				return wordlist
			#add exceptions here
			else:
				wordlist[number-1] = wordlist[number-1] + ','
				return wordlist
		else:
			return wordlist
#"kad" function
def kad(wordlist, number):
	if number == 0:
		return wordlist
	#check previous token for exceptions and punctuation
	if re.match('.*[,;:—-]$', wordlist[number-1]):
		return wordlist
	if re.match('[kK][Aa][Uu][Tt]$', wordlist[number-1]):
		return wordlist
	else:
		counter = 0
		#check for equal subclauses
		while counter < number:
			if re.match('[Kk]ad[,—-]?$|[kK]āpēc[,]?$|[kK]o$[,]?$|[kK]ā$[,]?$|[kK]ur$[,]?$|[kK]am$[,]?$', wordlist[counter]):
				temp = counter +1
				while temp < number:
					if re.match('un[,-—]?$|vai[,-—]?$|bet[,-—]?$', wordlist[temp]):
						return wordlist
					temp = temp+1
			counter = counter+1
		if number == 1 and re.match('Un|Bet', wordlist[number-1]):
			return wordlist
		#add exceptions here
		wordlist[number-1] = wordlist[number-1] + ','
		return wordlist
#"tostarp" function
def tostarp(wordlist, number):
	#check both punctuation and exception words
	if number == 0 or re.match('.*[(,;:-—]|[Uu]n[,—-]?$|[Vv]ai[,-—]?$|[Bb]et[,—-]?$', wordlist[number-1]):
		return wordlist
	#add exceptions here
	else:
		wordlist[number-1] = wordlist[number-1] + ','
		return wordlist
#"šķiet" function
def skiet(wordlist, number):
	if number == 0:
		#check if it's at the start of the sentence or brackets, as punctuation at the end was already checked before
		wordlist[number] = wordlist[number] + ','
		return wordlist
	elif re.match('(', wordlist[number]):
		wordlist[number] = wordlist[number] + ','
		return wordlist
		#add more exceptions
	else:
		return wordlist
#"ne" function
def ne(wordlist, number):
	if number == 0:
		return wordlist
	counter = 0
	#check previous punctuation
	if re.match('.*[,:—-]$', wordlist[number-1]):
		return wordlist
	#add more exceptions
	else:
		while counter < number:
			#check if there's another "ne"
			if re.match('[nN]e[,—-]?$', wordlist[counter]):
				wordlist[number-1] = wordlist[number-1] + ','
				return wordlist
			counter = counter+1

	return wordlist
#"kaut gan" function
def kautgan(wordlist, number):
	if number == 0:
		return wordlist
	#add exceptions here
	if re.match('.*[,:—-]$', wordlist[number-1]):
		return wordlist
	else:
		wordlist[number-1] = wordlist[number-1] + ','
		return wordlist
#"kaut arī" function
def kautari(wordlist, number):
	if number == 0:
		return wordlist
	if re.match('.*[,:—-]$', wordlist[number-1]):
		return wordlist
	#add exceptions here
	#check if the sentence starts with "un kaut arī"
	if re.match('[uU]n$', wordlist[number-1]) and number == 1:
		return wordlist
	else:
		wordlist[number-1] = wordlist[number-1] + ','
		return wordlist
#"kāpēc" function
def kapec(wordlist, number):
	if number == 0:
		return wordlist
	#check the exception words
	if re.match('.*[,;:—-]$|[Uu]n$|[Bb]et$|[Tt]ad$|[Vv]ai$|[Nn]ezin$', wordlist[number-1]):
		return wordlist
	#add exceptions here
	else:
		wordlist[number-1] = wordlist[number-1] + ','
		return wordlist
#"cik" function
def cik(wordlist, number):
	if number == 0:
		return wordlist
	#check all the excepton words
	if re.match('.*[,;:—-]$|[Uu]n$|[Bb]et$|[Tt]ad$|[Vv]ai$|[Nn]ezin$|[Jj]o$|[Pp]ar$|[Uu]z$|[Zz]em$|[Vv]irs$|[Pp]ie$|[Nn]ezin$', wordlist[number-1]):
		return wordlist
	#add exceptions here
	if number > 1:
		if re.match('arī$', wordlist[number-1]) and re.match('[lL]ai$', wordlist[number-2]):
			return wordlist
	wordlist[number-1] = wordlist[number-1] + ','
	return wordlist
#"kā arī" function
def kaaarii(wordlist, number):
	#If "kā" is in the begining of sentence or the previous word has punctuation marks at the end of it, return it
	if number == 0 or re.match('.*[(,;:—-]', wordlist[number-1]):
		return wordlist
	#if the previous word is one of the exceptions, try to put comma before them instead, if that's adequate
	if re.match('[lL]ai$|[Nn]o$|[Uu]z$', wordlist[number-1]):
		if number > 1:
			if not re.match('.*[(,;:—-]', wordlist[number-2]):
				wordlist[number-2] = wordlist[number-2] + ','
				return wordlist
			else:
				return wordlist
		return wordlist
	#Add other exceptions here
	#if no exceptions are met, put comma in default position and return the sentece
	else:
		wordlist[number-1] = wordlist[number-1] + ','
		return wordlist
#"proti" function
def proti (wordlist, number):
	counter = 0
	#check if there's an "-t/-ties" word after it in a short sentence
	if len(wordlist) > 1 and len(wordlist) < 6:
		while counter < len(wordlist):
			if re.match('.*t[,.?!:""]?[.]?[.]?$|.*ties[,.?!:""]?[.]?[.]?$', wordlist[counter]):
				return wordlist
			counter = counter + 1
	#if that is not the case, test if there's the word "tu" before it.
	elif len(wordlist) > 5:
		if number > 0:
			while counter < number:
				if re.match('[tT]u[.,]?[.]?[.]?$', wordlist[counter]):
					return wordlist
				counter = counter + 1
	#check if "proti" is the last word, in which case it is unlikely to be an insertion
	if len(wordlist) == number + 1:
		return wordlist
	#check if punctuation on either sides and if "proti" is the first word of the sentence
	if number != 0:
		if re.match('.*[(,.:;—-]$', wordlist[number-1]):
			if len(wordlist) > number + 1 and not re.match('.*[,.:;)""]', wordlist[number]):
				wordlist[number] = wordlist[number] + ','
			return wordlist
	#Add more exceptions here
		else:
			wordlist[number-1] = wordlist[number-1] + ','
			if len(wordlist) > number + 1 and not re.match('.*[,.:;)""]', wordlist[number]):
				if not re.match('-', wordlist[number+1]):
					wordlist[number] = wordlist[number] + ','
				return wordlist

			else:
				return wordlist
	else:
		if not re.match('.*[,.:;)""]', wordlist[number]):
			wordlist[number] = wordlist[number] + ','
			return wordlist
#"tad" function
def tad(wordlist, number):
	if number == 0:
		return wordlist
	else:
		#check if the previous word has punctuation marks already or it's one of the exception words
		if not re.match('.*[)(,:—;]$|.*[.][.][.]$|[("]?[uU]n$|[("]?[bB]et$|[("]?[tT]aču$|[("]?[tT]omēr$', wordlist[number-1]):
			counter = 0
			#add more exceptions here
			if number > 1:
				#check if "ja" or "kad" are present
				while counter < number:
					if re.match('[jJ]a[,.]?[.]?[.]?$|[kK]ad[,.]?[.]?[.]?$', wordlist[counter]):
						wordlist[number-1] = wordlist[number-1] + ','
						return wordlist
					counter = counter + 1
			return wordlist
		else:
			return wordlist	
#"ko", "ar ko" and "par ko" function
def ko(wordlist, number):
	if number == 0:
		return wordlist
	if number > 0:
		#check the "ar ko" and "par ko" word laws
		if re.match('[aA]r$|[pP]ar$', wordlist[number-1]):
			if number == 1:
				return wordlist
			else:
				#check their exception words both before and after
				if not re.match('.*[,:;-—]$|[(]?[uU]n$|[bB]et$|[vV]ai$|[nN]e$|[nN]av$|[iI]r$|[tT]ik$', wordlist[number-2]):
					if len(wordlist) > number+1:
						if not re.match('citu[),.:;!?]$', wordlist[number+1]):
							wordlist[number-2] = wordlist[number-2] + ','
						return wordlist
					else:
						wordlist[number-2] = wordlist[number-2] + ','
				else:
					return wordlist
		#check if exception words are before it
		elif not re.match('.*[,:;-—]$|[dD]audz$|[kK]aut$|[lL]ai$|[tT]ad$|[uU]z$|[nN]e$|[uU]n$|[bB]et$|[vV]ai$', wordlist[number-1]):
			#check if exception words are after it
			if len(wordlist) > number + 1:
				if re.match('.*u[).,:;""]?$', wordlist[number+1]):
					return wordlist
				else:
					wordlist[number-1] = wordlist[number-1] + ','
		#add more exceptions here
		return wordlist
#"nevis" function
def nevis(wordlist, number):
	if not number == 0:
		#test for exception words before the word
		if not re.match('.*[(,:;-—]$|[(]?[uU]n$|[(]?[bB]et$', wordlist[number-1]):
			if len(wordlist) > number + 1:
				counter = number
				#check for "bet" existence after "nevis"
				while counter+1 < len(wordlist):
					if re.match('bet[,.:—-]?', wordlist[counter]):
						return wordlist
					counter = counter + 1 
			#add new exceptions here
			wordlist[number-1] = wordlist[number-1] + ','
			return wordlist
		else:
			return wordlist
		return wordlist
	else:
		return wordlist
#"respektīvi" function
def respektivi(wordlist, number):
	if not number == 0:
		#add exceptions here
		#check if there arent punctuation marks before or after the word, in which case put the commas
		if not re.match('.*[(,:;-—]$', wordlist[number-1]):
			wordlist[number-1] = wordlist[number-1] + ','
		if len(wordlist) > number+1:
			if not re.match('.*[)(,:;—-]$', wordlist[number]) and not re.match('-—', wordlist[number+1]):
				wordlist[number] = wordlist[number] + ','
	else:
		if len(wordlist) > number+1:
			if not re.match('.*[)(,:;—-]$', wordlist[number]) and not re.match('-—', wordlist[number+1]):
				wordlist[number] = wordlist[number] + ','
	return wordlist


#Interface module
#specify the input file
inFile = open('testi/testin.txt', 'r')
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
# sentences = textsplitter(data)
# sentenceTest = open('testi/sentences.txt', 'w')
# counter = 0
# for sentence in sentences:
# 	sentenceTest.write(sentence)
# 	sentenceTest.write('\n')
# 	counter = counter + 1
# sentenceTest.write('%d' % counter)
# sentenceTest.close()
#writetext(data, file)
