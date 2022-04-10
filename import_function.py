import pandas as pd
import csv
import os
import glob

def import_data(path):
    '''Path should lead to a folder of csv files. Function takes in pathname as a str and returns a list of dataframes 
    for each converted csv file'''
    
    # stores file paths into a list
    all_files = glob.glob(path + "/*.csv")

    # stores all converted csv files in the folder into a list
    li = []

    # loops through the raw data list and converts csv files to dataframes and appends to list
    for file in all_files:
        df = pd.read_csv(file,encoding='unicode_escape',sep=';')
        del df['Unnamed: 15']
        li.append(df)

    return li
