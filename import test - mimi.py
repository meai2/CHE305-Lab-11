import pandas as pd
import glob
import numpy as np
from IPython.display import display

def read_r6(path):
    path = r'https://github.com/meai2/CHE305-Lab-11/tree/main/Data/Refrigerant%3D0.66%20kg'
    all_files = glob.glob(path + "/*.csv")

    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)

    df = pd.concat(li, axis=0, ignore_index=True)
    return df
   
def read_r7(path):
    path = r'https://github.com/meai2/CHE305-Lab-11/tree/main/Data/Refrigerant%3D0.7%20kg'
    all_files = glob.glob(path + "/*.csv")

    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)

    df = pd.concat(li, axis=0, ignore_index=True)
    return df

def read_r8(path):
    path = r'https://github.com/meai2/CHE305-Lab-11/tree/main/Data/Refrigerant%3D0.8%20kg'
    all_files = glob.glob(path + "/*.csv")

    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)

    df = pd.concat(li, axis=0, ignore_index=True)
    return df

def read_r88(path):
    path = r'https://github.com/meai2/CHE305-Lab-11/tree/main/Data/Refrigerant%3D0.88%20kg'
    all_files = glob.glob(path + "/*.csv")

    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)

    df = pd.concat(li, axis=0, ignore_index=True)
    return df

def read_r1(path):
    path = r'https://github.com/meai2/CHE305-Lab-11/tree/main/Data/Refrigerant%3D1%20kg'
    all_files = glob.glob(path + "/*.csv")

    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)

    df = pd.concat(li, axis=0, ignore_index=True)
    return df