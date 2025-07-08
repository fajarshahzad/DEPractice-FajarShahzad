# Updated to include automatic plotting of model performance using seaborn/matplotlib
import sys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog,
                             QLabel, QMessageBox, QComboBox)
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression, Perceptron
from sklearn.svm import SVC, SVR
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, mean_squared_error
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import datetime
import os

class MLApp(QWidget):
    def __init__(self):
        super().__init__()
        self.df = None
        self.target = None
        self.problem_type = None
        self.scaler = None
        self.latest_results = None
        self.results_dict = {}  # Store model scores for plotting
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("AI Lab - EDA & ML with PDF Export")
        self.setGeometry(100, 100, 600, 500)
        self.setStyleSheet("background-color: #121212; color: #ffffff;")

        layout = QVBoxLayout()

        self.label = QLabel("Welcome! Please load a dataset to start.")
        self.label.setFont(QFont("Segoe UI", 12))
        layout.addWidget(self.label)

        button_style = """
            QPushButton {
                background-color: #1db954;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 20px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #1ed760;
            }
        """

        combo_style = """
            QComboBox {
                background-color: #333;
                color: white;
                border-radius: 10px;
                padding: 6px;
            }
        """

        self.btn_load = QPushButton("1. Load Dataset")
        self.btn_load.setStyleSheet(button_style)
        self.btn_load.clicked.connect(self.load_dataset)
        layout.addWidget(self.btn_load)

        self.target_selector = QComboBox()
        self.target_selector.setStyleSheet(combo_style)
        self.target_selector.currentIndexChanged.connect(self.update_target)
        layout.addWidget(self.target_selector)

        self.problem_selector = QComboBox()
        self.problem_selector.setStyleSheet(combo_style)
        self.problem_selector.addItems(["Select Problem Type", "Classification", "Regression"])
        layout.addWidget(self.problem_selector)

        self.btn_preprocess = QPushButton("2. Preprocess Data")
        self.btn_preprocess.setStyleSheet(button_style)
        self.btn_preprocess.clicked.connect(self.preprocess_data)
        layout.addWidget(self.btn_preprocess)

        self.btn_train = QPushButton("3. Train Models")
        self.btn_train.setStyleSheet(button_style)
        self.btn_train.clicked.connect(self.train_models)
        layout.addWidget(self.btn_train)

        self.btn_pdf = QPushButton("4. Generate PDF Report")
        self.btn_pdf.setStyleSheet(button_style)
        self.btn_pdf.clicked.connect(self.generate_pdf)
        self.btn_pdf.setEnabled(False)
        layout.addWidget(self.btn_pdf)

        self.setLayout(layout)

    def load_dataset(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open CSV", "", "CSV Files (*.csv)")
        if path:
            self.df = pd.read_csv(path)
            self.label.setText(f"Loaded dataset with shape {self.df.shape}")
            self.target_selector.clear()
            self.target_selector.addItems(["Select Target Column"] + list(self.df.columns))

    def update_target(self):
        self.target = self.target_selector.currentText() if self.target_selector.currentIndex() > 0 else None

    def preprocess_data(self):
        if self.df is None or self.target is None or self.problem_selector.currentIndex() == 0:
            self.show_message("Error", "Please load dataset, select target and problem type.")
            return

        self.problem_type = self.problem_selector.currentText().lower()

        for col in self.df.select_dtypes(include=['object']).columns:
            self.df[col] = LabelEncoder().fit_transform(self.df[col])

        self.df.fillna(self.df.mean(numeric_only=True), inplace=True)

        self.scaler = StandardScaler()
        features = self.df.drop(columns=[self.target])
        self.X = self.scaler.fit_transform(features)
        self.y = self.df[self.target]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42)

        self.show_message("Success", "Preprocessing Done!")

    def train_models(self):
        if self.problem_type is None:
            self.show_message("Error", "Please preprocess the data first.")
            return

        results = ""
        self.results_dict = {}

        if self.problem_type == "classification":
            models = {
                "Logistic Regression": LogisticRegression(),
                "SVC": SVC(),
                "Decision Tree": DecisionTreeClassifier(),
                "Random Forest": RandomForestClassifier(),
                "KNN": KNeighborsClassifier(),
                "Naive Bayes": GaussianNB(),
                "Perceptron": Perceptron()
            }
            for name, model in models.items():
                model.fit(self.X_train, self.y_train)
                preds = model.predict(self.X_test)
                acc = accuracy_score(self.y_test, preds)
                results += f"{name}: Accuracy = {acc:.4f}\n"
                self.results_dict[name] = acc
        else:
            models = {
                "Linear Regression": LinearRegression(),
                "SVR": SVR(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest": RandomForestRegressor(),
                "KNN": KNeighborsRegressor()
            }
            for name, model in models.items():
                model.fit(self.X_train, self.y_train)
                preds = model.predict(self.X_test)
                mse = mean_squared_error(self.y_test, preds)
                results += f"{name}: MSE = {mse:.4f}\n"
                self.results_dict[name] = mse

        self.latest_results = results
        self.show_message("Results", results)
        self.btn_pdf.setEnabled(True)

        # Automatically show model comparison plot
        self.plot_model_results()

    def plot_model_results(self):
        metric = "Accuracy" if self.problem_type == "classification" else "MSE"
        plt.figure(figsize=(10, 6))
        sns.barplot(x=list(self.results_dict.keys()), y=list(self.results_dict.values()), palette="viridis")
        plt.title(f"Model {metric} Comparison", fontsize=16)
        plt.ylabel(metric)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def generate_pdf(self):
        if not self.latest_results:
            self.show_message("Error", "Train models first!")
            return

        path, _ = QFileDialog.getSaveFileName(self, "Save Report", "", "PDF Files (*.pdf)")
        if not path:
            return

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c = canvas.Canvas(path, pagesize=letter)
        width, height = letter

        c.setFont("Helvetica-Bold", 16)
        c.drawString(30, height - 50, "AI Lab ML Report")
        c.setFont("Helvetica", 10)
        c.drawString(30, height - 70, f"Generated: {now}")
        c.drawString(30, height - 85, f"Target Column: {self.target}")
        c.drawString(30, height - 100, f"Dataset Shape: {self.df.shape}")
        c.drawString(30, height - 120, "Model Results:")

        y = height - 135
        for line in self.latest_results.split("\n"):
            if y < 60:
                c.showPage()
                y = height - 50
            c.drawString(40, y, line)
            y -= 15

        try:
            sns.heatmap(self.df.corr(), annot=True, cmap='coolwarm')
            plt.title("Correlation Heatmap")
            plt.tight_layout()
            heatmap_path = "heatmap.png"
            plt.savefig(heatmap_path)
            plt.close()
            c.showPage()
            c.drawImage(heatmap_path, 30, 200, width=550, preserveAspectRatio=True)
        except Exception as e:
            c.drawString(30, y, f"Plot Error: {e}")

        c.save()
        self.show_message("Saved", f"Report saved to: {path}")

    def show_message(self, title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.exec_()
#main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MLApp()
    window.show()
    sys.exit(app.exec_())
