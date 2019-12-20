# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:49:18 2019

@author: Nishu Sharma
"""

import pandas as pd
import matplotlib.pyplot as plt
url = "https://archive.ics.uci.edu/ml//machine-learning-databases/iris/iris.data"
# Load dataset into Pandas Dataframe
df = pd.read_csv(url, names=['sepal length', 'sepal width', 'petal length', 'petal width', 'Target'])
from sklearn.preprocessing import StandardScaler
features = ['sepal length', 'sepal width', 'petal length', 'petal width']
# Separating out the features
x = df.loc[:, features].values
# Separating out the target
y = df.loc[:, ['Target']].values
# Standardizing the features
x = StandardScaler().fit_transform(x)
print(x)
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents,
                           columns = ['Principal Component 1', 'Principal Component 2'])
print(principalDf)