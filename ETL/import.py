import pandas as pd
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import time

# load environment variables
load_dotenv()

"""
Utility functions
"""
# A function to convert dataframes to csv
def df_csv(df,name):
    return df.to_csv(name,index=False)

# A function to load large csv files
def load_large_data(query,cursor,conn_db):
    try:
        cursor.execute(query)
        conn_db.commit()
        print("Data loaded successfully!")
    except Error as err:
        print(f"Error: {err}")
    
"""
Database connection
"""    

# Database variables
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_database = os.getenv('DB_DATABASE')




# # create database connection
conn_db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database,
    allow_local_infile=True 
)


cursor = conn_db.cursor()


"""
Loading dataset
"""


#Load the CSV file
air_quality_df = pd.read_csv('clean_data\cleaned.csv')





"""
Extracting and Transforming data 
"""



# create constituency dataframe
constituent_df = air_quality_df[["ct_id","ct_name","ct_mp"]].drop_duplicates()


# extract pollutants
pollutant_column = ["NOx", "NO2", "NO", "PM10", "O3", "NVPM10", "VPM10", "NVPM2_5", "PM2_5", "VPM2_5", "CO", "SO2"]


# create pollutant df
# Create pollutant dataframe
pollutant_df = air_quality_df.melt(
    id_vars= ['ObjectId2'],
    value_vars=pollutant_column,
    var_name="pol_type",
    value_name="val"
)
pol = {}
pol_list = pollutant_df['pol_type'].unique().tolist()

for p,r in enumerate(pol_list):
    pol[r] = p + 1
pollutant_df['pol_id']  = pollutant_df['pol_type'].map(pol)
pollutant_df.rename(columns={'ObjectId2':'ms_id','val':'pol_value'},inplace=True)

#convert pollutant to a csv file
df_csv(pollutant_df,'clean_data/pollutant.csv')





# create measurement dataframe
measurement_df = air_quality_df[["Date_Time","ObjectId2", "st_id",'band']].drop_duplicates()
measurement_df.rename(columns={"Date_Time":"date_time",
                               "ObjectId2":"ms_id"},inplace=True)

#convert measurements to csv file
df_csv(measurement_df,'clean_data/measure.csv')


# create weather_df
weather_df = air_quality_df[["ObjectId2","Pressure","RH","Temperature"]].drop_duplicates()
weather_df.rename(columns={
    "ObjectId2":"ms_id",
    "Pressure":"pressure",
    "RH": "r_humidity",
    "Temperature": "temperature"
},inplace=True)

#convert weather to csv
df_csv(weather_df,'clean_data/weather.csv')



# create station/site dataframe
site_df = air_quality_df[["st_id","Site_ID","Name","Latitude","Longitude",'ct_id']].drop_duplicates()


"""
Loading data into database
"""


#Delete all data in database table
tables = ['Constituents','Sites','Pollutants','Measurements','WeatherReadings']
for table in tables:
    cursor.execute(f"delete from {table}")
    
conn_db.commit()    


#start time
start_time = time.time()

#  Insert data into constituency table
for index,row in constituent_df.iterrows():
    cursor.execute(""" INSERT INTO Constituents (ct_id,ct_mp,ct_name)
                       VALUES (%s, %s, %s) 
                   """, (row['ct_id'],row['ct_mp'],row['ct_name']))
    
conn_db.commit()
print('Constituents loaded successfully!')

 
    

# load site data
for index,row in site_df.iterrows():
    cursor.execute(""" INSERT INTO Sites (st_id,st_no,st_name,st_lat,st_long,ct_id)
                       VALUES (%s,%s,%s,%s,%s,%s) 
                   """,
                   (row['st_id'],row['Site_ID'],row['Name'],row['Latitude'],row['Longitude'],row["ct_id"])
                   )
conn_db.commit()
print('Sites loaded successfully!')







# load pollutant data using the csv file
pollution_query = """
    LOAD DATA LOCAL INFILE 'clean_data/pollutant.csv'
    INTO TABLE Pollutants
    FIELDS TERMINATED BY ',' 
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (@ms_id,@pol_type,@pol_value,@pol_id)
    SET pol_id = @pol_id, pol_type = @pol_type,pol_value= @pol_value,ms_id=@ms_id
    
"""
load_large_data(pollution_query,cursor,conn_db)





# # Load measurement data
measurement_query = """
    LOAD DATA LOCAL INFILE 'clean_data/measure.csv'
    INTO TABLE Measurements
    FIELDS TERMINATED BY ',' 
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (@date_time, @ms_id,@st_id,@band)
    SET ms_id = @ms_id, date_time = @date_time, st_id = @st_id, band= @band
    
"""
load_large_data(measurement_query,cursor,conn_db)



#Load weather data
weather_query = """
    LOAD DATA LOCAL INFILE 'clean_data/weather.csv'
    INTO TABLE WeatherReadings
    FIELDS TERMINATED BY ',' 
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS
    (@ms_id, @pressure,@r_humidity,@temperature)
    SET pressure = @pressure, temperature = @temperature, r_humidity= @r_humidity, ms_id = @ms_id
    
"""
load_large_data(weather_query,cursor,conn_db)



"""
Close database connection
"""
# close connection
cursor.close()
conn_db.close()



end_time = time.time()  # End the timer
execution_time = end_time - start_time

print(f"Execution time: {execution_time:.4f} seconds")
 






