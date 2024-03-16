#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pandas as pd
import matplotlib as mtl
import math as mth



df1 = pd.read_csv('C:\\Users\\UMAID\\Downloads\\BTC-USD.csv', usecols=[0, 1, 2, 3, 4, 6])
print(df1)


df1['price'] = df1.Open.shift(-1)
print(df1)

df1['ret'] = df1.Close.pct_change()
print(df1)


df1 = df1.dropna()
print(df1)

profits = []
in_position = False
for index,row in df1.iterrows():
    if not in_position and row.ret > 0.01:
        buyprice = row.price
        in_position = True
        trailing_stop = buyprice*0.98
    if in_position:
        if row.Close* 0.98 >= trailing_stop:
            trailing_stop =rows.Close* 0.98
        if row.Close <= trailing_stop:
            sellprice = row.price
            profit =(sellprice-buyprice)/buyprice-0.0015
            profits.append(profit)
            in_position = False
print(profits)                

pd.Series(profits).plot()


(pd.Series(profits) + 1).cumprod().plot()

(pd.Series(profits) + 1).prod()

27423.929688/27423.929688
df1

len(profits)







