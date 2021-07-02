from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize



file1 = open("nostop.txt")
ps = PorterStemmer()
sentence = file1.read()

words = word_tokenize(sentence)

for w in words:
	print(w, " : ", ps.stem(w))
