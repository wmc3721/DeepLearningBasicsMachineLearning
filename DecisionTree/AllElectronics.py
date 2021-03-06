#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:51211 
@file: AllElectronics.py 
@time: 2017/07/08 
"""

from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO
import numpy

# Read in the csv file and put features in a list of dict and list of class label
allElectronicsData = open(r'../DecisionTree/AllElectronics.csv', 'r')
reader = csv.reader(allElectronicsData)
headers = next(reader)

print(headers)

featureList = []
labelList = []

for row in reader:
    labelList.append(row[len(row) - 1])
    rowDict = {}
    for i in range(1, len(row) - 1):
        rowDict[headers[i]] = row[i]
    featureList.append(rowDict)

print(featureList)

# Vecorize features
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()

print("dummyX:" + str(dummyX))
print(vec.get_feature_names())

# Vecorize class labels
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY:" + str(dummyY))

# Using decision tree for classification分类器 entropy信息熵
clf = tree.DecisionTreeClassifier(criterion='entropy')
# 构建决策树
clf = clf.fit(dummyX, dummyY)
print("clf:" + str(clf))

# Visualize model
with open("allElectronicInformationGainOri.dot", 'w') as f:
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)

oneRowX = dummyX[0, :]
print("oneRowX:" + str(oneRowX))

newRowX = oneRowX

newRowX[0] = 1
newRowX[2] = 0
print("newRowX:" + str(newRowX))

# newRowX = numpy.array(newRowX).reshape((1, -1))
# predictedY = clf.predict(newRowX)

predictedY = clf.predict([newRowX])

print("predictedY:" + str(predictedY))
