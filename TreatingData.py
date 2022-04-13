# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 21:10:33 2022

@author: armin
"""

#Import necessary libraries
import pandas as pd
import csv
import os
import glob

#Path to the folder containing csv files
all_path = "C:/Users/armin/Documents/CHE305 Code/0.66 kg/*csv"

#Function meant to convert csv files to dataframs and place them in a list
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



#Step 1: Import raw data as dataframes
df66 = import_data(all_path)
count = len(df66) #Count number of datasets
rows = [] #Create empty array for steady state data
data_path = "C:/Users/armin/Documents/CHE305 Code/Data.csv" #Path to final dataset csv file

#Step 2: Check for steady state in all of the datasets
for i in range(0,len(df66)): #Loop through all datasets
    df = df66[i] #Grab dataset
    SS = False #Set steady state condition to false
    data_count = len(df["Time (s)"]) #Count number of lines in dataset
    n = 1 #Create a counter to start at the second row of the dataset
    
    while SS == False and n < data_count: #While still not at steady state and more rows to check
        #Check set of steady state conditions
        #Create a percentage difference for the following operating parameters
        delta_check1 = (df["Q2 (ml/mn)"][n]-df["Q2 (ml/mn)"][n-1])/df["Q2 (ml/mn)"][n-1]
        delta_check2 = (df["Q3 (ml/mn)"][n]-df["Q3 (ml/mn)"][n-1])/df["Q3 (ml/mn)"][n-1]
        delta_check3 = (df["T4 (°C)"][n]-df["T4 (°C)"][n-1])/df["T4 (°C)"][n-1]
        
        #Check using defined acceptable tolerances
        if abs(delta_check1) < 0.01 and abs(delta_check2) < 0.001 and abs(delta_check3) < 0.0001:
            print ("true") #Visible check of number of datasets achieve steady state
            SS = True #Set condition to true
        else:
            n = 1 + n #If still not reached steady state, check next row
    
    #Step 3: Collect steady state conditions
    if SS == True:
        #Convert time to steady state to float
        hold_time = df["Time (s)"][n]
        hold_time = float(hold_time.split(" (")[0])
        #Check if time is below or above 10 minutes and assign accordingly
        if hold_time < 600:
            SS_time = "<10 Minutes"
        if hold_time >= 600:
            SS_time = ">=10 Minutes"
            
        #Collect remaining data
        SS_Q2 = df["Q2 (ml/mn)"][n]
        SS_Q3 = df["Q3 (ml/mn)"][n]
        SS_T4 = df["T4 (°C)"][n]
        #Temperature difference is useful due to variable starting conditions
        SS_delT4 = df["T4 (°C)"][n]-df["T4 (°C)"][0] 
        SS_Power = df["P (Watt)"][n]
        SS_HP = df["HP (abs.bar)"][n]
        SS_LP = df["LP (abs.bar)"][n]
        #Fluid amount must be changed manually according to imported folder
        SS_fluid = float(0.66)
        
        #Append all data to steady state array
        rows.append([SS_Q2, SS_Q3, SS_T4, SS_Power, SS_delT4, SS_HP, SS_LP, SS_fluid, SS_time])

#Write the steady state data to a csv file
with open(data_path, mode='a', newline='') as f: #Write and append mode modified as used
    writer = csv.writer(f)
    writer.writerows(rows)
    f.close()
        