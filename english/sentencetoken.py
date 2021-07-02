import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')

line = open("nofor.txt")
text = line.read()

# text = 'Hola amigo. Estoy bien.'
print(tokenizer.tokenize(text))
