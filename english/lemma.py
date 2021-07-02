import nltk
from nltk.stem import WordNetLemmatizer

wnl = WordNetLemmatizer()

file1 = open("nostop.txt")
line = file1.read()
words = line.split()
word1 = nltk.word_tokenize(line)

for word in word1:
    print(word, " : ", wnl.lemmatize(word))