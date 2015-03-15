#!/usr/bin/env python
from __future__ import division
__author__ = 'Vladimir Iglovikov'

# from pylab import *
import pandas as pd
import os
import sqlite3
import math
import seaborn as sns

#read data into the dataframe

data_path = os.path.join('..', 'data', 'square.db')

con = sqlite3.connect(data_path)

df = pd.read_sql("SELECT * FROM DQMC", con)

df = df[df["avg_sign_value"] >= 0.1]

#Now I want to keep only rows, where number_of_sites is equal to 16, 36, 64, 100

N = 16
u = 4
beta = 4

df = df[(df["number_of_sites"] == N) & (df["u"] == u) & (df["beta"] == beta)]



# It should not really matter right now, but later, when I will add results of the exact diagonalization
# I will not be able to use beta infinity, thus I will creat column that will correspond to a column
df["temperature"] = 1 / df["beta"]

df = df.sort('mu_up')

sns.tsplot(df["mu_up"], df["total_energy_value"])
