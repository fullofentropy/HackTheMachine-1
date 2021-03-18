# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 11:27:21 2021

@author: Rhodora
"""

import pandas as pd


dict1 = {'1': [1,2,3]}
df = pd.DataFrame(dict1)
df

df.columns = ['column1']
print(df.head())

df1 = df.T
print(df1)



