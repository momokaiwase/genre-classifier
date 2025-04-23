import csv
from sklearn.model_selection import train_test_split
import numpy as np

##SPLIT TRAINING AND TESTING DATA

#make separate csv file for only testing data for LLM classification

with open('final_dataset.csv', 'r') as file:
    csv_reader = csv.reader(file)

#get lyrics without stopwords removed
X = np.genfromtxt('final_dataset.csv', delimiter=',', skip_header=1, dtype=int)
X = X[:, :-1] #first : selects all rows, :-1 selects all except last column

print(X)

#get genre integer label
y = np.genfromtxt('final_dataset.csv', delimiter=',', skip_header=1, dtype=int)
y = y[:, -1] #all rows, just last column

print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) #, random_state=42