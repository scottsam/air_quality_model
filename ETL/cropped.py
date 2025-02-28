import pandas as pd
import numpy as np
import zipfile



"""
Load utility functions
-----------------------
- Function to create the names of MPs in each Constituents
- Function to create the level of NO2 in air
"""

# Constituency function to
# include MPs
def mps(x):
    if x == 'Bristol East':
        return 'Kerry McCarthy'
    elif x == 'Bristol North East':
        return 'Darren Jones'
    elif x == 'Bristol South':
        return 'Karin Smyth'
    else:
        return 'Thangam Debbonaire'
        



# No2 band function to
# Include NO2 bands as moderate, low, very high

def no2_level(x):
    if x >= 0 and x <= 200:
        return 'Low'
    elif x > 200 and x <= 400:
        return 'Moderate'
    elif x > 400 and x <= 600:
        return 'High'
    else:
        return 'Very High'
    
"""
Load the required datasets for preprocessing
"""

# load air_quality raw data
air_df = pd.read_csv('../raw_data/Air_Quality_Continuous.csv')
air_df = air_df.copy().round(2)



# Load constituency data
const_df = pd.read_csv('../clean_data/constituency.csv')
const_df = const_df.copy()


# create a mapping of site ID to create st_id
ob = {}
site_list = air_df['Site_ID'].unique().tolist()
for i , j in enumerate(site_list):
    ob[j] = i+1
    
air_df['st_id']  = air_df['Site_ID'].map(ob)




# create mapping of constinuents 
con = {}
const_df = const_df[~(const_df['Constituency'] == 'Constituency not found')]


con_list = const_df['Constituency'].unique().tolist()
for i , j in enumerate(con_list):
    con[j] = i+1
const_df['ct_id']  =  const_df['Constituency'].map(con)



# rename column
const_df = const_df.rename(columns={'Site_No': 'Site_ID',
                                    "Constituency":"ct_name"
                                    })


#include name of mps
const_df['ct_mp'] = const_df['ct_name'].apply(mps)


# Include No2 level info
air_df['band'] = air_df['NO2'].apply(no2_level)


# convert datetime
air_df["Date_Time"] = pd.to_datetime(air_df["Date_Time"], errors='coerce')


# Filter datetime
air_df = air_df[(air_df['Date_Time'] >= '2015/01/01')]



#Merge dataset
air_df= pd.merge(air_df,const_df,on='Site_ID')


# Create cropped csv file
cropped_df = air_df.to_csv('clean_data/cropped.csv',index=False)


# extract pollutants
pollutant_column = ["NOx", "NO2", "NO", "PM10", "O3", "NVPM10", "VPM10", "NVPM2_5", "PM2_5", "VPM2_5", "CO", "SO2"]


# Fill missing measurements with 0
air_df.fillna(value={"Temperature": 0, "RH": 0, "Pressure": 0}, inplace=True)

# Remove rows missing critical data
air_df.dropna(subset=["Date_Time", "Site_ID"], inplace=True)  


# fill missing pollutant values with 0
for val in range(len(pollutant_column)):
    air_df.fillna(value={pollutant_column[val]:0},inplace=True)

# drop irrelevant columns
air_df = air_df.drop(['ObjectId'],axis=1)



# Create clean csv file from cropped
cleaned_df = air_df.to_csv('clean_data/cleaned.csv',index=False)


#csv files to zip
cropped = 'clean_data/cropped.csv'
cleaned = 'clean_data/cleaned.csv'



zip_filename = 'cropped.zip'

with zipfile.ZipFile(zip_filename,"w",zipfile.ZIP_DEFLATED) as myzip:
        myzip.write(cropped,arcname='cropped.csv')
        myzip.write(cleaned,arcname='cleaned.csv')
print(f"Files zipped successfully into {zip_filename}!") 










