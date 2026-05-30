import streamlit as st
import requests

st.set_page_config(
    page_title="Sell Product",
    layout="wide"
)

# ----------------------------
# CSS
# ----------------------------

st.markdown("""
<style>

.hero{
    background:linear-gradient(
    135deg,
    #166534,
    #22c55e
    );

    padding:35px;
    border-radius:20px;
    color:white;
    margin-bottom:30px;
}

.form-card{
    background:#0f172a;
    padding:25px;
    border-radius:20px;
    border:1px solid #1e293b;
}

.preview-card{
    background:#0f172a;
    padding:20px;
    border-radius:20px;
    border:1px solid #1e293b;
    text-align:center;
}

.preview-title{
    color:#4ade80;
    font-size:22px;
    font-weight:bold;
}

.stButton button{
    background:#16a34a !important;
    color:white !important;
    border:none !important;
    border-radius:10px !important;
    height:50px !important;
    width:100%;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# HERO SECTION
# ----------------------------

st.markdown("""
<div class="hero">
<h1>🌿 Sell Ayurvedic Product</h1>
<p>Add new products to your inventory and manage stock efficiently.</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# LAYOUT
# ----------------------------

left, right = st.columns([2,1])

# ----------------------------
# LEFT COLUMN
# ----------------------------

with left:

    st.markdown(
        '<div class="form-card">',
        unsafe_allow_html=True
    )

    name = st.text_input(
        "📦 Product Name"
    )

    category = st.selectbox(
        "🌿 Category",
        [
            "Powder",
            "Tablet",
            "Juice",
            "Oil",
            "Capsule",
            "Chyawanprash",
            "Personal Care"
        ]
    )

    col1, col2 = st.columns(2)

    with col1:
        price = st.number_input(
            "💰 Price (₹)",
            min_value=0.0
        )

    with col2:
        quantity = st.number_input(
            "📦 Quantity",
            min_value=1
        )

    image = st.text_input(
        "🖼 Product Image URL"
    )

    add_product = st.button(
        "➕ Add Product"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

# ----------------------------
# RIGHT COLUMN
# ----------------------------

with right:

    st.markdown("""
    <div class="preview-card">
    <div class="preview-title">
    Product Preview
    </div>
    </div>
    """, unsafe_allow_html=True)

    if image:

        st.image(
            image,
            use_container_width=True
        )

    else:

        st.image(
            "https://images.unsplash.com/photo-1514733670139-4d87a1941d55?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8YXl1cnZlZGF8ZW58MHx8MHx8fDA%3D",
            use_container_width=True
        )

    st.markdown("### Product Information")

    st.write(f"**Name:** {name}")
    st.write(f"**Category:** {category}")
    st.write(f"**Price:** ₹ {price}")
    st.write(f"**Quantity:** {quantity}")

# ----------------------------
# ADD PRODUCT
# ----------------------------

if add_product:

    if not name:

        st.warning(
            "Please Enter Product Name"
        )

    else:

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
            "✅ Product Added Successfully"
        )

        st.balloons()