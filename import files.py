import pandas as pd
import csv
# from pandas import read_csv
# df = pd.read_csv(r'C:\Users\mimil\Desktop\School\Third Year\Second Semester\CHE305 - Lab\Lab 11\CHE305-Lab-11\w5.csv')
from os import listdir
from os.path import isfile,join 
files = [f for f in listdir('/Users/eemanabdulkadir/Documents/GitHub/CHE305-Lab-11/Data/Refrigerant=0.7 kg') if isfile(join('/Users/eemanabdulkadir/Documents/GitHub/CHE305-Lab-11/Data/Refrigerant=0.7 kg', f))]
