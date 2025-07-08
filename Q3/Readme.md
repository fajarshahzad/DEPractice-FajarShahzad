## 🔄 ETL Process

### 1. 🧲 Extract
- Fetch university data from the Hipolabs API
- Save the raw response to a CSV in `/extracted_data/`

### 2. 🧹 Transform
- Filter universities whose name contains "California"
- Flatten list-type fields (`domains`, `web_pages`)
- Clean and structure the data

### 3. 📊 Visualize
- Plot a bar chart showing **top 10 domains** used by California universities
- Show plot in the console (optional: save as image)

### 4. 💾 Load
- Save the cleaned and filtered data into a local SQLite DB (`my_lite_store.db`)
- Table name: `cal_uni`

---

## ▶️ How to Run

1. **Install Requirements**
   ```bash
   pip install pandas requests sqlalchemy matplotlib seaborn
