import nltk
import string
import spacy
import csv
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict, Counter
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
stopwords = set(stopwords.words('english'))
posDict = dict(line.strip().split('\t') for line in open('posTable.txt'))

lines = []
for line in open('building_global_community.txt'):
    # delete the blank and line feed at the begining and end
    line = line.strip()
    # add processed line text into list 'lines'
    lines.append(line.lower())

a = len(lines)
allwords = []
for i in range(0,a):
    words = word_tokenize(lines[i])
    allwords = allwords + words
for symbol in string.punctuation:
    stopwords.add(symbol)
l = ([w for w in allwords if w not in stopwords and w.isalnum()])
wordwithpos = nltk.pos_tag(l)
#for word, pos in wordwithpos:
#    print ('{0}/{1}'.format(word, pos))
if __name__ == '__main__':
    poswordcounter = defaultdict(Counter)
for word, pos in wordwithpos:
    poswordcounter[posDict[pos]][word] += 1
for pos, wordCounter in poswordcounter.items():
        print("{}:".format(pos))
        for word, count in wordCounter.most_common():
            print("%s: %d" % (word, count) )



#print(wordwithpos['NN'])
