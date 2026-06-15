import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import load_css, render_nav, render_footer, init_cart

st.set_page_config(
    page_title="About | Thee Bee Boutique",
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
  <div class="page-header-tag">🌿 Our Story</div>
  <h1 class="page-header-title">Pure soap, made with <em>purpose.</em></h1>
  <p class="page-header-sub">A passion for sustainability. A commitment to clean. A love for every skin type.</p>
</div>
""", unsafe_allow_html=True)

# ── FOUNDER STORY ────────────────────────────────────────────────
st.markdown('<div style="max-width:1200px;margin:0 auto;">', unsafe_allow_html=True)

left, right = st.columns([1.1, 1], gap="large")

with left:
    st.markdown("""
<div style="padding:5rem 2rem 5rem 4rem;">
  <div class="section-tag">🐝 The Origin</div>
  <h2 class="section-title">Born from a passion<br>for <em>better</em> skincare.</h2>
  <div class="honey-rule"></div>
  <p style="font-size:0.96rem;color:#6B3030;line-height:1.85;margin-bottom:1.5rem;">
    Thee Bee Boutique was created with one mission: make skincare products
    that are truly clean. No parabens. No aluminum. No phthalates.
    Just pure, handmade soap with ingredients you can actually pronounce.
  </p>
  <p style="font-size:0.96rem;color:#6B3030;line-height:1.85;margin-bottom:1.5rem;">
    Our story centers on a deep dedication to sustainability and a belief that
    everyone deserves access to products that are both effective and safe —
    especially for sensitive skin.
  </p>
  <p style="font-size:0.96rem;color:#6B3030;line-height:1.85;margin-bottom:2.2rem;">
    Every bar is handcrafted in small batches because we believe quality can't
    be rushed. From the first pour to the final wrap, each soap is made with
    intention — and a whole lot of love.
  </p>
  <div style="display:flex;gap:2rem;flex-wrap:wrap;margin-bottom:2rem;">
    <div style="text-align:center;">
      <div style="font-family:'Cormorant Garamond',serif;font-size:2.5rem;font-weight:600;color:#C9922A;">13+</div>
      <div style="font-size:0.8rem;color:#6B3030;text-transform:uppercase;letter-spacing:0.1em;font-weight:600;">Unique Scents</div>
    </div>
    <div style="text-align:center;">
      <div style="font-family:'Cormorant Garamond',serif;font-size:2.5rem;font-weight:600;color:#C9922A;">100%</div>
      <div style="font-size:0.8rem;color:#6B3030;text-transform:uppercase;letter-spacing:0.1em;font-weight:600;">Natural Ingredients</div>
    </div>
    <div style="text-align:center;">
      <div style="font-family:'Cormorant Garamond',serif;font-size:2.5rem;font-weight:600;color:#C9922A;">0</div>
      <div style="font-size:0.8rem;color:#6B3030;text-transform:uppercase;letter-spacing:0.1em;font-weight:600;">Harmful Chemicals</div>
    </div>
  </div>
  <a href="/Shop" target="_self" class="btn-honey" style="text-decoration:none;">Shop the Collection  →</a>
</div>
""", unsafe_allow_html=True)

with right:
    st.markdown("""
<div style="padding:5rem 4rem 5rem 2rem;">
  <div class="story-img">
    <img src="https://images.unsplash.com/photo-1576426863848-c21f53c60b19?auto=format&fit=crop&w=700&q=80"
         alt="Handmade soap making" loading="lazy">
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ── VALUES ───────────────────────────────────────────────────────
st.markdown("""
<div style="background:linear-gradient(135deg,#F5E0D0,#FAF5EE);padding:5.5rem 4rem;">
  <div style="max-width:1200px;margin:0 auto;">
    <div class="section-center" style="margin-bottom:3.5rem;">
      <div class="section-tag">💛 What Drives Us</div>
      <h2 class="section-title">Our values are <em>non-negotiable</em></h2>
      <div class="honey-rule"></div>
    </div>
</div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div style="background:linear-gradient(135deg,#F5E0D0,#FAF5EE);padding:0 4rem 5.5rem;">', unsafe_allow_html=True)
    st.markdown('<div style="max-width:1200px;margin:0 auto;">', unsafe_allow_html=True)

    v_cols = st.columns(4)
    values = [
        {
            "icon": "🚫",
            "title": "Truly Clean",
            "text": "Zero parabens. Zero aluminum. Zero phthalates. No compromises on what goes into our bars — ever. What's on the label is all that's in the soap.",
        },
        {
            "icon": "🌿",
            "title": "Organic Ingredients",
            "text": "We source organic oils, butters, and botanicals because your skin absorbs what you put on it. Every ingredient earns its place in our formula.",
        },
        {
            "icon": "♻️",
            "title": "Sustainability First",
            "text": "From how we source ingredients to how we package our products, we make choices that are good for your skin and for the planet.",
        },
        {
            "icon": "💛",
            "title": "Black Woman Owned",
            "text": "Thee Bee Boutique is proudly Black woman-owned and operated. Every purchase supports an independent maker and a community-driven business.",
        },
    ]
    for i, v in enumerate(values):
        with v_cols[i]:
            st.markdown(f"""
<div class="value-card">
  <span class="value-icon">{v['icon']}</span>
  <div class="value-title">{v['title']}</div>
  <p class="value-text">{v['text']}</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ── THE PROCESS ──────────────────────────────────────────────────
p_left, p_right = st.columns([1, 1], gap="large")

with p_left:
    st.markdown("""
<div style="padding:5rem 2rem 5rem 4rem;">
  <div class="section-tag">⚗️ Small Batch Craft</div>
  <h2 class="section-title">How your soap<br>comes to <em>life</em></h2>
  <div class="honey-rule"></div>
  <div class="process-step">
    <div class="step-num">1</div>
    <div class="step-body">
      <h4>Source Organic Ingredients</h4>
      <p>We carefully select organic oils, butters, and botanical extracts from trusted suppliers. Every ingredient is chosen for what it does for your skin, not for cost.</p>
    </div>
  </div>
  <div class="process-step">
    <div class="step-num">2</div>
    <div class="step-body">
      <h4>Handcraft in Small Batches</h4>
      <p>Using cold-process and hot-process methods, each bar is hand-mixed, hand-poured, and hand-cut. Small batches mean consistent quality and maximum freshness.</p>
    </div>
  </div>
  <div class="process-step">
    <div class="step-num">3</div>
    <div class="step-body">
      <h4>Cure & Inspect</h4>
      <p>Bars are cured to develop a harder, longer-lasting lather. Every single bar is inspected before it leaves our hands — because your skin deserves perfection.</p>
    </div>
  </div>
  <div class="process-step" style="margin-bottom:0;">
    <div class="step-num">4</div>
    <div class="step-body">
      <h4>Shipped to You with Love</h4>
      <p>Packaged sustainably and shipped within 2–3 business days. Because we know once you order, you're excited — and we are too.</p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

with p_right:
    st.markdown("""
<div style="padding:5rem 4rem 5rem 2rem;">
  <div class="story-img">
    <img src="https://images.unsplash.com/photo-1559715745-e1b33a271d2b?auto=format&fit=crop&w=700&q=80"
         alt="Soap ingredients" loading="lazy">
  </div>
</div>
""", unsafe_allow_html=True)

# ── INGREDIENTS SPOTLIGHT ─────────────────────────────────────────
st.markdown("""
<div style="background:#1A0808;padding:5.5rem 4rem;">
  <div style="max-width:1200px;margin:0 auto;">
    <div class="section-center" style="margin-bottom:3.5rem;">
      <div class="section-tag" style="color:rgba(240,192,96,0.7);">🌿 What's Inside</div>
      <h2 class="section-title" style="color:#FFF8EE;">Ingredients we <em>love</em></h2>
      <div class="honey-rule" style="margin:0.8rem auto 0;"></div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;">
      <div style="background:rgba(201,146,42,0.08);border:1px solid rgba(201,146,42,0.18);border-radius:18px;padding:2rem;">
        <div style="font-size:2.4rem;margin-bottom:0.8rem;">🫒</div>
        <div style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;font-weight:600;color:#F0C060;margin-bottom:0.6rem;">Organic Oils</div>
        <p style="font-size:0.85rem;color:rgba(255,248,238,0.6);line-height:1.72;margin:0;">
          Coconut, olive, castor, and safflower oils form the foundation of every bar. Rich, nourishing, and effective without clogging your pores.
        </p>
      </div>
      <div style="background:rgba(201,146,42,0.08);border:1px solid rgba(201,146,42,0.18);border-radius:18px;padding:2rem;">
        <div style="font-size:2.4rem;margin-bottom:0.8rem;">🧈</div>
        <div style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;font-weight:600;color:#F0C060;margin-bottom:0.6rem;">Shea & Cocoa Butter</div>
        <p style="font-size:0.85rem;color:rgba(255,248,238,0.6);line-height:1.72;margin:0;">
          Deep moisturizing butters that soften, soothe, and protect the skin barrier. Your skin drinks these in — no greasiness, just glow.
        </p>
      </div>
      <div style="background:rgba(201,146,42,0.08);border:1px solid rgba(201,146,42,0.18);border-radius:18px;padding:2rem;">
        <div style="font-size:2.4rem;margin-bottom:0.8rem;">🌿</div>
        <div style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;font-weight:600;color:#F0C060;margin-bottom:0.6rem;">Botanical Extracts</div>
        <p style="font-size:0.85rem;color:rgba(255,248,238,0.6);line-height:1.72;margin:0;">
          Real lavender buds, turmeric, coffee grounds, and more. Every botanical is chosen for a purpose — never just for looks.
        </p>
      </div>
      <div style="background:rgba(139,26,44,0.1);border:1px solid rgba(139,26,44,0.2);border-radius:18px;padding:2rem;">
        <div style="font-size:2.4rem;margin-bottom:0.8rem;">🍯</div>
        <div style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;font-weight:600;color:#F0C060;margin-bottom:0.6rem;">Raw Honey</div>
        <p style="font-size:0.85rem;color:rgba(255,248,238,0.6);line-height:1.72;margin:0;">
          A natural humectant rich in enzymes and antioxidants. Draws moisture into skin and keeps it there, naturally.
        </p>
      </div>
      <div style="background:rgba(139,26,44,0.1);border:1px solid rgba(139,26,44,0.2);border-radius:18px;padding:2rem;">
        <div style="font-size:2.4rem;margin-bottom:0.8rem;">✨</div>
        <div style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;font-weight:600;color:#F0C060;margin-bottom:0.6rem;">Vitamin E</div>
        <p style="font-size:0.85rem;color:rgba(255,248,238,0.6);line-height:1.72;margin:0;">
          A powerful antioxidant that protects skin from free radicals and helps maintain its youthful moisture balance.
        </p>
      </div>
      <div style="background:rgba(139,26,44,0.1);border:1px solid rgba(139,26,44,0.2);border-radius:18px;padding:2rem;">
        <div style="font-size:2.4rem;margin-bottom:0.8rem;">🚫</div>
        <div style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;font-weight:600;color:#F0C060;margin-bottom:0.6rem;">What We Leave Out</div>
        <p style="font-size:0.85rem;color:rgba(255,248,238,0.6);line-height:1.72;margin:0;">
          No parabens. No aluminum. No phthalates. No SLS. No synthetic dyes. No artificial preservatives. That's our clean promise.
        </p>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── CTA ──────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:5.5rem 4rem;background:#FAF5EE;">
  <div class="section-tag">🛒 Ready?</div>
  <h2 class="section-title">Find your <em>perfect</em> bar</h2>
  <div class="honey-rule" style="margin:0.8rem auto 1.5rem;"></div>
  <p style="font-size:0.95rem;color:#6B3030;max-width:450px;margin:0 auto 2.5rem;line-height:1.78;">
    Browse 13+ handmade scents — from Black Cherry Merlot to Bee Loved —
    all free of the chemicals your skin doesn't need.
  </p>
  <a href="/Shop" target="_self" class="btn-honey" style="text-decoration:none;">Shop All Soaps  →</a>
</div>
""", unsafe_allow_html=True)

render_footer()
