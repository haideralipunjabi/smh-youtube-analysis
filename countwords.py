import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json_lines
import os
from progress.bar import Bar
import json

files  = os.listdir("rawdata")
stopwords = stopwords.words('english')

bar = Bar('Progress: ', max=len(files))
data = {}
for file in files:
    file_data = json_lines.reader(open('rawdata/'+file,'r'))
    for comment in file_data:
        tokens = word_tokenize(comment['text'])
        for word in tokens:
            word = word.lower()
            if word not in stopwords and word.isalpha():
                if word in data.keys():
                    data[word] += 1
                else:
                    data[word] = 1
    bar.next()
bar.finish()

data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1],reverse=True)}
json.dump(data,fp=open("wordcount.json","w"))
                

