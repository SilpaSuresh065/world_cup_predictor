# ⚽ World Cup Predictor (Machine Learning Project)

## 🏆 Overview

This project is a **Machine Learning-based World Cup Match Predictor** that predicts the outcome of football matches (Win / Loss / Draw) based on historical match data.

It also includes a **Streamlit web application** for interactive predictions.

---

## 🚀 Features

* Predict match results (Win / Loss / Draw)
* Supports multiple teams and tournaments
* Machine Learning model using Random Forest Classifier
* Encoded team and tournament data
* Interactive web UI using Streamlit
* Easy to use dropdown-based interface

---

## 📁 Project Structure

```
world_cup_predictor/
│
├── app.py                  # Streamlit web app
├── train_model.py         # Model training script
├── data/
│   └── results.csv        # Dataset
│
├── model/
│   ├── model.pkl          # Trained ML model (NOT uploaded to GitHub if large)
│   ├── home_encoder.pkl   # Home team encoder
│   ├── away_encoder.pkl   # Away team encoder
│   └── tour_encoder.pkl   # Tournament encoder
│
├── requirements.txt       # Dependencies
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/world_cup_predictor.git
cd world_cup_predictor
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Train the Model (Important Step)

If `model.pkl` is not available, train the model:

```bash
python train_model.py
```

This will generate:

* model.pkl
* encoders for teams and tournaments

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 📊 How It Works

1. User selects:

   * Home Team
   * Away Team
   * Tournament

2. Data is encoded into numerical values

3. Random Forest model predicts:

   * Win / Loss / Draw

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas
* Scikit-learn
* Streamlit
* Joblib

---

## ⚠️ Important Note

* Large files like `model.pkl` may exceed GitHub's 100MB limit.
* If not included, run `train_model.py` to generate it locally.

---

## 👨‍💻 Author

Developed as a Machine Learning project for learning and demonstration purposes.

---

## ⭐ Future Improvements

* Add team rankings feature
* Improve accuracy with advanced models
* Add live match API data
* Deploy on cloud (Streamlit Cloud / Render)
