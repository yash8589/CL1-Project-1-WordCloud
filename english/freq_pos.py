import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from nltk.probability import FreqDist




stop_words = set(stopwords.words('english'))



file1 = open("nofor.txt")
line = file1.read()
words = line.split()

tokenized = sent_tokenize(line)
for i in tokenized:
	
	
	wordsList = nltk.word_tokenize(i)

	wordsList = [w for w in wordsList if not w in stop_words]  # removing stopwords again for caution......so we can input original data in it also


	tagged = nltk.pos_tag(wordsList)

	# print(tagged)

c = Counter(tagged)


fdist = FreqDist(tagged)

fdist.plot(30,cumulative=False)
plt.show()

