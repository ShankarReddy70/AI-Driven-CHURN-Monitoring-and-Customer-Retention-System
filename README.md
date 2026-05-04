# 🚀 Customer Churn Prediction System (AI-Powered Dashboard)

## 📌 Project Overview

Customer churn is one of the biggest challenges faced by subscription-based businesses.
This project builds an **end-to-end Machine Learning system** to predict whether a customer is likely to churn and provides actionable insights through an interactive dashboard.

👉 The goal is to help businesses:

* Identify high-risk customers
* Improve retention strategies
* Increase revenue

---

## 🧠 Problem Statement

Companies lose a significant portion of customers due to churn.
By predicting churn in advance, businesses can take proactive actions such as:

* Offering discounts
* Improving engagement
* Providing personalized services

---

## ⚙️ Tech Stack

### 🔹 Programming & Libraries

* Python
* Pandas, NumPy
* Scikit-learn
* Plotly

### 🔹 Visualization & UI

* Streamlit

---

## 🏗️ Project Architecture

```
Raw Data 
   ↓
Data Cleaning 
   ↓
Feature Processing (Pipeline)
   ↓
Machine Learning Model
   ↓
Prediction System
   ↓
Streamlit Dashboard
```

---

## 🔥 Key Features

### 🤖 Machine Learning

* End-to-end ML pipeline using **Scikit-learn Pipeline**
* Automatic preprocessing with **ColumnTransformer**
* Logistic Regression model for churn prediction

### 📊 Dashboard

* Interactive Streamlit UI
* Real-time churn prediction
* Risk score visualization (Gauge Chart)
* Donut chart for churn vs retention
* KPI metrics (Tenure, Billing, Contract)

### 🧠 Business Intelligence

* Risk categorization (Low / Medium / High)
* Actionable recommendations
* Behavioral indicators

---

## 📊 Model Details

* Model Used: Logistic Regression
* Preprocessing:

  * OneHot Encoding (Categorical features)
  * Standard Scaling (Numerical features)
* Evaluation Metrics:

  * Accuracy
  * Precision
  * Recall
  * ROC-AUC

---

## 📈 Sample Output

* ✅ Customer Likely to Stay
* ⚠️ High Churn Risk
* 📊 Probability Score
* 📉 Risk Visualization

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone <your-github-repo-link>
cd Customer-Churn-Prediction
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Train the Model

```bash
python main.py
```

### 5️⃣ Run the Dashboard

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
Customer-Churn-Prediction/
│
├── data/                # Dataset
├── src/                 # Source code
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── pipeline.py
│   ├── train.py
│   ├── evaluate.py
│   ├── predict.py
│
├── models/              # Saved ML pipeline
├── outputs/             # Graphs and results
│
├── main.py              # Training pipeline
├── app.py               # Streamlit dashboard
├── requirements.txt
└── README.md
```

---

## 📸 Screenshots

👉 You can check in the images and outputs folders

* Dashboard UI
* Prediction results
* Gauge chart
* Confusion matrix
* ROC curve

---

## 💡 Business Impact

This system helps businesses:

* 🔻 Reduce customer churn
* 📈 Improve retention strategies
* 💰 Increase revenue
* 🎯 Enable targeted marketing

---

## 🚀 Future Improvements

* 🔍 SHAP Explainability (Why customer churns)
* 🌐 FastAPI backend
* 💻 Next.js frontend
* ☁️ Cloud deployment (AWS / GCP)
* 🤖 Advanced models (XGBoost, LightGBM)

---

## 🧠 Learnings from This Project

* Built a **production-style ML pipeline**
* Learned **end-to-end ML lifecycle**
* Designed **interactive dashboards**
* Understood **business impact of ML models**

---

## 👨‍💻 Author

**Yuva Karthikeswar Dadisetty**
📍 Aspiring Data Scientist / ML Engineer

---

## ⭐ Support

If you found this project useful, consider ⭐ starring the repository!
