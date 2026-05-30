import streamlit as st
import requests

st.title("➕ Add Product")

name = st.text_input(
    "Product Name"
)

category = st.selectbox(
    "Category",
    [
        "Powder",
        "Tablet",
        "Juice",
        "Oil",
        "Capsule"
    ]
)

price = st.number_input(
    "Price",
    min_value=0.0
)

quantity = st.number_input(
    "Quantity",
    min_value=1
)

image = st.text_input(
    "Image URL"
)

if st.button("Add Product"):

    data = {
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "image": image
    }

    response = requests.post(
        "http://127.0.0.1:8000/products/add",
        json=data
    )

    st.success(
        response.json()["message"]
    )