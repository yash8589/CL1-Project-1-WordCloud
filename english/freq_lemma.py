import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer





stop_words = set(stopwords.words('english'))



wnl = WordNetLemmatizer()
lemma = []

file1 = open("nostop.txt")
line = file1.read()
words = line.split()
word1 = nltk.word_tokenize(line)

for word in word1:
    lemma.append(wnl.lemmatize(word))	

c = Counter(lemma)


fdist = FreqDist(lemma)

fdist.plot(30,cumulative=False)
plt.show()

