import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
# 🌿 Ayurvedic Inventory Management

Manage Ayurvedic Products Easily

---
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Products", "100+")

with col2:
    st.metric("Categories", "12")

with col3:
    st.metric("Suppliers", "25")

st.image(
    "https://images.unsplash.com/photo-1515377905703-c4788e51af15",
    width=1200
)

st.success("Healthy Inventory. Healthy Business.")