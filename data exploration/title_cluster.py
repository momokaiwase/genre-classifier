#clusters of song titles (for k-means)

#make sure genism, numpy==1.24.3, scipy is installed

import nltk
nltk.download('stopwords')

import gensim
from nltk.corpus import stopwords
import numpy as np
import scipy as sp
import re
from sklearn.cluster import KMeans

stoplist = stopwords.words('english')
#add own stopwords into an array here: stoplist.extend()

#READ IN DATA
 
titles = []     # this will store the original song titles
titlestoks = []  # this will store the lists of tokens in those titles

#data file should be a text file contain one title per line
f = open("data exploration/streamedsongs421_titles.txt")
for line in f:
    line = line.rstrip()
    titles.append(line)
    line = re.sub(r"(^| )[0-9]+($| )", r" ", line)  # remove digits
    addme = [t.lower() for t in line.split() if t.lower() not in stoplist]
    titlestoks.append(addme)
f.close()

##IDENTIFY TOPICS
#!wget https://github.com/eyaler/word2vec-slim/raw/refs/heads/master/GoogleNews-vectors-negative300-SLIM.bin.gz
bigmodel = gensim.models.KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300-SLIM.bin.gz", binary=True)

#read in the normalized tokens for each headline, look up their vectors in the word2vec model, 
# and sum them all up into a single vector per headline

titlevectors = []   # this list will contain one 300-dimensional vector per headline

for h in titlestoks:
    totvec = np.zeros(300)
    for w in h:
        if w.lower() in bigmodel:
            totvec = totvec + bigmodel[w.lower()]
    titlevectors.append(totvec)

#k-means clustering - how many clusters is set beforehand: 
kmnews = KMeans(n_clusters=10, random_state=0)
titleclusters = kmnews.fit_predict(titlevectors)


# see what the clusters look like
# The `k-means fit_predict()` function in scikit returns a list containing a single integer for every input vector corresponding to the cluster ID that vector was assigned to. 
# iterate through that list of cluster assignments
# we can print out all the titles that belong to one of the clusters.

for i in range(len(titleclusters)):
    if titleclusters[i] == 3: #see all titles in cluster 3
        print(titles[i])

