import streamlit as st
import pickle
import json
import numpy as np


# Load the model and columns
def load_artifacts():
    with open("model/columns.json", "r") as f:
        data_columns = json.load(f)["data_columns"]
        locations = data_columns[3:]

    with open("model/banglore_home_prices_model.pickle", "rb") as f:
        model = pickle.load(f)

    return data_columns, locations, model


data_columns, locations, model = load_artifacts()


# Predict function
def predict_price(location, sqft, bhk, bath):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(model.predict([x])[0], 2)


# Page layout
st.set_page_config(page_title="Bangalore House Price Predictor", layout="centered")
st.title("🏠 Bangalore Property Price Prediction")

# Create tabs
tab1, tab2 = st.tabs(["🏡 Project Info", "📈 Predict Price"])

# --- Tab 1: Project Info ---
with tab1:
    st.image("istockphoto-1396856251-1024x1024.jpg", use_container_width=True)

    st.markdown("""
    Welcome to the **Bangalore House Price Prediction App**!  
    This app uses a machine learning model to estimate property prices in Bangalore based on:
    - Area (in square feet)
    - Number of bedrooms (BHK)
    - Number of bathrooms
    - Property location

    ---
    ### 🛠️ Technologies Used:
    - **Python** for backend and ML model
    - **Pandas & NumPy** for data analysis
    - **Scikit-learn** for building and training the model
    - **Streamlit** for deploying the web interface

    ---
    ### 🔍 How It Works:
    - A dataset of Bangalore properties was used to train the model.
    - Location is one-hot encoded.
    - Inputs are transformed into numerical features.
    - A trained model predicts the price in Lakhs ₹.

    ---
    **Designed & Developed by Gyan**
    """)

# --- Tab 2: Predict Price ---
with tab2:

    st.title("📈 Estimate Property Price")

    sqft = st.number_input("📏 Area (in square feet)", value=1000, step=50)
    bhk = st.selectbox("🛏️ Number of Bedrooms (BHK)", [1, 2, 3, 4, 5])
    bath = st.selectbox("🛁 Number of Bathrooms", [1, 2, 3, 4, 5])
    location = st.selectbox("📍 Location", sorted(locations))

    if st.button("💰 Estimate Price"):
        result = predict_price(location, sqft, bhk, bath)
        st.success(f"💰 Estimated Price: ₹ {result} Lakhs")

