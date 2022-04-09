import pandas as pd
import glob
import numpy as np
from IPython.display import display

path = r'https://github.com/meai2/CHE305-Lab-11/tree/main/Data/Refrigerant%3D0.66%20kg'
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)