import gensim
import csv
import time

# Stores tokens from csv file
alltokens = []
# Open CSV file containing raw lyric tokens
with open('songs_final422.csv', 'r', encoding='utf-8') as csvfile:
    # Initiatilize csv reader
    csvreader = csv.reader(csvfile)
    next(csvreader) # Skip header row

    # Append lyric tokens to alltokens
    for row in csvreader:
        songtokens = row[3].replace('[', '').replace(']', '').replace('\"', '').replace('\'', '').split(', ')
        # Add songtokens to alltokens
        for token in songtokens:
            alltokens.append(token)

# print(alltokens)

alltokens = [a.split() for a in alltokens]

# Builds dictionary from alltokens
dictionary = gensim.corpora.Dictionary(alltokens)
print('done!')

# Create bag of words for each sentence
corpus = [dictionary.doc2bow(alltok) for alltok in alltokens]
print('done!')

# print(corpus[5])

print(time.ctime())
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=10, id2word=dictionary, passes=5)
print(time.ctime())

# Print out the 5 most strongly associated words for each topic
for i in range(10):
    words = ldamodel.show_topic(i, 10)
    for w in words:
        print(w[0], end=", ")
    print("\n")