import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

!wget -O PatientData.csv https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/drug200.csv

Dataset = pd.read_csv("PatientData.csv")
Dataset.head()
Dataset.shape

x = Dataset[["",""]].values
y = Dataset[""]
x.shape
y.shape

from sklearn.model_selection import train_test_split

Xtrain, Xtest, Ytrain, Ytest = train_test_split(x, y, test_size = o.7, random_state = 4)

model = DecisionTreeClassifier(criterion = "entropy", max_depth = 4)

model.fit(Xtrain, Ytrain)
Ytest_pred = model.predict(Xtest)

from sklearn import metrics

metrics.accuracy_score(Ytest_pred, Ytest)

