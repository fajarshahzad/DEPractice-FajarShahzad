##ETL Pipeline
import os
import matplotlib.pyplot as plt
import seaborn as sns
import requests ##Extract Data from Api's
import pandas as pd ##Perform Data transformation
from sqlalchemy import create_engine ##Collection to a database
def extract()->dict:
    ##Extract data from http://universities.hipolabs.com/search?country=United+States
    API_URL="http://universities.hipolabs.com/search?country=United+States"
    data=requests.get(API_URL).json()
    # Create folder if not exists
    folder="extracted_data"
    os.makedirs(folder,exist_ok=True)
    # Save to CSV
    df=pd.DataFrame(data)
    csv_path=os.path.join(folder,"universities_raw.csv")
    df.to_csv(csv_path, index=False)
    print(f"Extracted data saved to: {csv_path}")
    return data
def visualize(df:pd.DataFrame)->None:
    sns.set(style='darkgrid')
    domain_counts=df['domains'].value_counts().head(10)
    plt.figure(figsize=(10,6))
    sns.barplot(x=domain_counts.values, y=domain_counts.index, palette="viridis")
    plt.title("Top 10 Most Common University Domains (California)")
    plt.xlabel("Number of Universities")
    plt.ylabel("Domain")
    plt.tight_layout()
    os.makedirs("output", exist_ok=True)
    plt.savefig("output/ca_university_domains.png")
    plt.show()
def transform(data:dict)->pd.DataFrame:
    ## Transform Data
    df=pd.DataFrame(data)
    print(f"Total number of universities from the API {len(data)}")
    df=df[df["name"].str.contains("California")]
    print(f"Total number of universities in California {len(df)}")
    df['domains']=[','.join(map(str,l)) for l in df['domains']]
    df['web_pages']=[','.join(map(str,l)) for l in df['web_pages']]
    df=df.reset_index(drop=True)
    return df[["domains","country","web_pages","name"]]
def load(df:pd.DataFrame)->None:
    ## Load Data into Sqlite Database
    disk_engine=create_engine('sqlite:///my_lite_store.db')
    df.to_sql('cal_uni',disk_engine,if_exists='replace')

print("ETL Pipeline Basics")
print("1.Extract\n2.Transform\n3.Load")
state=True
while state:
    option=int(input("Go with the Flow:"))
    if option==1:
        data=extract()
        print("Data Extracted from the API")
    elif option==2:
        df=transform(data)
        print("✅ Data Transformed")
        visualize(df)   # <-- Add this line
    elif option==3:
        load(df)
        print("Data Loaded into .db file")
        state=False
    elif option>3 or option<1:
        print("Invalid option..:(")
        print("Logging out..!")
        state=False
