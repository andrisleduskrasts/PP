import re
#Text splitting module
def textsplitter(content):
	sentences = re.findall('.*?[A-Za-z0-9āčēģīķļņšūž][.!?][][!""''()*+,.;<=>?@\^_{|}~]*?\s?|.*?[.?!]+[^.]|.*?[.?!]+$|.*?$', content)
	#The current regex also splits situations like "tas utt. ļāva un 1997. gadā"
	counter = 0
	while counter + 1 < len(sentences):
		if re.match('[a-zāčēģīķļņšūž)].*|[.?!]', sentences[counter]):
			if counter != 0:
				sentences[counter-1] = sentences[counter-1] + sentences[counter]
				sentences.pop(counter)
				counter = counter - 1
		counter = counter + 1
	#If a non-first sentence starts with lower letter, add it to the previous sentence and pop it out of the list
	return sentences
