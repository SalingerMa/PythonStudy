# -*- coding: utf-8 -*-
import requests
import pandas
import os
from matplotlib import pyplot as plt
path = r"C:\Users\mhm\Desktop\study\\"
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
r = requests.get(url)
with open(path+"iris.csv", 'w') as f:
    f.write(r.text)
os.chdir(path)
df = pandas.read_csv(path + 'iris.csv',
                     names=['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])

groupdata = df.groupby("class")
groupmean = groupdata.mean()
groupmean.plot(kind="ked")
plt.legend(loc="upper center",bbox_to_anchor=(0.5, 1.2), ncol=2)
plt.show()

# print(df['sepal length'])
# print(df.ix[:3, :2])
# print("--------")
# print(df.ix[:3, [x for x in df.columns if 'width' in x]])
