##ETL Pipeline
import os
from dotenv import load_dotenv
import requests ##Extract Data from Api's
import pandas as pd ##Perform Data transformation
def extract()->dict:
    load_dotenv()
    API_URL=os.getenv("weather_url")
    data=requests.get(API_URL).json()
    # Create folder if not exists
    folder="extracted_data"
    os.makedirs(folder,exist_ok=True)
    # Save to CSV
    df = pd.DataFrame(data["daily"])
    df1=pd.DataFrame(data)
    csv_path=os.path.join(folder,"Daily_Lahore_weather_raw.csv")
    df.to_csv(csv_path, index=False)
    csv1_path=os.path.join(folder,"Lahore_weather_raw.csv")
    df1.to_csv(csv1_path,index=False)
    print(f"Extracted data saved to: {csv_path}")
    return data
