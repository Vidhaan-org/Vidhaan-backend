import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import feature_extraction, linear_model, model_selection, preprocessing
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

df = pd.read_csv("ILDC_single.csv")

train_set = df.query(" split=='train' ")
test_set = df.query(" split=='test' ")
val_set = df.query(" split=='dev' ")
del train_set['split'],train_set['name'],val_set['split'],val_set['name'],test_set['split'],test_set['name']
print(train_set.head(10))

x_train = train_set['text']
y_train = train_set['label']

x_test = test_set['text']
y_test = test_set['label']

x_val = val_set['text']
y_val = val_set['label']
# del train_set,val_set,test_set
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

train_vectors = vectorizer.fit_transform(x_train)
clf = linear_model.RidgeClassifier()

scores = model_selection.cross_val_score(clf, train_vectors, y=y_train, cv=11, scoring="f1")
scores

clf.fit(train_vectors,y_train)

test_vectors = vectorizer.transform(x_test)
ConfusionMatrixDisplay.from_estimator(clf,test_vectors,y_test)
# plt.show()

# print(test_set.head())

test_vectors = vectorizer.transform(x_test)
ConfusionMatrixDisplay.from_estimator(clf,test_vectors,y_test)
# plt.show()

# print(test_set.head())

test_set['Prediction'] = clf.predict(test_vectors)
test_set['probability'] = clf.decision_function(test_vectors)

# print(test_set.head())

test_set = test_set.reset_index(drop=True)
# list(test_set['probability'])
print(test_set.head(20))


lbl,pred = list(test_set['label']),list(test_set['Prediction'])
right,wrong = 0,0

for i in range(len(lbl)):
    if lbl[i]==pred[i]:   #correct pred
        right+=1
    else:
        wrong+=1          #wrong pred
print(f"Accuracy: {100*(right/len(lbl))}")
print(f"Right predictions: {right}")
print(f"Wrong predictions: {wrong}")

print(clf.score(X=test_vectors,y=y_test))