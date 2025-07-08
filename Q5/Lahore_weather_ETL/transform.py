import pandas as pd

def transform_weather_data(df: pd.DataFrame, output_csv_path: str = "cleaned_weather_data.csv"):
    print("🔧 Transforming data...")
    df_cleaned = df.fillna(0)
    df_cleaned.to_csv(output_csv_path, index=False)
    print(f"✅ Cleaned CSV saved as '{output_csv_path}'")

    return df_cleaned

