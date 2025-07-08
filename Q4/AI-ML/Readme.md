# 🧠 ML Model Trainer & Evaluator GUI

A PyQt5-based desktop application that allows users to:

- 📁 Load CSV datasets  
- 🔎 Select target column and problem type (Classification or Regression)  
- ⚙️ Preprocess data automatically  
- 🏋️‍♂️ Train multiple machine learning models in one go  
- 📊 Visualize model comparison using Seaborn/Matplotlib  
- 📝 Export results and correlation heatmap to a PDF report  

---

## 🚀 Features

| Feature                           | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| 📂 Load Dataset                  | Open and load any CSV dataset                                              |
| 🏷️ Target Selection              | Choose which column to predict                                             |
| 🔀 Auto Preprocessing            | Label encoding, missing value handling, standard scaling                   |
| 🤖 Multiple Models               | Trains several classification or regression models                         |
| 📉 Metric Display                | Shows Accuracy (for Classification) or MSE (for Regression)                |
| 📊 Plot Comparison               | Auto-generated bar chart for visual model performance                      |
| 📎 PDF Export                    | Save a detailed report including results and correlation heatmap           |

---

## 📦 Technologies Used

- **Python 3.x**
- **PyQt5** – GUI framework
- **Pandas / NumPy** – Data handling
- **Scikit-learn** – Machine learning
- **Matplotlib / Seaborn** – Data visualization
- **ReportLab** – PDF generation

---

## 📷 Screenshots

> 💡 Optional – Add images of the app UI, bar charts, or PDF report pages here.

---

## 🧪 Supported Models

### 🟦 Classification:
- Logistic Regression  
- Support Vector Classifier (SVC)  
- Decision Tree  
- Random Forest  
- K-Nearest Neighbors (KNN)  
- Naive Bayes  
- Perceptron  

### 🟨 Regression:
- Linear Regression  
- Support Vector Regressor (SVR)  
- Decision Tree Regressor  
- Random Forest Regressor  
- K-Nearest Neighbors Regressor  

---

## 🧑‍💻 How to Run

1. **Install dependencies:**

   pip install pandas numpy seaborn matplotlib scikit-learn pyqt5 reportlab


