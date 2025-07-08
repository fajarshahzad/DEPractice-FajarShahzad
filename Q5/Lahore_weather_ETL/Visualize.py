import matplotlib.pyplot as plt
import pandas as pd
import os
def plot_temperature_trend(df,max_unique:int=10):
    print("📊 Visualizing  temperature...")
    for column in df.columns:
        if df[column].nunique() <= max_unique and df[column].dtype != 'float64':
            value_counts = df[column].value_counts()
            
            plt.figure(figsize=(6, 6))
            plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=140)
            plt.title(f"Pie Chart of '{column}'")
            plt.axis('equal')
            plt.tight_layout()
            os.makedirs("output", exist_ok=True)
            plt.savefig(f"output/Lahore_weather_of_{column}.png")
            plt.show()
    
