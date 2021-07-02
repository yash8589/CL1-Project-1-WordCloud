from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

file = open("text_with_stop.txt")
text = file.read()
tokewords=word_tokenize(text)
# print(tokewords)

fdist = FreqDist(tokewords)
# print(fdist)
# print(fdist.most_common(2))

fdist.plot(30,cumulative=False)
plt.show()

