#Importing required Libraries
import pandas as pd

#Read the json file
df = pd.read_json('data.json')
print(df)


#Convert Height in meteres and calculate BMI using the given formula
df['Height(m)'] = df['HeightCm']/100 
df['BMI(kg/m)'] = df['WeightKg']/df['Height(m)']


#Applying the Risk criteria by iterating over each row and evaluting BMI category, Health Risk and categorizing the same in "BMI_Category" and "Health_Risk" column

for i, row in df.iterrows():
    
    if df.loc[i,'BMI(kg/m)'] <= 18.4:
        df.loc[i,'BMI_Category'] = 'UnderWeight'
        df.loc[i,'Health_Risk'] = 'Malnutrition Risk'

    elif df.loc[i,'BMI(kg/m)'] > 18.4 and df.loc[i,'BMI(kg/m)'] < 24.9:
        df.loc[i,'BMI_Category'] = 'Normal Weight'
        df.loc[i,'Health_Risk'] = 'Low Risk'
        
    elif df.loc[i,'BMI(kg/m)'] > 25 and df.loc[i,'BMI(kg/m)'] < 29.9:
        df.loc[i,'BMI_Category'] = 'OverWeight'
        df.loc[i,'Health_Risk'] = 'Enhanced Risk'
        
    elif df.loc[i,'BMI(kg/m)'] > 30 and df.loc[i,'BMI(kg/m)'] < 34.9:
        df.loc[i,'BMI_Category'] = 'Moderately Obese'
        df.loc[i,'Health_Risk'] = 'Medium Risk'
        
    elif df.loc[i,'BMI(kg/m)'] > 35 and df.loc[i,'BMI(kg/m)'] < 39.9:
        df.loc[i,'BMI_Category'] = 'Severely Obese'
        df.loc[i,'Health_Risk'] = 'High Risk'
        
    elif df.loc[i,'BMI(kg/m)'] > 40:
        df.loc[i,'BMI_Category'] = 'Very Severely Obese'
        df.loc[i,'Health_Risk'] = 'Very High Risk'


#Print the results and save it as a csv for reference        
print(df)
df.to_csv('results.csv')