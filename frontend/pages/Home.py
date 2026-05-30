import streamlit as st

st.set_page_config(
    page_title="Ayurvedic Inventory",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color:#07111f;
}

.hero-container{
    position:relative;
    border-radius:25px;
    overflow:hidden;
    height:500px;
}

.hero-image{
    width:100%;
    height:500px;
    object-fit:cover;
    border-radius:25px;
}

.overlay{
    position:absolute;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background:rgba(0,0,0,0.55);
}

.hero-content{
    position:absolute;
    top:50%;
    left:5%;
    transform:translateY(-50%);
    color:white;
}

.hero-title{
    font-size:60px;
    font-weight:700;
    color:white;
}

.hero-green{
    color:#67e567;
}

.hero-subtitle{
    font-size:24px;
    color:#d4d4d4;
    margin-top:15px;
}

.metric-card{
    background:rgba(255,255,255,0.05);
    padding:25px;
    border-radius:20px;
    text-align:center;
    backdrop-filter: blur(8px);
    border:1px solid rgba(255,255,255,0.1);
}

.metric-title{
    color:#8eff8e;
    font-size:18px;
}

.metric-value{
    font-size:38px;
    color:white;
    font-weight:bold;
}

.section-title{
    color:white;
    font-size:35px;
    font-weight:700;
    margin-top:40px;
}

.feature-card{
    background:#0d1b2a;
    padding:20px;
    border-radius:20px;
    text-align:center;
    border:1px solid #1e293b;
}

.feature-card h3{
    color:#7CFC00;
}

.feature-card p{
    color:#d1d5db;
}

</style>
""", unsafe_allow_html=True)

# Hero Section

st.markdown("""
<div class="hero-container">

<img
class="hero-image"
src="https://images.unsplash.com/photo-1515377905703-c4788e51af15"
/>

<div class="overlay"></div>

<div class="hero-content">

<div class="hero-title">
Ayurvedic <span class="hero-green">Inventory Management</span>
</div>

<div class="hero-subtitle">
Manage products, track inventory and grow your Ayurvedic business.
</div>

</div>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Stats

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-title">Products</div>
    <div class="metric-value">120+</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-title">Categories</div>
    <div class="metric-value">12</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-title">Stock</div>
    <div class="metric-value">2500+</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-title">Suppliers</div>
    <div class="metric-value">25+</div>
    </div>
    """, unsafe_allow_html=True)

# Features

st.markdown(
    '<div class="section-title">Why Choose Us?</div>',
    unsafe_allow_html=True
)

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card">
    <h3>🌿 Natural</h3>
    <p>100% Ayurvedic Products</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
    <h3>🛡 Quality</h3>
    <p>Quality Assured Inventory</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
    <h3>📦 Stock</h3>
    <p>Inventory Tracking</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
    <h3>🚚 Delivery</h3>
    <p>Supplier Management</p>
    </div>
    """, unsafe_allow_html=True)