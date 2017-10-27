# -*- coding: utf-8 -*-
from bayes import BayesianFilter
import csvReader

bf = BayesianFilter()

df = csvReader.reader()

columns = df.columns

for col in columns:
    print(col)
    
    for val in df[col]:
        print(val)

        bf.fit(val,col)


pre, scorelist = bf.predict("兵庫県川西市坂根二丁目25-6-305")

print("結果=", pre)
print(scorelist)

