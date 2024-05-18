import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import sklearn.metrics as sklm


filename = 'iris.csv'
df = pd.read_csv(filename)


np.random.seed(1234)

df_train, df_test = train_test_split(df, test_size = 0.2)

feature_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
target_name = 'species'


X_train = df_train[feature_names]
y_train = df_train[target_name]
X_test = df_test[feature_names]
y_test = df_test[target_name]


# Naive Bayes

nb_classifier = GaussianNB()

nb_classifier.fit(X_train, y_train)

df_test['NB_predicted'] = nb_classifier.predict(X_test)
df_test['NB_correct'] = df_test['NB_predicted'] == df_test[target_name]


# K Nearest Neighbors
knn_classifier = KNeighborsClassifier(n_neighbors = 5)

knn_classifier.fit(X_train, y_train)

df_test['5NN_predicted'] = knn_classifier.predict(X_test)
df_test['5NN_correct'] = df_test['5NN_predicted'] == df_test[target_name]

# Decision Tree
dt_classifier = DecisionTreeClassifier()

dt_classifier.fit(X_train, y_train)

df_test['DT_predicted'] = dt_classifier.predict(df_test[feature_names])
df_test['DT_correct'] = df_test['DT_predicted'] == df_test[target_name]

# Confusin matrix
conf = sklm.confusion_matrix(df_test[target_name], df_test['5NN_predicted'])
metrics = sklm.precision_recall_fscore_support(df_test[target_name], df_test['5NN_predicted'])
print(all(df_test['DT_correct']))
print(all(df_test['5NN_correct']))
print(all(df_test['NB_correct']))
print(metrics)