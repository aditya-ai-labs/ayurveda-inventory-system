import streamlit as st
import requests
import pandas as pd

st.title("📊 Admin Dashboard")

response = requests.get(
    "http://127.0.0.1:8000/products/"
)

products = response.json()

total_products = len(products)

total_stock = sum(
    p["quantity"]
    for p in products
)

total_sold = sum(
    p["sold"]
    for p in products
)

c1,c2,c3 = st.columns(3)

c1.metric(
    "Products",
    total_products
)

c2.metric(
    "Stock",
    total_stock
)

c3.metric(
    "Sold",
    total_sold
)

st.divider()

for product in products:

    col1,col2 = st.columns([8,1])

    with col1:
        st.write(
            f"{product['name']} | Stock : {product['quantity']}"
        )

    with col2:

        if st.button(
            "❌",
            key=product["id"]
        ):

            requests.delete(
                f"http://127.0.0.1:8000/products/delete/{product['id']}"
            )

            st.rerun()

df = pd.DataFrame(products)

st.dataframe(
    df,
    use_container_width=True
)