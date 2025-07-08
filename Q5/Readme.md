# 🌦️ Lahore Weather ETL Pipeline

This project demonstrates a complete **ETL (Extract, Transform, Load)** pipeline to fetch **historical weather data** for **Lahore** using the [Open-Meteo API](https://open-meteo.com/), clean and transform the data, store it in a **SQLite** database and CSV, and generate **visualizations**.

---

## 📌 Features

- 🔄 Extracts 7 years of historical weather data (temperature, windspeed, precipitation)
- 🧹 Transform `None` values and replaces them with `0`
- 💾 Saves cleaned data to both **CSV** and **SQLite** database
- 📊 Generates **pie chart visualizations** from any column
- 🔐 Uses a `.env` file for API parameters and sensitive values


## ⚙️ ETL Flow

### 1. 📥 Extract
- API: [`archive-api.open-meteo.com`](https://open-meteo.com/en/docs)
- Parameters:
  - `latitude=31.5497`, `longitude=74.3436` (Lahore)
  - Daily metrics: temperature, precipitation, windspeed
  - Data range: 7 years back from today

### 2. 🧹 Transform
- Converts `None` to `0`
- Exports `cleaned_weather.csv`

### 3. 💾 Load
- Saves the final dataframe to:
  - `cleaned_weather.csv`
  - SQLite DB `lahore_weather.db`, table `lahore_weather`

### 4. 📊 Visualize
- Function `visualize_column_distribution(df)` creates pie charts
- Visualizes distribution of all non-numeric or categorical columns


## 🚀 How to Run

### 1. Install Dependencies

pip install pandas requests matplotlib sqlalchemy python-dotenv

python main.py


