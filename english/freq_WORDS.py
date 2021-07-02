from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

file = open("nostop.txt")
text = file.read()
tokenwords=word_tokenize(text)
# print(tokenwords)

fdist = FreqDist(tokenwords)
# print(fdist)
# print(fdist.most_common(2))

fdist.plot(30,cumulative=False)
plt.show()

