"""
session_transition_matrix.py

This script analyzes session-based categorical data from 'Genel_unibolum.xlsx' and generates 
a transition matrix that counts how many times each FactorId follows another within the same SessionId.

For each session, it tracks sequential transitions between FactorIds and stores the frequency 
of each transition in a square matrix.

Use Cases:
- Feature engineering for sequence-based categorical transitions
- User behavior analysis in session data
- Clickstream or activity flow analysis
- Building features for machine learning models based on factor order

Input:
- Genel_unibolum.xlsx (Excel file with SessionId and FactorId columns)

Output:
- Genel_unibolum_output.xlsx (Excel file with the resulting transition matrix)
"""


import pandas as pd
import numpy as np 

df = pd.read_excel('your_file_name', engine='openpyxl')

id = df["your_column_name1"]
category = df["your_column_name2"]
unique_category = df["your_column_name2"].unique()
unique_id = df["your_column_name1"].unique()

#print(unique_category)
#print(unique_id)

matris = pd.DataFrame(index = unique_category, columns = unique_category)

matris[:] = 0  

for index, value in enumerate(category):
    if index > 0:
        if id[index] == id[index-1]:
            previous_value = category[index - 1]
            matris.at[previous_value, value] = matris.at[previous_value, value] + 1
        
print(matris)

matris.to_excel('your_file_name.xlsx', index=True)

