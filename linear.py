# -*- coding: utf-8 -*-
"""linear.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-X8uN-slR6H8uTogCFhekkPhmCxkvmIa
"""

import numpy as np
import sklearn
from sklearn import linear_model
height=[[4.0],[5.0],[6.0],[7.0],[8.0],[9.0],[10.0]]
weight=[  8, 10 , 12, 14, 16, 18, 20]
reg=linear_model.LinearRegression()
reg.fit(height,weight)
X_height=[[12.0]]
print(reg.predict(X_height))