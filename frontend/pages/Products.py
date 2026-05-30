import streamlit as st
import requests

st.set_page_config(
    page_title="Products",
    layout="wide"
)

# ---------------------
# CSS
# ---------------------

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
    margin-bottom:25px;
}

.product-card{
    background:#0f172a;
    padding:15px;
    border-radius:20px;
    border:1px solid #1e293b;
    margin-bottom:25px;
}

.product-name{
    color:white;
    font-size:22px;
    font-weight:bold;
}

.product-category{
    color:#4ade80;
    font-weight:600;
}

.price{
    color:#facc15;
    font-size:22px;
    font-weight:bold;
}

.stock{
    color:#cbd5e1;
}

.stButton button{
    background:#16a34a !important;
    color:white !important;
    border:none !important;
    border-radius:10px !important;
    width:100%;
    height:45px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------
# HERO
# ---------------------

st.markdown("""
<div class="hero">
<h1>🌿 Ayurvedic Product Store</h1>
<p>Browse and purchase Ayurvedic wellness products.</p>
</div>
""", unsafe_allow_html=True)

# ---------------------
# FILTERS
# ---------------------

c1, c2 = st.columns([3,1])

with c1:
    search = st.text_input(
        "🔍 Search Product"
    )

with c2:
    selected_category = st.selectbox(
        "Category",
        [
            "All",
            "Powder",
            "Tablet",
            "Juice",
            "Oil",
            "Capsule",
            "Personal Care"
        ]
    )

# ---------------------
# API
# ---------------------

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

# ---------------------
# FILTER
# ---------------------

filtered_products = []

for product in products:

    search_match = (
        search.lower()
        in product["name"].lower()
    )

    category_match = (
        selected_category == "All"
        or product["category"] == selected_category
    )

    if search_match and category_match:
        filtered_products.append(product)

# ---------------------
# PRODUCT GRID
# ---------------------

if len(filtered_products) == 0:

    st.warning(
        "No Products Found"
    )

else:

    cols = st.columns(3)

    for index, product in enumerate(filtered_products):

        with cols[index % 3]:

            image = product.get("image")

            if not image:

                image = (
                    "https://images.unsplash.com/"
                    "photo-1505751172876-fa1923c5c528"
                )

            st.image(
                image,
                use_container_width=True
            )

            st.markdown(
                f"""
                <div class="product-card">

                <div class="product-name">
                {product['name']}
                </div>

                <div class="product-category">
                🌿 {product['category']}
                </div>

                <br>

                <div class="price">
                ₹ {product['price']}
                </div>

                <div class="stock">
                📦 Stock : {product['quantity']}
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            buy = st.button(
                f"🛒 Buy Now",
                key=f"buy_{product['id']}"
            )

            if buy:

                response = requests.put(
                    f"http://127.0.0.1:8000/products/buy/{product['id']}"
                )

                result = response.json()

                st.success(
                    result["message"]
                )

                st.rerun()