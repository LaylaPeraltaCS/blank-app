import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import (
    load_css, render_nav, render_footer,
    PRODUCTS, render_product_card,
    add_to_cart, init_cart,
)

st.set_page_config(
    page_title="Shop | Thee Bee Boutique",
    page_icon="🐝",
    layout="wide",
    initial_sidebar_state="collapsed",
)

init_cart()
load_css()
render_nav()

# ── PAGE HEADER ──────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
  <div class="page-header-tag">🍯 Handcrafted · Small Batch · All Natural</div>
  <h1 class="page-header-title">The <em>Hive</em> Collection</h1>
  <p class="page-header-sub">Every bar made with raw honey, botanical oils, and a whole lot of love.</p>
</div>
""", unsafe_allow_html=True)

# ── FILTERS + GRID ───────────────────────────────────────────────
st.markdown('<div style="max-width:1340px;margin:0 auto;padding:3rem 3rem 5rem;">', unsafe_allow_html=True)

filter_col, grid_col = st.columns([1, 3.5], gap="large")

with filter_col:
    st.markdown('<div class="filter-panel">', unsafe_allow_html=True)
    st.markdown('<div class="filter-title">🔍 &nbsp;Filter Soaps</div>', unsafe_allow_html=True)

    scent_options = ["All Scents", "Sweet", "Floral", "Citrus", "Fresh"]
    selected_scent = st.radio("Scent Family", scent_options, index=0)

    st.markdown('<div style="margin-top:1.5rem;"></div>', unsafe_allow_html=True)

    skin_options = ["All Skin Types", "Sensitive", "Dry", "Oily", "Normal", "Acne-Prone"]
    selected_skin = st.radio("Skin Type", skin_options, index=0)

    st.markdown('<div style="margin-top:1.5rem;"></div>', unsafe_allow_html=True)
    max_price = st.slider("Max Price", min_value=8, max_value=20, value=20, step=1, format="$%d")

    st.markdown('<div style="margin-top:1.5rem;"></div>', unsafe_allow_html=True)
    sort_by = st.selectbox("Sort By", ["Featured", "Price: Low to High", "Price: High to Low", "Top Rated"])

    st.markdown("</div>", unsafe_allow_html=True)

with grid_col:
    # Filter products
    filtered = PRODUCTS.copy()

    if selected_scent != "All Scents":
        filtered = [p for p in filtered if p["scent_family"] == selected_scent]

    if selected_skin != "All Skin Types":
        filtered = [p for p in filtered if selected_skin in p["skin_types"]]

    filtered = [p for p in filtered if p["price"] <= max_price]

    if sort_by == "Price: Low to High":
        filtered.sort(key=lambda p: p["price"])
    elif sort_by == "Price: High to Low":
        filtered.sort(key=lambda p: p["price"], reverse=True)
    elif sort_by == "Top Rated":
        filtered.sort(key=lambda p: p["rating"], reverse=True)

    count_label = f"{len(filtered)} product{'s' if len(filtered) != 1 else ''} found"
    st.markdown(
        f'<p style="font-size:0.85rem;color:#8B5E3C;margin-bottom:1.5rem;font-weight:500;">{count_label}</p>',
        unsafe_allow_html=True,
    )

    if not filtered:
        st.markdown("""
<div style="text-align:center;padding:4rem 2rem;color:#8B5E3C;">
  <span style="font-size:3rem;display:block;margin-bottom:1rem;">🍯</span>
  <h3 style="font-family:'Playfair Display',serif;color:#2C1A0E;margin-bottom:0.6rem;">No soaps match these filters</h3>
  <p style="font-size:0.9rem;">Try adjusting your filters to discover more of the hive.</p>
</div>
""", unsafe_allow_html=True)
    else:
        rows = [filtered[i:i+3] for i in range(0, len(filtered), 3)]
        for row in rows:
            cols = st.columns(3)
            for j, product in enumerate(row):
                with cols[j]:
                    render_product_card(product)

                    # Expandable detail
                    with st.expander("View Details"):
                        st.markdown(f"""
<div style="font-size:0.88rem;color:#6B4226;line-height:1.72;margin-bottom:1rem;">
  {product['description']}
</div>
<div style="margin-bottom:0.6rem;">
  <strong style="font-size:0.8rem;color:#2C1A0E;letter-spacing:0.05em;text-transform:uppercase;">Skin Types</strong><br>
  {"".join(f'<span class="skin-chip">{s}</span>' for s in product['skin_types'])}
</div>
<div style="margin-top:0.8rem;">
  <strong style="font-size:0.8rem;color:#2C1A0E;letter-spacing:0.05em;text-transform:uppercase;">Ingredients</strong><br>
  {"".join(f'<span class="ingredient-chip">{ing}</span>' for ing in product['ingredients'])}
</div>
<div style="margin-top:0.8rem;font-size:0.8rem;color:#8B5E3C;">
  Weight: <strong>{product['weight']}</strong>
</div>
""", unsafe_allow_html=True)

                    if st.button("🛒  Add to Cart", key=f"shop_{product['id']}"):
                        add_to_cart(product["id"])
                        st.toast(f"'{product['name']}' added to cart!", icon="🐝")

            st.markdown('<div style="height:0.5rem;"></div>', unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ── BOTTOM BANNER ────────────────────────────────────────────────
st.markdown("""
<div style="background:#F5E8CC;padding:3.5rem 4rem;text-align:center;border-top:1px solid #E8D5B0;">
  <div class="section-tag">🐝 Bee-Powered Promise</div>
  <h3 style="font-family:'Playfair Display',serif;font-size:1.6rem;color:#2C1A0E;margin:0.5rem 0 0.8rem;">
    Not happy? We'll make it right.
  </h3>
  <p style="font-size:0.9rem;color:#6B4226;max-width:520px;margin:0 auto;line-height:1.72;">
    Every order comes with our 30-day happiness guarantee.
    If your skin isn't glowing, contact us and we'll replace your bar or refund you — no questions asked.
  </p>
</div>
""", unsafe_allow_html=True)

render_footer()
