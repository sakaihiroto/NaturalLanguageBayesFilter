# -*- coding: utf-8 -*-
import pandas as pd
import os
from docutils.parsers.rst.directives import encoding

def reader():
    os.chdir("./csv")
    df = pd.read_csv('sample.csv',encoding='utf-8',engine='python')
    
    return df

if __name__ == '__main__':
    reader()

