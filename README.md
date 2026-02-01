# 🛡️ Phishing Website Detection System

A machine learning-based system to detect phishing websites using URL feature analysis.

---

## 📌 Project Overview

Phishing is a cyber attack where attackers create fake websites to steal sensitive information such as usernames, passwords, and banking details.

This project uses **machine learning** to analyze different features of a given URL and predict whether the website is **legitimate or phishing**.

The system takes a URL as input and returns a prediction in real time.

---

## 🚀 Features

- Detects phishing websites using ML
- Real-time URL input
- Feature-based analysis of URLs
- Fast and accurate predictions
- Simple and user-friendly interface

---

## 🧠 Technologies Used

- Python  
- Scikit-learn  
- Pandas  
- NumPy  
- Flask  
- HTML, CSS  

---

## 🔑 Feature Extraction

The system extracts the following features from the URL:

- **URL Length** – Total number of characters in the URL  
- **Number of Dots** – Counts the number of `.` in the URL  
- **Number of Hyphens** – Counts the number of `-` in the URL  
- **Number of '@' Symbols** – Detects redirection tricks  
- **IP Address Usage** – Checks whether the URL uses an IP address instead of a domain  

These features help identify suspicious patterns commonly found in phishing websites.

---

## 🤖 Machine Learning Model

The project uses supervised machine learning algorithms such as:

- Logistic Regression  
- Random Forest  
- Decision Tree  

(The best performing model is used for final prediction.)

---

## 🔍 How It Works

1. User enters a website URL  
2. The system extracts important features from the URL  
3. The ML model analyzes these features  
4. The system predicts:
   - `0` → Legitimate Website  
   - `1` → Phishing Website  

---

## 🛠️ Installation & Setup

### Step 1: Clone the repository
```bash
git clone https://github.com/your-username/Phishing_website_detection.git
cd Phishing_website_detection
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the application
```bash
python app.py
```

### Open in browser:

http://127.0.0.1:5000/
