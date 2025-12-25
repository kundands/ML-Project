# Student Exam Performance Prediction 🎓📊

## Project Overview

This project focuses on predicting a student’s **Math Score** based on academic, demographic, and preparation-related factors using Machine Learning techniques. The system takes multiple student attributes as input and predicts the expected math performance, helping educators and institutions understand the impact of different factors on academic outcomes.

The project demonstrates an **end-to-end Machine Learning workflow**, including data analysis, model training, evaluation, and deployment through a user-friendly web application. 
---

## Problem Statement

Student academic performance is influenced by various socio-economic, educational, and preparatory factors. However, identifying how these factors collectively affect a student’s math score can be challenging.

This project aims to build a predictive model that estimates a student’s **Math Score** based on the following inputs:

- Gender  
- Race / Ethnicity  
- Parental Level of Education  
- Lunch Type  
- Test Preparation Course  
- Reading Score (0–100)  
- Writing Score (0–100)  

Such predictions can assist educators in early intervention, personalized learning strategies, and data-driven academic planning.

---

## Key Features

- Predicts student **Math Score** using multiple input attributes
- Performs Exploratory Data Analysis (EDA) to identify key patterns
- Applies data preprocessing and feature engineering
- Trains and evaluates multiple machine learning models
- Saves the best-performing model for deployment
- Provides a web-based interface for real-time predictions
- Modular, scalable, and production-style project structure

---

## System Workflow

1. Student data is collected and explored using Jupyter Notebooks  
2. Categorical and numerical features are preprocessed  
3. Machine Learning models are trained and evaluated  
4. The best model is selected and saved as an artifact  
5. A web application loads the trained model  
6. Users input student details through the interface  
7. The system predicts and displays the **Math Score**

---

## Technology Stack

- **Programming Language:** Python  
- **Data Analysis:** pandas, numpy  
- **Visualization:** matplotlib, seaborn  
- **Machine Learning:** scikit-learn, CatBoost  
- **Development Environment:** Jupyter Notebook  
- **Web Framework:** Streamlit
- **Project Setup:** setup.py, requirements.txt  

---

## Setup and Installation

Follow the steps below to run the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/kundands/ML-Project.git
cd ML-Project
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux
```

### 3. Install required dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the web application
```bash
python app.py
```
