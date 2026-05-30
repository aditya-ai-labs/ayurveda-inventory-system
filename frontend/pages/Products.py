import streamlit as st
import requests

st.title("🌿 Ayurvedic Products")

search = st.text_input(
    "🔍 Search Product"
)

response = requests.get(
    "http://127.0.0.1:8000/products/"
)

products = response.json()

filtered_products = []

for product in products:

    if search.lower() in product["name"].lower():
        filtered_products.append(product)

cols = st.columns(3)

for index, product in enumerate(filtered_products):

    with cols[index % 3]:

        image = product["image"]

        if not image:
            image = "https://via.placeholder.com/300"

        st.image(
            image,
            use_container_width=True
        )

        st.subheader(
            product["name"]
        )

        st.write(
            f"🌿 {product['category']}"
        )

        st.write(
            f"₹ {product['price']}"
        )

        st.write(
            f"Stock : {product['quantity']}"
        )

        buy = st.button(
            f"Buy #{product['id']}"
        )

        if buy:

            requests.put(
                f"http://127.0.0.1:8000/products/buy/{product['id']}"
            )

            st.success(
                "Product Purchased"
            )

            st.rerun()