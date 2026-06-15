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
  <h1 class="page-header-title">Made with <em>intention,</em><br>not shortcuts.</h1>
  <p class="page-header-sub">A small studio, a big love for good skin, and the bees that make it all possible.</p>
</div>
""", unsafe_allow_html=True)

# ── FOUNDER STORY ────────────────────────────────────────────────
st.markdown('<div style="max-width:1200px;margin:0 auto;">', unsafe_allow_html=True)

left, right = st.columns([1.1, 1], gap="large")

with left:
    st.markdown("""
<div style="padding:4.5rem 2rem 4rem 4rem;">
  <div class="section-tag">🐝 From the Founder</div>
  <h2 class="section-title">A little kitchen.<br>A <em>big</em> dream.</h2>
  <div class="honey-rule"></div>
  <p style="font-size:0.96rem;color:#6B4226;line-height:1.82;margin-bottom:1.4rem;">
    Thee Bee Boutique started the way all good things do — out of necessity
    and love. After struggling with dry, sensitive skin for years and
    finding nothing that actually worked, I decided to make my own.
  </p>
  <p style="font-size:0.96rem;color:#6B4226;line-height:1.82;margin-bottom:1.4rem;">
    Armed with a kitchen scale, a YouTube playlist, and a local beekeeper
    who sold me my first jar of raw wildflower honey, I poured my first
    batch of soap in 2019. My friends and family were hooked immediately —
    and the rest is history.
  </p>
  <p style="font-size:0.96rem;color:#6B4226;line-height:1.82;margin-bottom:2rem;">
    Today, every bar is still made in small batches in my studio, cured for
    4–6 weeks, and hand-wrapped with care. Because shortcuts don't belong
    in skincare — or in anything worth doing right.
  </p>
  <div style="display:flex;align-items:center;gap:1rem;margin-top:1rem;">
    <div style="width:56px;height:56px;border-radius:50%;background:linear-gradient(135deg,#C9922A,#F0C060);display:flex;align-items:center;justify-content:center;color:white;font-family:'Playfair Display',serif;font-size:1.3rem;font-weight:700;flex-shrink:0;">B</div>
    <div>
      <div style="font-family:'Playfair Display',serif;font-size:1rem;font-weight:600;color:#2C1A0E;">Bee, Founder</div>
      <div style="font-size:0.82rem;color:#8B5E3C;">Soapmaker · Honey lover · Small batch queen</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

with right:
    st.markdown("""
<div style="padding:4.5rem 4rem 4rem 2rem;">
  <div class="story-img">
    <img src="https://images.unsplash.com/photo-1559715745-e1b33a271d2b?auto=format&fit=crop&w=700&q=80"
         alt="Soap making studio" loading="lazy">
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ── VALUES ───────────────────────────────────────────────────────
st.markdown("""
<div style="background:linear-gradient(135deg,#F5E8CC,#FFF8EE);padding:5.5rem 4rem;">
  <div style="max-width:1200px;margin:0 auto;">
    <div class="section-center">
      <div class="section-tag">💛 What We Stand For</div>
      <h2 class="section-title">Our <em>values</em> are non-negotiable</h2>
      <div class="honey-rule"></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div style="background:linear-gradient(135deg,#F5E8CC,#FFF8EE);padding:0 4rem 5.5rem;">', unsafe_allow_html=True)
    st.markdown('<div style="max-width:1200px;margin:0 auto;">', unsafe_allow_html=True)

    v_cols = st.columns(4)
    values = [
        {
            "icon": "🌿",
            "title": "Always Natural",
            "text": "Every ingredient earns its place. No sulfates, no parabens, no synthetic fragrances — ever. What you see on the label is exactly what's in the bar.",
        },
        {
            "icon": "🐝",
            "title": "Bee-Friendly",
            "text": "We partner with local beekeepers who practice ethical, sustainable beekeeping. Healthy bees mean healthier honey — and a healthier planet.",
        },
        {
            "icon": "♻️",
            "title": "Low Waste",
            "text": "Our packaging is plastic-free and compostable. We source local where possible to reduce our footprint. Good for your skin and the earth.",
        },
        {
            "icon": "✊🏽",
            "title": "Woman Owned",
            "text": "Thee Bee Boutique is proudly Black woman-owned and operated. Every purchase directly supports an independent maker and her community.",
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
  <div class="section-tag">⚗️ How It's Made</div>
  <h2 class="section-title">The cold-process<br><em>craft</em></h2>
  <div class="honey-rule"></div>
  <div class="process-step">
    <div class="step-num">1</div>
    <div class="step-body">
      <h4>Source & Measure</h4>
      <p>We weigh every ingredient by the gram — premium oils, butters, and fresh raw honey sourced within 50 miles of our studio.</p>
    </div>
  </div>
  <div class="process-step">
    <div class="step-num">2</div>
    <div class="step-body">
      <h4>Blend & Saponify</h4>
      <p>Oils and lye are carefully combined at precise temperatures. The chemical reaction (saponification) creates soap — and zero lye remains in the finished bar.</p>
    </div>
  </div>
  <div class="process-step">
    <div class="step-num">3</div>
    <div class="step-body">
      <h4>Pour & Set</h4>
      <p>We pour the batter into molds, add botanicals on top, and let the bars set for 24–48 hours before unmolding and cutting by hand.</p>
    </div>
  </div>
  <div class="process-step" style="margin-bottom:0;">
    <div class="step-num">4</div>
    <div class="step-body">
      <h4>Cure for 4–6 Weeks</h4>
      <p>Each bar air-cures on wooden racks. This evaporates excess water, hardens the bar, and develops a richer, longer-lasting lather.</p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

with p_right:
    st.markdown("""
<div style="padding:5rem 4rem 5rem 2rem;">
  <div class="story-img">
    <img src="https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?auto=format&fit=crop&w=700&q=80"
         alt="Soap curing process" loading="lazy">
  </div>
</div>
""", unsafe_allow_html=True)

# ── INGREDIENTS SPOTLIGHT ─────────────────────────────────────────
st.markdown("""
<div style="background:#2C1A0E;padding:5.5rem 4rem;">
  <div style="max-width:1200px;margin:0 auto;">
    <div class="section-center" style="margin-bottom:3.5rem;">
      <div class="section-tag" style="color:rgba(240,192,96,0.75);">🍯 The Good Stuff</div>
      <h2 class="section-title" style="color:#FFF8EE;">Hero <em>ingredients</em> we love</h2>
      <div class="honey-rule" style="margin:0.8rem auto 0;"></div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;">
      <div style="background:rgba(201,146,42,0.1);border:1px solid rgba(201,146,42,0.2);border-radius:18px;padding:2rem;">
        <div style="font-size:2.5rem;margin-bottom:0.8rem;">🍯</div>
        <div style="font-family:'Playfair Display',serif;font-size:1.1rem;font-weight:600;color:#F0C060;margin-bottom:0.6rem;">Raw Wildflower Honey</div>
        <p style="font-size:0.86rem;color:rgba(255,248,238,0.65);line-height:1.7;margin:0;">
          A natural humectant that draws moisture into skin. Rich in amino acids, antioxidants, and antibacterial properties. Our skin's best friend.
        </p>
      </div>
      <div style="background:rgba(201,146,42,0.1);border:1px solid rgba(201,146,42,0.2);border-radius:18px;padding:2rem;">
        <div style="font-size:2.5rem;margin-bottom:0.8rem;">🌿</div>
        <div style="font-family:'Playfair Display',serif;font-size:1.1rem;font-weight:600;color:#F0C060;margin-bottom:0.6rem;">Shea Butter</div>
        <p style="font-size:0.86rem;color:rgba(255,248,238,0.65);line-height:1.7;margin:0;">
          A deep moisturizer packed with vitamins A, E, and F. It helps repair the skin barrier and reduces dryness without clogging pores.
        </p>
      </div>
      <div style="background:rgba(201,146,42,0.1);border:1px solid rgba(201,146,42,0.2);border-radius:18px;padding:2rem;">
        <div style="font-size:2.5rem;margin-bottom:0.8rem;">✨</div>
        <div style="font-family:'Playfair Display',serif;font-size:1.1rem;font-weight:600;color:#F0C060;margin-bottom:0.6rem;">Beeswax</div>
        <p style="font-size:0.86rem;color:rgba(255,248,238,0.65);line-height:1.7;margin:0;">
          Forms a protective, breathable barrier on skin. Locks in moisture, soothes irritation, and gives our bars their signature creamy hardness.
        </p>
      </div>
      <div style="background:rgba(201,146,42,0.1);border:1px solid rgba(201,146,42,0.2);border-radius:18px;padding:2rem;">
        <div style="font-size:2.5rem;margin-bottom:0.8rem;">🫒</div>
        <div style="font-family:'Playfair Display',serif;font-size:1.1rem;font-weight:600;color:#F0C060;margin-bottom:0.6rem;">Olive Oil</div>
        <p style="font-size:0.86rem;color:rgba(255,248,238,0.65);line-height:1.7;margin:0;">
          The backbone of our formula. Deeply nourishing, gentle on all skin types, and packed with squalene that mimics your skin's natural oils.
        </p>
      </div>
      <div style="background:rgba(201,146,42,0.1);border:1px solid rgba(201,146,42,0.2);border-radius:18px;padding:2rem;">
        <div style="font-size:2.5rem;margin-bottom:0.8rem;">🥥</div>
        <div style="font-family:'Playfair Display',serif;font-size:1.1rem;font-weight:600;color:#F0C060;margin-bottom:0.6rem;">Coconut Oil</div>
        <p style="font-size:0.86rem;color:rgba(255,248,238,0.65);line-height:1.7;margin:0;">
          Creates that luxurious, bubbly lather we all love. Antimicrobial and conditioning, it cleanses deeply while leaving skin soft.
        </p>
      </div>
      <div style="background:rgba(201,146,42,0.1);border:1px solid rgba(201,146,42,0.2);border-radius:18px;padding:2rem;">
        <div style="font-size:2.5rem;margin-bottom:0.8rem;">🌸</div>
        <div style="font-family:'Playfair Display',serif;font-size:1.1rem;font-weight:600;color:#F0C060;margin-bottom:0.6rem;">Botanicals & Essentials</div>
        <p style="font-size:0.86rem;color:rgba(255,248,238,0.65);line-height:1.7;margin:0;">
          Real lavender buds, rose petals, oatmeal, and activated charcoal — each chosen for a specific skin benefit, never just for looks.
        </p>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── CTA ──────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:5rem 4rem;">
  <div class="section-tag">🛒 Ready to Glow?</div>
  <h2 class="section-title">Find your perfect <em>bar</em></h2>
  <div class="honey-rule" style="margin:0.8rem auto 1.5rem;"></div>
  <p style="font-size:0.96rem;color:#6B4226;max-width:480px;margin:0 auto 2.5rem;line-height:1.75;">
    Browse the full Hive Collection and discover the soap that your skin has been waiting for.
  </p>
  <a href="/Shop" target="_self" class="btn-honey" style="text-decoration:none;">Shop All Soaps  →</a>
</div>
""", unsafe_allow_html=True)

render_footer()
