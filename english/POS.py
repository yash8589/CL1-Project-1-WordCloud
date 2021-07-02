import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))



file1 = open("nofor.txt")
line = file1.read()
words = line.split()

tokenized = sent_tokenize(line)
for i in tokenized:
	
	wordsList = nltk.word_tokenize(i)

	wordsList = [w for w in wordsList if not w in stop_words]

	tagged = nltk.pos_tag(wordsList)

	print(tagged)
