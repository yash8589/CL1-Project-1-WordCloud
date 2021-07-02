import nltk
words = set(nltk.corpus.words.words())

file = open("text_with_stop.txt")
sent = file.read()
print(" ".join(w for w in nltk.wordpunct_tokenize(sent) if w.lower() in words or not w.isalpha()))
