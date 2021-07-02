import nltk
file_c = open("nofor.txt").read()
tokens = nltk.word_tokenize(file_c)
print(tokens)