import multidict as multidict
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def makeI(text):

    wc = WordCloud(background_color="white", max_words=75)
    wc.generate_from_frequencies(text)

    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

def getFrequency(sentence):
    full = multidict.MultiDict()
    TDict = {}
    for text in sentence.split(" "):
        val = TDict.get(text, 0)
        TDict[text] = val + 1
    for key in TDict:
        full.add(key, TDict[key])
    return full


file = open("nostop.txt")
text = file.read()
makeI(getFrequency(text))
