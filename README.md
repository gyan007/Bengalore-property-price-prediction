# 🏠 Bangalore House Price Prediction App

This is a Machine Learning-powered web application built using **Streamlit** that allows users to **predict property prices in Bangalore** based on input features like location, total square feet, number of bedrooms (BHK), and number of bathrooms.

---

## 🔍 Project Overview

This app helps users (home buyers, real estate agents, and property investors) estimate the price of residential properties in Bangalore. It uses a regression model trained on real-world housing data to predict prices in **Lakhs of INR**.

The application features:
- 🧠 Machine learning model for price prediction
- 📍 Dynamic location selection
- 📊 Clean and responsive UI
- 🎨 Blurred background effect for modern feel
- 🚀 Easy deployment with Streamlit

---

## 🧰 Tech Stack

| Component         | Technology                      |
|------------------|----------------------------------|
| Frontend UI      | Streamlit                        |
| Machine Learning | Scikit-learn                     |
| Data Handling    | Pandas, NumPy                    |
| Deployment       | Streamlit Cloud / Local          |
| Language         | Python 3.x                       |

---

## 📁 Project Structure

```
bangalore_price_prediction/
├── model/
│   ├── banglore_home_prices_model.pickle
│   └── columns.json
├── istockphoto-1396856251-1024x1024.jpg
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## 📦 Installation

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/bangalore-price-predictor.git
cd bangalore-price-predictor
```

### 🔹 Step 2: Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 🔹 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App Locally

```bash
streamlit run streamlit_app.py
```

The app will open in your browser at:  
📍 `http://localhost:8501`

---

## 🌐 Deployment (Streamlit Cloud)

1. Push this project to GitHub.
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. Click “New App”
4. Connect your repo, select `streamlit_app.py` as the entry point.
5. Done! Your app will get a live URL.

---

## 🧠 Model Details

- Model: Trained using `LinearRegression` (or similar)
- Features used:
  - `total_sqft` (continuous)
  - `bath` (numerical)
  - `bhk` (numerical)
  - `location` (one-hot encoded from over 200+ locations)

Artifacts:
- `columns.json`: stores all features including location names
- `banglore_home_prices_model.pickle`: the trained model

---

## 🖼️ UI Highlights

- Blurred image background behind the form (modern look)
- Responsive design with two tabs:
  - **Tab 1:** Project info
  - **Tab 2:** Price prediction form
- Interactive inputs using Streamlit widgets

---

## ⚖️ License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
Feel free to use, modify, and distribute with attribution.

---

## 🤝 Contributing

Pull requests are welcome!  
For major changes, please open an issue first to discuss what you would like to change.

---

## 🙋‍♂️ Author

**Gyan Thakur**  
📧 Email: gyanthakurthakur@gmail.com  
📍 Pune, Maharashtra, India  
💼 [LinkedIn](https://www.linkedin.com/in/your-profile/) <!-- Replace with actual -->

---

## 📌 Acknowledgements

- Dataset: Bangalore House Price data (available on Kaggle / GitHub)
- Inspired by Krish Naik’s real estate model tutorial
- Background image: [iStock](https://www.istockphoto.com/)

---
