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
all_path = "C:/Users/armin/Documents/CHE305 Code/0.66 kg/*csv"

def import_data(all_path):
    '''Path should lead to a folder of csv files. Function takes in pathname as a str and returns a list of dataframes 
    for each converted csv file'''
    
    #all_path = "C:/Users/armin/Documents/CHE305 Code/0.66/*csv"
    
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

#Import data for 0.66kg unit
df66 = import_data(all_path)
count = len(df66) #Count number of datasets
#SS_time = []
rows = []
data_path = "C:/Users/armin/Documents/CHE305 Code/Data.csv"

for i in range(0,len(df66)): #Loop through all datasets
    df = df66[i] #Grab dataset
    SS = False 
    data_count = len(df["Time (s)"]) #Count number of lines in dataset
    n = 1
    
    while SS == False and n < data_count: #While conditions
        #Check set of steady state conditions
        delta_check1 = (df["Q2 (ml/mn)"][n]-df["Q2 (ml/mn)"][n-1])/df["Q2 (ml/mn)"][n-1]
        delta_check2 = (df["Q3 (ml/mn)"][n]-df["Q3 (ml/mn)"][n-1])/df["Q3 (ml/mn)"][n-1]
        delta_check3 = (df["T4 (°C)"][n]-df["T4 (°C)"][n-1])/df["T4 (°C)"][n-1]
        if abs(delta_check1) < 0.01 and abs(delta_check2) < 0.001 and abs(delta_check3) < 0.0001:
            print ("true")
            SS = True
        else:
            n = 1 + n
    
    #If reach steady state, grab useful information
    if SS == True:
        hold_time = df["Time (s)"][n]
        hold_time = float(hold_time.split(" (")[0])
        #SS_time.append(float(hold_time.split(" (")[0]))
        if hold_time < 600:
            SS_time = "<10 Minutes"
        #if hold_time >= 420 and hold_time < 720:
            #SS_time = "7-12 Minutes"
        #if hold_time >= 600 and hold_time < 900:
            #SS_time = "10-15 Minutes"
        if hold_time >= 600:
            SS_time = ">=10 Minutes"
        SS_Q2 = df["Q2 (ml/mn)"][n]
        SS_Q3 = df["Q3 (ml/mn)"][n]
        SS_T4 = df["T4 (°C)"][n]
        SS_delT4 = df["T4 (°C)"][n]-df["T4 (°C)"][0]
        SS_Power = df["P (Watt)"][n]
        SS_HP = df["HP (abs.bar)"][n]
        SS_LP = df["LP (abs.bar)"][n]
        #SS_HPdiff = df["HP (abs.bar)"][n]-df["HP (abs.bar)"][0]
        #SS_LPdiff = df["LP (abs.bar)"][n]-df["LP (abs.bar)"][0]
        SS_fluid = float(0.66)
        rows.append([SS_Q2, SS_Q3, SS_T4, SS_Power, SS_delT4, SS_HP, SS_LP, SS_fluid, SS_time])

#Write the row to a csv file
with open(data_path, mode='a', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
    f.close()
        