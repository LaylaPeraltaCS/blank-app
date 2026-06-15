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
  <div class="page-header-tag">💌 Say Hello</div>
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
  <p style="font-size:0.92rem;color:#6B3030;line-height:1.75;">
    We typically respond within 24–48 hours. For the fastest response,
    DM us on Instagram <strong>@thebeeboutique</strong>.
  </p>
</div>
""", unsafe_allow_html=True)

    with st.form("contact_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            first = st.text_input("First Name *", placeholder="Keisha")
        with c2:
            last = st.text_input("Last Name *", placeholder="Williams")

        email = st.text_input("Email Address *", placeholder="keisha@email.com")

        subject = st.selectbox("Subject", [
            "General Question",
            "Order Inquiry",
            "Custom / Wholesale Order",
            "Sensitive Skin Help",
            "Ingredient Question",
            "Collaboration / Press",
            "Other",
        ])

        message = st.text_area(
            "Your Message *",
            placeholder="What can we help you with?",
            height=160,
        )

        submitted = st.form_submit_button("🐝  Send Message")

        if submitted:
            if not first or not email or not message:
                st.error("Please fill in all required fields (marked with *).")
            else:
                st.success(f"""
**Message received, {first}! 🍯**

Thanks for reaching out to Thee Bee Boutique. We'll get back to you at **{email}** within 24–48 hours.
""")

with info_col:
    st.markdown("""
<div class="contact-info-card">
  <div style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;color:#F0C060;margin-bottom:2rem;font-weight:600;">
    🐝 &nbsp;Find the Hive
  </div>

  <div class="contact-item">
    <span class="contact-icon">📷</span>
    <div>
      <div class="contact-item-title">Instagram</div>
      <div class="contact-item-val">@thebeeboutique<br>DMs open daily — fastest response</div>
    </div>
  </div>

  <div class="contact-item">
    <span class="contact-icon">📧</span>
    <div>
      <div class="contact-item-title">Email</div>
      <div class="contact-item-val">hello@thebeeboutique.com<br>Response within 24–48 hours</div>
    </div>
  </div>

  <div class="contact-item">
    <span class="contact-icon">📦</span>
    <div>
      <div class="contact-item-title">Shipping</div>
      <div class="contact-item-val">Ships within 2–3 business days<br>Free shipping on orders $35+</div>
    </div>
  </div>

  <div class="contact-item" style="margin-bottom:0;">
    <span class="contact-icon">🤝</span>
    <div>
      <div class="contact-item-title">Custom & Wholesale</div>
      <div class="contact-item-val">Boutiques & gifting welcome.<br>Custom scents available for 50+ bar orders.</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

    st.markdown('<div style="height:1.2rem;"></div>', unsafe_allow_html=True)
    st.markdown("""
<div style="background:#F5E0D0;border-radius:16px;padding:1.8rem;border:1px solid #E8C8B8;">
  <div style="font-family:'Cormorant Garamond',serif;font-size:1rem;font-weight:600;color:#1A0808;margin-bottom:0.5rem;">
    📷 &nbsp;Follow on Instagram
  </div>
  <p style="font-size:0.84rem;color:#6B3030;line-height:1.65;margin-bottom:1.2rem;">
    Behind-the-scenes batches, new scent reveals, giveaways, and skin tips.
    Come hang with the hive.
  </p>
  <a href="#" style="background:#8B1A2C;color:white;padding:0.5rem 1.4rem;border-radius:50px;text-decoration:none;font-size:0.82rem;font-weight:600;display:inline-block;">
    📷 &nbsp;@thebeeboutique
  </a>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ── FAQ ──────────────────────────────────────────────────────────
st.markdown("""
<div style="background:linear-gradient(135deg,#F5E0D0,#FAF5EE);padding:5.5rem 4rem;">
  <div style="max-width:900px;margin:0 auto;">
    <div class="section-center" style="margin-bottom:3rem;">
      <div class="section-tag">❓ Got Questions?</div>
      <h2 class="section-title">Frequently <em>Asked</em></h2>
      <div class="honey-rule"></div>
    </div>
""", unsafe_allow_html=True)

faqs = [
    {
        "q": "Are your soaps really free of parabens, aluminum, and phthalates?",
        "a": "Yes — 100%. Every single bar we make is free of parabens, aluminum, and phthalates. These are non-negotiable for us. We believe skincare should never come with a side of harmful chemicals.",
    },
    {
        "q": "Are your products safe for sensitive skin?",
        "a": "Absolutely. All of our soaps are formulated to be sensitive skin friendly. We use organic ingredients and keep our formulas clean and gentle. If you have severe skin allergies, we always recommend a patch test first.",
    },
    {
        "q": "What does 'organic' mean for your ingredients?",
        "a": "We source certified organic oils and butters where possible — coconut oil, olive oil, shea butter, and more. Organic means grown without synthetic pesticides, which is better for your body and the planet.",
    },
    {
        "q": "How long does a bar last?",
        "a": "With proper care (a draining soap dish, keeping it dry between uses), our bars last 3–5 weeks with daily use. Let your bar dry out fully between showers for maximum longevity.",
    },
    {
        "q": "Do you ship everywhere in the US?",
        "a": "Yes! We ship to all 50 states. Standard shipping is free on orders over $35. International shipping is coming soon — sign up for our newsletter to be notified!",
    },
    {
        "q": "Can I do a custom scent or bulk order?",
        "a": "Yes! We love custom work. Minimum 50 bars for custom scents, 24 bars for custom labels. Perfect for weddings, corporate gifting, boutique wholesale, and more. Email us to get started.",
    },
    {
        "q": "What is your return policy?",
        "a": "We offer a 30-day happiness guarantee. Not satisfied? Contact us within 30 days of delivery and we'll replace your bar or refund you fully — no questions asked.",
    },
]

with st.container():
    st.markdown('<div style="background:linear-gradient(135deg,#F5E0D0,#FAF5EE);padding:0 4rem 5.5rem;">', unsafe_allow_html=True)
    st.markdown('<div style="max-width:900px;margin:0 auto;">', unsafe_allow_html=True)
    for faq in faqs:
        with st.expander(faq["q"]):
            st.markdown(f'<p style="font-size:0.9rem;color:#6B3030;line-height:1.78;margin:0;">{faq["a"]}</p>', unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True)

# ── SHIPPING ──────────────────────────────────────────────────────
st.markdown("""
<div style="max-width:1100px;margin:0 auto;padding:5rem 4rem;">
  <div class="section-center">
    <div class="section-tag">📦 Delivery</div>
    <h2 class="section-title">Shipping <em>Info</em></h2>
    <div class="honey-rule"></div>
  </div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;margin-top:2rem;">
    <div style="background:white;border-radius:18px;padding:2rem;text-align:center;box-shadow:0 4px 24px rgba(26,8,8,0.07);">
      <div style="font-size:2.5rem;margin-bottom:0.8rem;">🚚</div>
      <div style="font-family:'Cormorant Garamond',serif;font-size:1.05rem;font-weight:600;color:#1A0808;margin-bottom:0.5rem;">Standard Shipping</div>
      <div style="font-size:0.85rem;color:#6B3030;line-height:1.68;">5–7 business days · $5.99<br>Free on orders over $35</div>
    </div>
    <div style="background:white;border-radius:18px;padding:2rem;text-align:center;box-shadow:0 4px 24px rgba(26,8,8,0.07);">
      <div style="font-size:2.5rem;margin-bottom:0.8rem;">⚡</div>
      <div style="font-family:'Cormorant Garamond',serif;font-size:1.05rem;font-weight:600;color:#1A0808;margin-bottom:0.5rem;">Express Shipping</div>
      <div style="font-size:0.85rem;color:#6B3030;line-height:1.68;">2–3 business days · $12.99<br>Available at checkout</div>
    </div>
    <div style="background:white;border-radius:18px;padding:2rem;text-align:center;box-shadow:0 4px 24px rgba(26,8,8,0.07);">
      <div style="font-size:2.5rem;margin-bottom:0.8rem;">📬</div>
      <div style="font-family:'Cormorant Garamond',serif;font-size:1.05rem;font-weight:600;color:#1A0808;margin-bottom:0.5rem;">Processing Time</div>
      <div style="font-size:0.85rem;color:#6B3030;line-height:1.68;">Orders ship in 2–3 business days<br>Tracking included on all orders</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

render_footer()
