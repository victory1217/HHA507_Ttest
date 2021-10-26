# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

##Step 1- Import pandas package 

import pandas as pd

##Step 2- Bring in dataframe using the raw code link in GitHub 

diabetic_data = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')

##Step 3- Identify categorical and numerical values in dataset

list(diabetic_data)

##For this assignment, the columns of interest are : 
##  'gender', 'time_in_hospital', 'race', 'num_lab_procedures'

##Gender is a column consisting of categorical data
##Time in hospital is a column consisting of numerical data (measured in days)
##Race is a column consisting of categorical data 
##Number of lab procedures is a column cnsisting of numerical data 

###FIRST QUESTION: Is there a difference between sex (M:F) and the number of days in hospital?

##Step 4- Create variables for both genders in dataframe 

Females = diabetic_data[diabetic_data['gender'] == 'Female']
Males = diabetic_data[diabetic_data['gender'] == 'Male']

##Step 5- Perform a 2-sample T-test to solve question

from scipy.stats import ttest_ind

ttest_ind(Females['time_in_hospital'], Males['time_in_hospital'])
##Ttest stat result: 9.542637042242887
##Ttest pvalue result: 1.4217299655114968e-21
##Conclusion: Since the p value is below .05, it means that there is a significant 
##difference between females and males in relation to total number of days in hospital. 




