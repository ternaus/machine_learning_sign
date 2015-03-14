#!/usr/bin/env python
from __future__ import division
__author__ = 'Vladimir Iglovikov'

import pandas as pd
import os
import sqlite3
import math

#read data into the dataframe

data_path = os.path.join('..', 'data', 'square.db')


con = sqlite3.connect(data_path)

df = pd.read_sql("SELECT * FROM DQMC", con)

df = df[df["avg_sign_value"] >= 0.1]

#Now I want to keep only rows, where number_of_sites is equal to 16, 36, 64, 100

df = df[(df["number_of_sites"] == 16) | (df["number_of_sites"] == 36) | (df["number_of_sites"] == 64) | (df["number_of_sites"] == 100)]

result = df[["total_energy_value", "number_of_sites", "beta", "mu_up", "u"]]

# It should not really matter right now, but later, when I will add results of the exact diagonalization
# I will not be able to use beta infinity, thus I will creat column that will correspond to a column
result["temperature"] = 1 / result["beta"]

result.drop("beta", 1)

result.to_csv("cleaned_data.csv")

