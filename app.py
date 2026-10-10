
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page settings
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Website heading
st.title("🏠 House Price Prediction")
st.write("Predict the estimated price of a house.")

st.divider()

# House details
st.subheader("Enter House Details")

area = st.number_input(
    "Area (square feet)",
    min_value=100,
    max_value=10000,
    value=1200
)

bedrooms = st.selectbox(
    "Number of Bedrooms",
    [1, 2, 3, 4, 5, 6, 7, 8]
)

bathrooms = st.selectbox(
    "Number of Bathrooms",
    [1, 2, 3, 4, 5, 6]
)

age = st.number_input(
    "Age of House (years)",
    min_value=0,
    max_value=200,
    value=5
)
location = st.selectbox(
    "Location",
    ["Kozhikode", "Kochi", "Malappuram", "Kannur"]
)
# Prediction button
if st.button("Predict House Price"):
    house = pd.DataFrame([{
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "age": age,
        "location": location
    }])

    price = model.predict(house)[0]

    st.success("Prediction Completed!")

    st.subheader("Estimated House Price")
    st.write(f"₹ {price:,.0f}")

    st.caption(
        "This estimate is based on sample training data "
        "and is not an actual market valuation."
    )
