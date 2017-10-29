# -*- coding: utf-8 -*-
import pickle

from bayes import BayesianFilter
import csvReader


@profile
def study():
    bf = BayesianFilter()

    dfLists = csvReader.reader()

    for df in dfLists:
        columns = df.columns

        for col in columns:
            print(col)

            for val in df[col]:
                print(val)

                bf.fit(val, col)

    pre, scorelist = bf.predict("兵庫県川西市坂根二丁目25-6-305")

    print("結果=", pre)
    print(scorelist)


if __name__ == '__main__':
    study()
