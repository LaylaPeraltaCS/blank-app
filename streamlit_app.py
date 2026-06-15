import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import (
    load_css, render_nav, render_footer,
    PRODUCTS, render_product_card,
    add_to_cart, init_cart,
)

st.set_page_config(
    page_title="Thee Bee Boutique | Handmade Soaps",
    page_icon="🐝",
    layout="wide",
    initial_sidebar_state="collapsed",
)

init_cart()
load_css()
render_nav()

# ── HERO ────────────────────────────────────────────────────────
st.markdown("""
<section class="bee-hero">
  <div class="hero-inner">
    <div class="hero-badge">🐝 &nbsp;Small Batch · All Natural · Handcrafted</div>
    <h1 class="hero-headline">Skin that <em>glows,</em><br>naturally.</h1>
    <p class="hero-sub">
      Thee Bee Boutique crafts luxurious handmade soaps using raw honey,
      beeswax, and botanical ingredients your skin will truly love.
    </p>
    <div class="hero-cta-row">
      <a href="/Shop" target="_self" class="btn-honey">Shop the Hive &nbsp;→</a>
      <a href="/About" target="_self" class="btn-ghost">Our Story</a>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ── SCENT MARQUEE ────────────────────────────────────────────────
items = [
    "🍯 Raw Honey", "🌸 French Lavender", "🍊 Citrus Blends",
    "🌿 Botanicals", "🥥 Coconut Milk", "🌹 Rose Absolute",
    "✨ Beeswax", "🫐 Oatmeal & Shea", "🌿 Tea Tree", "🍦 Vanilla Bean",
]
track = "".join(
    f'<span class="scent-item">{x}</span><span class="scent-dot"> · </span>'
    for x in items
) * 2
st.markdown(
    f'<div class="scent-strip"><div class="scent-track">{track}</div></div>',
    unsafe_allow_html=True,
)

# ── FEATURED PRODUCTS ────────────────────────────────────────────
st.markdown("""
<div class="section section-center">
  <div class="section-tag">🍯 The Honey Collection</div>
  <h2 class="section-title">Our <em>Bestselling</em> Bars</h2>
  <div class="honey-rule"></div>
  <p class="section-sub">
    Each bar is made in small batches and cold-process cured for 4–6 weeks
    for the richest lather and gentlest cleanse.
  </p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div style="max-width:1200px;margin:0 auto;padding:0 3rem 1rem;">', unsafe_allow_html=True)
featured = PRODUCTS[:3]
cols = st.columns(3)
for i, product in enumerate(featured):
    with cols[i]:
        render_product_card(product)
        if st.button(f"🛒  Add to Cart", key=f"home_{product['id']}"):
            add_to_cart(product["id"])
            st.toast(f"'{product['name']}' added to cart!", icon="🐝")

st.markdown("</div>", unsafe_allow_html=True)

_, mid, _ = st.columns([3, 1, 3])
with mid:
    st.markdown('<div style="text-align:center;padding:0.5rem 0 3rem;">', unsafe_allow_html=True)
    if st.button("View All Soaps  →", key="view_all_home"):
        st.switch_page("pages/Shop.py")
    st.markdown("</div>", unsafe_allow_html=True)

# ── BRAND STORY SPLIT ────────────────────────────────────────────
st.markdown("""
<div style="max-width:1200px;margin:0 auto;padding:0 3rem;">
  <hr style="border:none;border-top:1px solid #E8D5B0;margin:0 0 4rem;">
</div>
""", unsafe_allow_html=True)

story_l, story_r = st.columns([1, 1], gap="large")
with story_l:
    st.markdown("""
<div style="padding:2rem 2rem 2rem 3rem;">
  <div class="section-tag">🌿 The Story</div>
  <h2 class="section-title">Made with <em>intention,</em><br>not shortcuts.</h2>
  <div class="honey-rule"></div>
  <p style="font-size:0.96rem;color:#6B4226;line-height:1.78;margin-bottom:1.5rem;">
    Thee Bee Boutique began in a small kitchen with one goal: create a soap
    that was truly good for the skin — no sulfates, no synthetic fragrances,
    no compromises. Just raw honey, beeswax, and botanicals that actually work.
  </p>
  <p style="font-size:0.96rem;color:#6B4226;line-height:1.78;margin-bottom:2rem;">
    Every bar is hand-poured in small batches, cured for weeks, and wrapped
    with love. Because your skin deserves the real thing.
  </p>
  <a href="/About" target="_self" class="btn-honey" style="text-decoration:none;">Meet the Maker  →</a>
</div>
""", unsafe_allow_html=True)

with story_r:
    st.markdown("""
<div style="padding:2rem 3rem 2rem 2rem;">
  <div class="story-img">
    <img src="https://images.unsplash.com/photo-1576426863848-c21f53c60b19?auto=format&fit=crop&w=700&q=80"
         alt="Artisan soap making" loading="lazy">
  </div>
</div>
""", unsafe_allow_html=True)

# ── WHY CHOOSE US ────────────────────────────────────────────────
st.markdown("""
<div class="why-band">
  <div style="max-width:1200px;margin:0 auto;">
    <div class="section-center" style="margin-bottom:3.5rem;">
      <div class="section-tag">✨ Why We're Different</div>
      <h2 class="section-title">Crafted with <em>care</em> in every bar</h2>
      <div class="honey-rule"></div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1.5rem;">
      <div class="why-card">
        <span class="why-icon">🍯</span>
        <div class="why-title">Raw Honey Infused</div>
        <p class="why-text">We source raw wildflower honey directly from local beekeepers — packed with enzymes and antioxidants your skin craves.</p>
      </div>
      <div class="why-card">
        <span class="why-icon">🌿</span>
        <div class="why-title">100% Natural</div>
        <p class="why-text">No SLS, no parabens, no synthetic dyes. Just skin-loving oils, butters, and plant botanicals — full stop.</p>
      </div>
      <div class="why-card">
        <span class="why-icon">✋</span>
        <div class="why-title">Small Batch Handmade</div>
        <p class="why-text">We make 5–12 bars at a time using traditional cold-process methods. Quality you can see, smell, and feel.</p>
      </div>
      <div class="why-card">
        <span class="why-icon">🐝</span>
        <div class="why-title">Cruelty Free</div>
        <p class="why-text">Every formula is vegan-friendly and never tested on animals. Good for you, good for the planet, good for the bees.</p>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── TESTIMONIALS ─────────────────────────────────────────────────
st.markdown("""
<div class="testimonial-band">
  <div class="section section-center">
    <div class="section-tag">💛 Happy Hive</div>
    <h2 class="section-title">What our <em>customers</em> are saying</h2>
    <div class="honey-rule"></div>
  </div>
</div>
""", unsafe_allow_html=True)

t_cols = st.columns(3)
testimonials = [
    {
        "text": "I've tried so many natural soaps and nothing compares. The Golden Honey Oat Bar cleared up my dry patches in two weeks. My skin feels unbelievably soft.",
        "name": "Jasmine T.",
        "loc": "Atlanta, GA",
        "init": "J",
    },
    {
        "text": "The Lavender Beeswax Dream smells divine and my skin looks incredible. I've been sleeping so much better since I started using it at night. Absolute magic.",
        "name": "Renée M.",
        "loc": "New Orleans, LA",
        "init": "R",
    },
    {
        "text": "I ordered a gift set for my mom and she cried — in a good way! The packaging is gorgeous and the soaps last forever. We're both hooked. Won't buy from anywhere else.",
        "name": "Destiny K.",
        "loc": "Houston, TX",
        "init": "D",
    },
]

with st.container():
    st.markdown('<div style="max-width:1200px;margin:0 auto;padding:0 3rem 5rem;">', unsafe_allow_html=True)
    t3 = st.columns(3)
    for i, t in enumerate(testimonials):
        with t3[i]:
            st.markdown(f"""
<div class="testimonial-card">
  <div class="testimonial-stars">★★★★★</div>
  <p class="testimonial-text">"{t['text']}"</p>
  <div class="testimonial-author">
    <div class="t-avatar">{t['init']}</div>
    <div>
      <div class="t-name">{t['name']}</div>
      <div class="t-loc">{t['loc']}</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ── NEWSLETTER ───────────────────────────────────────────────────
st.markdown("""
<div class="newsletter-band">
  <div style="max-width:600px;margin:0 auto;">
    <div class="section-tag" style="color:rgba(255,255,255,0.7);">🐝 Stay in the Hive</div>
    <h2 class="section-title">Get <em>first access</em> to new drops</h2>
    <div class="honey-rule"></div>
    <p class="section-sub">Join our community for exclusive scents, restocks, and 10% off your first order.</p>
  </div>
</div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div style="background:#C9922A;padding:0 4rem 4rem;">', unsafe_allow_html=True)
    _, center, _ = st.columns([1, 2, 1])
    with center:
        with st.form("newsletter_form", clear_on_submit=True):
            email = st.text_input("", placeholder="Enter your email address…")
            submitted = st.form_submit_button("🐝  Subscribe — It's Free")
            if submitted and email:
                st.success("You're in the hive! Check your inbox for your 10% off code. 🍯")
            elif submitted:
                st.warning("Please enter your email address.")
    st.markdown("</div>", unsafe_allow_html=True)

render_footer()
