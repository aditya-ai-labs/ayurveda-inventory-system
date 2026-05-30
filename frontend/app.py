import streamlit as st

st.set_page_config(
    page_title="Ayurvedic Inventory System",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

.main{
    background:#06121f;
}

.hero{
    background:
    linear-gradient(
    rgba(0,0,0,.55),
    rgba(0,0,0,.55)
    ),
    url("https://images.unsplash.com/photo-1515377905703-c4788e51af15");

    background-size:cover;
    background-position:center;

    border-radius:25px;

    padding:80px 60px;

    margin-bottom:40px;

    box-shadow:
    0px 10px 30px rgba(0,0,0,.3);
}

.hero-title{
    color:white;
    font-size:65px;
    font-weight:800;
    line-height:1.2;
}

.hero-green{
    color:#5eea75;
}

.hero-sub{
    color:#e2e8f0;
    font-size:22px;
    margin-top:20px;
}

.stat-card{
    background:#0f172a;
    border:1px solid #1e293b;
    border-radius:20px;
    padding:25px;
    text-align:center;
}

.stat-number{
    color:#5eea75;
    font-size:35px;
    font-weight:bold;
}

.stat-title{
    color:white;
    font-size:18px;
}

.feature{
    background:#0f172a;
    border:1px solid #1e293b;
    border-radius:20px;
    padding:25px;
    text-align:center;
    height:170px;
}

.feature h3{
    color:#5eea75;
}

.feature p{
    color:#cbd5e1;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO SECTION
# -----------------------------

st.markdown("""

<div class="hero">

<div class="hero-title">

🌿 Ayurvedic
<span class="hero-green">
Inventory Management
</span>

</div>

<div class="hero-sub">

Manage Products • Track Stock • Monitor Inventory

</div>

</div>

""", unsafe_allow_html=True)

# -----------------------------
# STATS
# -----------------------------

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">120+</div>
        <div class="stat-title">Products</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">12</div>
        <div class="stat-title">Categories</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">2500+</div>
        <div class="stat-title">Stock Units</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">25+</div>
        <div class="stat-title">Suppliers</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("## 🌿 Platform Features")

f1,f2,f3,f4 = st.columns(4)

with f1:
    st.markdown("""
    <div class="feature">
    <h3>📦 Inventory</h3>
    <p>Track products and stock in real time.</p>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature">
    <h3>🛒 Buy & Sell</h3>
    <p>Add and manage Ayurvedic products.</p>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature">
    <h3>📊 Dashboard</h3>
    <p>View inventory and business insights.</p>
    </div>
    """, unsafe_allow_html=True)

with f4:
    st.markdown("""
    <div class="feature">
    <h3>🌿 Ayurveda</h3>
    <p>Focused on herbal and wellness products.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.info(
    "Use the sidebar to manage products, inventory and administration."
)