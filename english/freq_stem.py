
#########################################################
file1 = open("nostop.txt")
text = file1.read()
# text = " ". join(paragraph)
words = text.split(" ")

from collections import Counter

cnt = Counter(words)

cnt.most_common(10)




# importing modules
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
tokenstem = []

file1 = open("nostop.txt")
sentence = file1.read()

# sentence = "Programmers program with programing languages"
words = word_tokenize(sentence)

for w in words:
	tokenstem.append(ps.stem(w))


##########trial run of graph making

# print(fdist)

# from nltk.tokenize import word_tokenize
# from nltk.probability import FreqDist

# import matplotlib.pyplot as plt
# from matplotlib.pyplot import figure
# from matplotlib.font_manager import FontProperties
# import matplotlib as mpl


# mpl.rcParams['font.sans-serif'] = ['Source Han Sans TW',
#                                    'sans-serif',
#                                    "Lohit Devanagari"  # fc-list :lang=hi family --> run in bash to check what fonts are supported
#                                    ]


# figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
# # a = list.copy(fdist)
# # b = dict(a)


# # val_val = b.values()
# # key_val = b.keys()
# # plt.bar(key_val,val_val)
# # plt.show()


# # Lemma
# # a = list.copy(Lemma_all)
# # b = dict(a)


# # val_val = b.values()
# # key_val = b.keys()
# # plt.bar(key_val,val_val)
# # plt.show()

# fdist = FreqDist(lemma_all)
# fdist.plot(30,cumulative=False)
# plt.show()

from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# print(tokenized_word)

fdist = FreqDist(tokenstem)
# print(fdist)
# print(fdist.most_common(2))

fdist.plot(30,cumulative=False)
plt.show()


