import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Admin Dashboard",
    layout="wide"
)

# ---------------------------------
# CSS
# ---------------------------------

st.markdown("""
<style>

.hero{
    background:linear-gradient(
    135deg,
    #0f766e,
    #14b8a6
    );

    padding:35px;
    border-radius:20px;
    color:white;
    margin-bottom:25px;
}

.metric-card{
    background:#0f172a;
    padding:20px;
    border-radius:20px;
    border:1px solid #1e293b;
    text-align:center;
}

.metric-title{
    color:#94a3b8;
    font-size:16px;
}

.metric-value{
    color:#4ade80;
    font-size:34px;
    font-weight:bold;
}

.product-card{
    background:#0f172a;
    border:1px solid #1e293b;
    padding:15px;
    border-radius:15px;
    margin-bottom:10px;
}

.low-stock{
    color:#ef4444;
    font-weight:bold;
}

.good-stock{
    color:#22c55e;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------
# HERO
# ---------------------------------

st.markdown("""
<div class="hero">
<h1>📊 Admin Dashboard</h1>
<p>Monitor inventory, stock levels and product performance.</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------
# FETCH DATA
# ---------------------------------

try:

    response = requests.get(
        "http://127.0.0.1:8000/products/"
    )

    products = response.json()

except:

    st.error(
        "Backend Not Running"
    )

    st.stop()

# ---------------------------------
# CALCULATIONS
# ---------------------------------

total_products = len(products)

total_stock = sum(
    p["quantity"]
    for p in products
)

total_sold = sum(
    p.get("sold", 0)
    for p in products
)

low_stock_count = len(
    [
        p
        for p in products
        if p["quantity"] <= 5
    ]
)

# ---------------------------------
# KPI CARDS
# ---------------------------------

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="metric-card">
    <div class="metric-title">Products</div>
    <div class="metric-value">{total_products}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card">
    <div class="metric-title">Inventory Stock</div>
    <div class="metric-value">{total_stock}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card">
    <div class="metric-title">Products Sold</div>
    <div class="metric-value">{total_sold}</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="metric-card">
    <div class="metric-title">Low Stock</div>
    <div class="metric-value">{low_stock_count}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------
# INVENTORY MANAGEMENT
# ---------------------------------

st.subheader("📦 Inventory Management")

for product in products:

    left,right = st.columns([8,1])

    stock_status = (
        "🔴 Low Stock"
        if product["quantity"] <= 5
        else "🟢 In Stock"
    )

    with left:

        st.markdown(f"""
        <div class="product-card">

        <b>{product['name']}</b>

        <br>

        Category:
        {product['category']}

        <br>

        Price:
        ₹ {product['price']}

        <br>

        Quantity:
        {product['quantity']}

        <br>

        Status:
        {stock_status}

        </div>
        """, unsafe_allow_html=True)

    with right:

        if st.button(
            "🗑",
            key=f"delete_{product['id']}"
        ):

            requests.delete(
                f"http://127.0.0.1:8000/products/delete/{product['id']}"
            )

            st.success(
                "Product Deleted"
            )

            st.rerun()

# ---------------------------------
# TABLE
# ---------------------------------

st.markdown("---")

st.subheader("📋 Product Records")

df = pd.DataFrame(products)

if len(df) > 0:

    show_columns = [
        "id",
        "name",
        "category",
        "price",
        "quantity",
        "sold"
    ]

    available_columns = [
        c
        for c in show_columns
        if c in df.columns
    ]

    st.dataframe(
        df[available_columns],
        use_container_width=True
    )

else:

    st.warning(
        "No Products Found"
    )