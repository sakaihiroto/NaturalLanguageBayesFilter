# -*- coding: utf-8 -*-
import pandas as pd
import os
from docutils.parsers.rst.directives import encoding

dfLists=[]

def reader():
    csvFileNameLists = os.listdir('./csv')
    os.chdir('./csv')
    
    for fileName in csvFileNameLists:
        df = pd.read_csv(fileName, encoding='utf-8', engine='python')
        
        dfLists.append(df)

    return dfLists

if __name__ == '__main__':
    reader()

