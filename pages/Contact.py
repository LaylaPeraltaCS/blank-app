import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import load_css, render_nav, render_footer, init_cart

st.set_page_config(
    page_title="Contact | Thee Bee Boutique",
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
  <div class="page-header-tag">💌 Get in Touch</div>
  <h1 class="page-header-title">We'd <em>love</em> to hear from you</h1>
  <p class="page-header-sub">Questions, custom orders, wholesale — our hive is always open.</p>
</div>
""", unsafe_allow_html=True)

# ── CONTACT FORM + INFO ──────────────────────────────────────────
st.markdown('<div style="max-width:1100px;margin:0 auto;padding:5rem 4rem;">', unsafe_allow_html=True)

form_col, info_col = st.columns([1.4, 1], gap="large")

with form_col:
    st.markdown("""
<div style="margin-bottom:1.8rem;">
  <div class="section-tag">✍️ Send a Message</div>
  <h2 class="section-title">Drop us a <em>note</em></h2>
  <div class="honey-rule"></div>
  <p style="font-size:0.92rem;color:#6B4226;line-height:1.72;">
    We typically respond within 24–48 hours. For urgent orders, please
    DM us on Instagram <strong>@thebeeboutique</strong>.
  </p>
</div>
""", unsafe_allow_html=True)

    with st.form("contact_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            first = st.text_input("First Name *", placeholder="Jasmine")
        with c2:
            last = st.text_input("Last Name *", placeholder="Taylor")

        email = st.text_input("Email Address *", placeholder="jasmine@email.com")

        subject = st.selectbox("Subject", [
            "General Question",
            "Order Inquiry",
            "Custom / Wholesale Order",
            "Skin Concern Help",
            "Collaboration / Press",
            "Other",
        ])

        message = st.text_area(
            "Your Message *",
            placeholder="Tell us what's on your mind…",
            height=160,
        )

        submitted = st.form_submit_button("🐝  Send Message")

        if submitted:
            if not first or not email or not message:
                st.error("Please fill in all required fields (marked with *).")
            else:
                st.success(f"""
**Message received, {first}! 🍯**

Thanks for reaching out. We'll get back to you at **{email}** within 24–48 hours.
While you wait, feel free to explore [our full collection](/Shop)!
""")

with info_col:
    st.markdown("""
<div class="contact-info-card">
  <div style="font-family:'Playfair Display',serif;font-size:1.25rem;color:#F0C060;margin-bottom:1.8rem;font-weight:600;">
    🐝 &nbsp;Find Us
  </div>

  <div class="contact-item">
    <span class="contact-icon">📷</span>
    <div>
      <div class="contact-item-title">Instagram</div>
      <div class="contact-item-val">@thebeeboutique<br>DMs open daily · fastest response</div>
    </div>
  </div>

  <div class="contact-item">
    <span class="contact-icon">📧</span>
    <div>
      <div class="contact-item-title">Email</div>
      <div class="contact-item-val">hello@thebeeboutique.com<br>Response within 24–48 hrs</div>
    </div>
  </div>

  <div class="contact-item">
    <span class="contact-icon">📦</span>
    <div>
      <div class="contact-item-title">Shipping</div>
      <div class="contact-item-val">All orders ship within 2–3 business days<br>Free shipping on orders $45+</div>
    </div>
  </div>

  <div class="contact-item" style="margin-bottom:0;">
    <span class="contact-icon">🤝</span>
    <div>
      <div class="contact-item-title">Wholesale & Custom</div>
      <div class="contact-item-val">Boutique owners & gifting companies welcome. Custom scents available for orders of 50+ bars.</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

    st.markdown('<div style="height:1.5rem;"></div>', unsafe_allow_html=True)

    st.markdown("""
<div style="background:#F5E8CC;border-radius:18px;padding:1.8rem;border:1px solid #E8D5B0;">
  <div style="font-family:'Playfair Display',serif;font-size:1rem;font-weight:600;color:#2C1A0E;margin-bottom:0.5rem;">
    🍯 &nbsp;Bee Social
  </div>
  <p style="font-size:0.85rem;color:#6B4226;line-height:1.65;margin-bottom:1.2rem;">
    Follow us for behind-the-scenes soap making, new scent reveals, and skin tips.
  </p>
  <div style="display:flex;gap:0.75rem;">
    <a href="#" style="background:#C9922A;color:white;padding:0.5rem 1.2rem;border-radius:50px;text-decoration:none;font-size:0.82rem;font-weight:600;">📷 Instagram</a>
    <a href="#" style="background:#2C1A0E;color:#F0C060;padding:0.5rem 1.2rem;border-radius:50px;text-decoration:none;font-size:0.82rem;font-weight:600;">📌 Pinterest</a>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ── FAQ ──────────────────────────────────────────────────────────
st.markdown("""
<div style="background:linear-gradient(135deg,#F5E8CC,#FFF8EE);padding:5.5rem 4rem;">
  <div style="max-width:900px;margin:0 auto;">
    <div class="section-center" style="margin-bottom:3rem;">
      <div class="section-tag">❓ Common Questions</div>
      <h2 class="section-title">Frequently <em>Asked</em></h2>
      <div class="honey-rule"></div>
    </div>
</div>
""", unsafe_allow_html=True)

faqs = [
    {
        "q": "Are your soaps safe for sensitive skin?",
        "a": "Yes! Our Golden Honey Oat Bar and Coconut Milk & Honey are specifically formulated for sensitive skin. All bars are free of SLS, parabens, synthetic dyes, and artificial fragrances. We always recommend patch-testing if you have severe skin allergies.",
    },
    {
        "q": "How long does a bar last?",
        "a": "With proper care (using a soap dish that drains well and keeping it dry between uses), our bars last 4–6 weeks with daily use. We recommend a slatted soap dish to maximize bar life.",
    },
    {
        "q": "Do you ship internationally?",
        "a": "We currently ship within the United States. International shipping is coming soon! Sign up for our newsletter to be the first to know when we expand.",
    },
    {
        "q": "What is your return policy?",
        "a": "We offer a 30-day happiness guarantee. If you're not satisfied, contact us within 30 days of delivery and we'll replace your bar or issue a full refund — no questions asked.",
    },
    {
        "q": "Can I order custom scents or labels?",
        "a": "Absolutely! We love custom orders for weddings, baby showers, corporate gifting, and boutique wholesale. Minimum order is 50 bars for custom scents and 24 bars for custom labels. Contact us to get started.",
    },
    {
        "q": "Are your products vegan?",
        "a": "Most of our bars are vegan-friendly. Our Lavender Beeswax Dream and any bar containing beeswax or honey are not technically vegan, though they are cruelty-free. The product descriptions clearly list all ingredients.",
    },
]

with st.container():
    st.markdown('<div style="background:linear-gradient(135deg,#F5E8CC,#FFF8EE);padding:0 4rem 5.5rem;">', unsafe_allow_html=True)
    st.markdown('<div style="max-width:900px;margin:0 auto;">', unsafe_allow_html=True)

    for faq in faqs:
        with st.expander(faq["q"]):
            st.markdown(f'<p style="font-size:0.92rem;color:#6B4226;line-height:1.75;margin:0;">{faq["a"]}</p>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ── SHIPPING INFO ─────────────────────────────────────────────────
st.markdown("""
<div style="max-width:1100px;margin:0 auto;padding:5rem 4rem;">
  <div class="section-tag" style="text-align:center;">📦 Delivery Details</div>
  <h2 class="section-title" style="text-align:center;">Shipping <em>Information</em></h2>
  <div class="honey-rule" style="margin:0.8rem auto 3rem;"></div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;">
    <div style="background:white;border-radius:18px;padding:2rem;text-align:center;box-shadow:0 4px 24px rgba(44,26,14,0.07);">
      <div style="font-size:2.5rem;margin-bottom:0.8rem;">🚚</div>
      <div style="font-family:'Playfair Display',serif;font-size:1.05rem;font-weight:600;color:#2C1A0E;margin-bottom:0.5rem;">Standard Shipping</div>
      <div style="font-size:0.86rem;color:#6B4226;line-height:1.65;">5–7 business days · $5.99<br>Free on orders over $45</div>
    </div>
    <div style="background:white;border-radius:18px;padding:2rem;text-align:center;box-shadow:0 4px 24px rgba(44,26,14,0.07);">
      <div style="font-size:2.5rem;margin-bottom:0.8rem;">⚡</div>
      <div style="font-family:'Playfair Display',serif;font-size:1.05rem;font-weight:600;color:#2C1A0E;margin-bottom:0.5rem;">Express Shipping</div>
      <div style="font-size:0.86rem;color:#6B4226;line-height:1.65;">2–3 business days · $12.99<br>Available at checkout</div>
    </div>
    <div style="background:white;border-radius:18px;padding:2rem;text-align:center;box-shadow:0 4px 24px rgba(44,26,14,0.07);">
      <div style="font-size:2.5rem;margin-bottom:0.8rem;">📬</div>
      <div style="font-family:'Playfair Display',serif;font-size:1.05rem;font-weight:600;color:#2C1A0E;margin-bottom:0.5rem;">Order Processing</div>
      <div style="font-size:0.86rem;color:#6B4226;line-height:1.65;">We ship within 2–3 business days<br>Tracking provided for all orders</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

render_footer()
