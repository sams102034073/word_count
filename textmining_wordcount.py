import nltk
import string
import csv
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
nltk.download('punkt')
nltk.download('stopwords')
stopwords = set(stopwords.words('english'))

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
    stopwords.add("--")
    stopwords.add("'s")
    stopwords.add("'ve")
    stopwords.add("'re")
    stopwords.add("n't")
    stopwords.add("``")
    stopwords.add("ai")
    stopwords.add("''")
l = ([w for w in allwords if w not in stopwords])

counter = Counter(l)
for name, count in counter.most_common():
    print('{0}: {1}'.format(name, count))

with open('wordcount.csv', 'w') as csvfile:
    # set up header
    fieldnames = ['word', 'count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for word, count in counter.most_common():
        writer.writerow({'word': word, 'count': count})




















