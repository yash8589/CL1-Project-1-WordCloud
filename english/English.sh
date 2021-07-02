#!bin/bash
# nostop

# corpus collection, cleaning and sentence tokenization
python3 crawl.py > text_with_stop.txt                   # corpus collection from <p> tags in wikipedia
python3 removefor.py > nofor.txt                        # remove foreign words from the collected corpus
python3 sentencetoken.py > sentencetoken.txt            # tokenizes the sentences before running punctuation.py
python3 punctuation.py                                  # removes all the punctuations from the file

# word tokenization, POS tagging, stopwords removal, stemming and lemmatization
python3 tokenizer.py > tokens.txt                       # tokenizes the words and stores in tokens.txt
python3 POS.py > POS.txt                                # does POS tagging on nofor.txt
python3 stopwords.py                                    # removes stopwords and stores data in nostop.txt
python3 stemt.py > stemt.txt                            # stemming of words and putting it in stemt.txt
python3 lemma.py > lemma.txt                            # lemmatization of words and putting it in lemma.txt

# frequency graphs, wordcloud
python3 freq_withstop.py                                # plots frequency graph of text_with_stop.txt  
python3 freq_WORDS.py                                   # plots frequency graph of nostop.txt
python3 freq_pos.py                                     # plots POS freq graph of nofor.txt
python3 freq_stem.py                                    # plots stem freq graph for nostop.txt      
python3 freq_lemma.py                                   # plots lemma freq graph for nostop.txt
python3 wc.py                                           # plots a wordcloud of nostop.txt                                   