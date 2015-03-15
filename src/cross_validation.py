#!/usr/bin/env python

from __future__ import division
__author__ = 'Vladimir Iglovikov'

'''
This script will use cross validation on the existing training set to decide which algorithm for a given data will show
better results
'''

import pandas as pd
from sklearn import cross_validation
from sklearn.ensemble import RandomForestRegressor
df = pd.read_csv("cleaned_data.csv")
from sklearn import svm

target = df["total_energy_value"].values

train = df.drop("total_energy_value", axis=1).values

x_train, x_test, y_train, y_test = cross_validation.train_test_split(train, target, test_size=0.3, random_state=0)

print x_train.shape, x_test.shape, y_train.shape, y_test.shape

forest = RandomForestRegressor(n_jobs=2)

fit = forest.fit(x_train, y_train)

print fit.score(x_test, y_test)
