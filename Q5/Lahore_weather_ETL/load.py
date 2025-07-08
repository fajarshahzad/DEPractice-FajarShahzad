from sqlalchemy import create_engine
DB_Name='Lahore_Weather.db'
def load_data_to_db(df):
    print(f"💾 Loading data into SQLite DB: {DB_Name}")
    engine = create_engine(f"sqlite:///{DB_Name}")
    df.to_sql('lahore_weather', con=engine, if_exists='replace', index=False)
    print("✅ Data loaded into database.")
