import pandas as pd
from extract import extract
from transform import transform_weather_data
from load import load_data_to_db
from Visualize import plot_temperature_trend

print("ETL Pipeline For Lahore Weather")
print("1.Extract\n2.Transform\n3.Load")
state=True
while state:
    option=int(input("Go with the Flow:"))
    if option==1:
        data=extract()
        print("Data Extracted from the API")
    elif option==2:
        df_raw = pd.read_csv("./extracted_data/Lahore_weather_raw.csv")
        df_cleaned = transform_weather_data(df_raw, "cleaned_lahore_weather.csv")
        print("✅ Data Transformed")
        plot_temperature_trend(df_cleaned)
    elif option==3:
        load_data_to_db(df_cleaned)
        print("Data Loaded into .db file")
        state=False
    elif option>3 or option<1:
        print("Invalid option..:(")
        print("Logging out..!")
        state=False
