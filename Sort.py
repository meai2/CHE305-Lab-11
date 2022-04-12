# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 21:10:33 2022

@author: armin
"""

#Import
import pandas as pd
import csv
import os
import glob

all_path = "C:/Users/armin/Documents/CHE305 Code/0.66/*csv"

def import_data(allpath):
    '''Path should lead to a folder of csv files. Function takes in pathname as a str and returns a list of dataframes 
    for each converted csv file'''
    
    all_path = "C:/Users/armin/Documents/CHE305 Code/0.66/*csv"
    
    # stores file paths into a list
    all_files = glob.glob(all_path)

    # stores all converted csv files in the folder into a list
    li = []

    # loops through the raw data list and converts csv files to dataframes and appends to list
    for file in all_files:
        df = pd.read_csv(file,encoding='unicode_escape',sep=';')
        del df['Unnamed: 15']
        li.append(df)

    return li

df66 = import_data(0.66)
count = len(df66)
SS_time = []

for i in range(0,len(df66)):
    df = df66[i]
    SS = False
    data_count = len(df["Time (s)"])
    n = 1
    
    while SS == False and n < data_count:
        delta_check1 = (df["Q2 (ml/mn)"][n]-df["Q2 (ml/mn)"][n-1])/df["Q2 (ml/mn)"][n-1]
        delta_check2 = (df["Q3 (ml/mn)"][n]-df["Q3 (ml/mn)"][n-1])/df["Q3 (ml/mn)"][n-1]
        delta_check3 = (df["T4 (°C)"][n]-df["T4 (°C)"][n-1])/df["T4 (°C)"][n-1]
        if abs(delta_check1) < 0.01 and abs(delta_check2) < 0.0001 and abs(delta_check3) < 0.0001:
            print ("true")
            SS = True
        else:
            n = 1 + n
    
    if SS == True:
        SS_time.append(df["Time (s)"][n])
        