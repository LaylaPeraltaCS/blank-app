import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import (
    load_css, render_nav, render_footer,
    PRODUCTS, render_product_card,
    add_to_cart, init_cart,
)

st.set_page_config(
    page_title="Thee Bee Boutique | Pure Handmade Natural Soaps",
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
    <div class="hero-badge">🐝 &nbsp;Pure · Handmade · Natural</div>
    <h1 class="hero-headline">Your skin deserves<br>the <em>real thing.</em></h1>
    <p class="hero-sub">
      Thee Bee Boutique crafts handmade natural soaps free of parabens,
      aluminum, and phthalates — because your skin deserves better than chemicals.
    </p>
    <div class="hero-pills">
      <span class="hero-pill">✅ Paraben-Free</span>
      <span class="hero-pill">✅ Aluminum-Free</span>
      <span class="hero-pill">✅ Phthalate-Free</span>
      <span class="hero-pill">✅ Sensitive Skin Friendly</span>
      <span class="hero-pill">✅ Organic Ingredients</span>
    </div>
    <div class="hero-cta-row">
      <a href="/Shop" target="_self" class="btn-honey">Shop Now &nbsp;→</a>
      <a href="/About" target="_self" class="btn-ghost">Our Story</a>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ── SCENT MARQUEE ────────────────────────────────────────────────
items = [
    "🍷 Black Cherry Merlot", "🐝 Bee Loved", "💌 Love Letter",
    "👑 Be Still Queen", "🍊 Orange Turmeric", "☕ Brewski",
    "🍎 Apple & Spice", "🥃 Vanilla Bourbon", "🍹 Sangria Bar",
    "🎃 Pumpkin Spice", "❄️ Vanilla Snowflake", "💜 Lavender Unwind",
    "🍯 Honey Almond",
]
track = "".join(
    f'<span class="scent-item">{x}</span><span class="scent-dot">&nbsp;·&nbsp;</span>'
    for x in items
) * 2
st.markdown(
    f'<div class="scent-strip"><div class="scent-track">{track}</div></div>',
    unsafe_allow_html=True,
)

# ── FEATURED PRODUCTS ────────────────────────────────────────────
st.markdown("""
<div class="section section-center">
  <div class="section-tag">🍯 The Collection</div>
  <h2 class="section-title">Customer <em>Favorites</em></h2>
  <div class="honey-rule"></div>
  <p class="section-sub">
    Every bar is handmade in small batches with organic ingredients —
    no fillers, no shortcuts, just real soap for real skin.
  </p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div style="max-width:1200px;margin:0 auto;padding:0 3rem 1rem;">', unsafe_allow_html=True)

# Show 4 featured products: Black Cherry Merlot, Bee Loved, Be Still Queen, Orange Turmeric
featured_ids = [1, 2, 4, 6]
featured = [p for p in PRODUCTS if p["id"] in featured_ids]

cols = st.columns(4)
for i, product in enumerate(featured):
    with cols[i]:
        render_product_card(product)
        if st.button(f"🛒 Add to Cart", key=f"home_{product['id']}"):
            add_to_cart(product["id"])
            st.toast(f"'{product['name']}' added to cart!", icon="🐝")

st.markdown("</div>", unsafe_allow_html=True)

_, mid, _ = st.columns([3, 1, 3])
with mid:
    st.markdown('<div style="text-align:center;padding:1rem 0 3.5rem;">', unsafe_allow_html=True)
    if st.button("View All Soaps  →", key="view_all_home"):
        st.switch_page("pages/Shop.py")
    st.markdown("</div>", unsafe_allow_html=True)

# ── BRAND PROMISE STRIP ──────────────────────────────────────────
st.markdown("""
<div style="background:#FAF5EE;border-top:1px solid #E8D0C0;border-bottom:1px solid #E8D0C0;padding:2.5rem 4rem;">
  <div style="max-width:1100px;margin:0 auto;display:grid;grid-template-columns:repeat(4,1fr);gap:2rem;text-align:center;">
    <div>
      <div style="font-size:2rem;margin-bottom:0.5rem;">🚫</div>
      <div style="font-family:'Cormorant Garamond',serif;font-size:1rem;font-weight:600;color:#1A0808;margin-bottom:0.3rem;">No Parabens</div>
      <div style="font-size:0.8rem;color:#6B3030;">Ever. Not even a little.</div>
    </div>
    <div>
      <div style="font-size:2rem;margin-bottom:0.5rem;">🚫</div>
      <div style="font-family:'Cormorant Garamond',serif;font-size:1rem;font-weight:600;color:#1A0808;margin-bottom:0.3rem;">No Aluminum</div>
      <div style="font-size:0.8rem;color:#6B3030;">Clean formula, always.</div>
    </div>
    <div>
      <div style="font-size:2rem;margin-bottom:0.5rem;">🚫</div>
      <div style="font-family:'Cormorant Garamond',serif;font-size:1rem;font-weight:600;color:#1A0808;margin-bottom:0.3rem;">No Phthalates</div>
      <div style="font-size:0.8rem;color:#6B3030;">Because you deserve better.</div>
    </div>
    <div>
      <div style="font-size:2rem;margin-bottom:0.5rem;">✅</div>
      <div style="font-family:'Cormorant Garamond',serif;font-size:1rem;font-weight:600;color:#1A0808;margin-bottom:0.3rem;">Sensitive Skin Safe</div>
      <div style="font-size:0.8rem;color:#6B3030;">Gentle for every skin type.</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── BRAND STORY SPLIT ────────────────────────────────────────────
story_l, story_r = st.columns([1, 1], gap="large")
with story_l:
    st.markdown("""
<div style="padding:5rem 2rem 5rem 4rem;">
  <div class="section-tag">🌿 Pure by Design</div>
  <h2 class="section-title">Made with <em>intention,</em><br>not shortcuts.</h2>
  <div class="honey-rule"></div>
  <p style="font-size:0.96rem;color:#6B3030;line-height:1.82;margin-bottom:1.5rem;">
    Thee Bee Boutique was born from a passion for sustainability and a deep
    belief that your skincare routine shouldn't come with a list of chemicals
    you can't pronounce.
  </p>
  <p style="font-size:0.96rem;color:#6B3030;line-height:1.82;margin-bottom:2rem;">
    Every bar is handcrafted with organic ingredients, made in small batches
    so nothing sits on a shelf too long. Real soap. Real results.
    Real love for your skin.
  </p>
  <a href="/About" target="_self" class="btn-honey" style="text-decoration:none;">Read Our Story  →</a>
</div>
""", unsafe_allow_html=True)

with story_r:
    st.markdown("""
<div style="padding:5rem 4rem 5rem 2rem;">
  <div class="story-img">
    <img src="https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?auto=format&fit=crop&w=700&q=80"
         alt="Handmade soap making" loading="lazy">
  </div>
</div>
""", unsafe_allow_html=True)

# ── WHY CHOOSE US ────────────────────────────────────────────────
st.markdown("""
<div class="why-band">
  <div style="max-width:1100px;margin:0 auto;">
    <div class="section-center" style="margin-bottom:3.5rem;">
      <div class="section-tag">✨ The Difference</div>
      <h2 class="section-title">Why the hive <em>loves</em> us</h2>
      <div class="honey-rule"></div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1.5rem;">
      <div class="why-card">
        <span class="why-icon">🧴</span>
        <div class="why-title">Pure Ingredients</div>
        <p class="why-text">Organic oils, butters, and botanical extracts. Nothing artificial, nothing harmful. What's on the label is everything that's in the bar.</p>
      </div>
      <div class="why-card">
        <span class="why-icon">✋</span>
        <div class="why-title">Truly Handmade</div>
        <p class="why-text">Every bar is hand-poured and hand-cut in small batches. No mass production. Your soap was made by real hands with real care.</p>
      </div>
      <div class="why-card">
        <span class="why-icon">🌱</span>
        <div class="why-title">Sustainability First</div>
        <p class="why-text">From ingredient sourcing to packaging, we make choices that are good for your skin and for the planet. Because both matter.</p>
      </div>
      <div class="why-card">
        <span class="why-icon">💛</span>
        <div class="why-title">Black Woman Owned</div>
        <p class="why-text">Thee Bee Boutique is proudly Black woman-owned and operated. Every purchase directly supports an independent maker and her community.</p>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── TESTIMONIALS ─────────────────────────────────────────────────
st.markdown("""
<div class="testimonial-band">
  <div class="section section-center">
    <div class="section-tag">💛 The Hive Speaks</div>
    <h2 class="section-title">Real results, real <em>people</em></h2>
    <div class="honey-rule"></div>
  </div>
</div>
""", unsafe_allow_html=True)

testimonials = [
    {
        "text": "The Black Cherry Merlot is everything. My husband keeps stealing it out of the shower. I've had to start ordering two at a time just to keep one for myself!",
        "name": "Keisha W.",
        "loc": "Houston, TX",
        "init": "K",
        "product": "Black Cherry Merlot",
    },
    {
        "text": "I have super sensitive skin and have been dealing with reactions to store soaps for years. Bee Loved is the ONLY soap I can use without breaking out. I'm never going back.",
        "name": "Tamara J.",
        "loc": "Atlanta, GA",
        "init": "T",
        "product": "Bee Loved",
    },
    {
        "text": "Be Still Queen is my self-care ritual now. Something about the scent just makes me feel grounded. Ordered 6 bars and gave 3 away as gifts. Everyone asked where I got them.",
        "name": "Monique R.",
        "loc": "Chicago, IL",
        "init": "M",
        "product": "Be Still Queen",
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
      <div class="t-loc">{t['loc']} · <em>{t['product']}</em></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ── NEWSLETTER ───────────────────────────────────────────────────
st.markdown("""
<div class="newsletter-band">
  <div style="max-width:580px;margin:0 auto;">
    <div class="section-tag" style="color:rgba(255,255,255,0.65);">🐝 Stay in the Hive</div>
    <h2 class="section-title">New scents drop <em>first</em> here</h2>
    <div class="honey-rule"></div>
    <p class="section-sub">Join the hive for exclusive drops, restocks, and 10% off your first order.</p>
  </div>
</div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div style="background:linear-gradient(135deg,#8B1A2C,#C9922A);padding:0 4rem 4.5rem;">', unsafe_allow_html=True)
    _, center, _ = st.columns([1, 2, 1])
    with center:
        with st.form("newsletter_form", clear_on_submit=True):
            email = st.text_input("", placeholder="Enter your email address…")
            sub = st.form_submit_button("🐝  Join the Hive — It's Free")
            if sub and email:
                st.success("You're in! Check your inbox for your 10% off code. 🍯")
            elif sub:
                st.warning("Please enter your email address.")
    st.markdown("</div>", unsafe_allow_html=True)

render_footer()
