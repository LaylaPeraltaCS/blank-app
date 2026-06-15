import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import (
    load_css, render_nav, render_footer,
    PRODUCTS_BY_ID, init_cart, cart_count, cart_total,
    remove_from_cart, update_qty,
)

st.set_page_config(
    page_title="Cart | Thee Bee Boutique",
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
  <div class="page-header-tag">🛒 Your Order</div>
  <h1 class="page-header-title">Your <em>Cart</em></h1>
  <p class="page-header-sub">Review your items and check out when you're ready.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div style="max-width:1100px;margin:0 auto;padding:4rem 4rem 6rem;">', unsafe_allow_html=True)

cart = st.session_state.get("cart", {})

if not cart:
    st.markdown("""
<div class="empty-cart">
  <span class="empty-cart-icon">🛒</span>
  <h3>Your cart is empty</h3>
  <p>
    Looks like you haven't added anything yet.<br>
    Head over to the shop and find your perfect bar!
  </p>
</div>
""", unsafe_allow_html=True)
    _, mid, _ = st.columns([2, 1, 2])
    with mid:
        if st.button("🛍️  Browse the Hive", key="goto_shop"):
            st.switch_page("pages/Shop.py")
else:
    cart_col, summary_col = st.columns([1.6, 1], gap="large")

    with cart_col:
        st.markdown("""
<div style="margin-bottom:1.5rem;">
  <div class="section-tag">🧴 Your Soaps</div>
  <h2 style="font-family:'Playfair Display',serif;font-size:1.5rem;color:#2C1A0E;margin:0.3rem 0 1.5rem;">
    Cart Items
  </h2>
</div>
""", unsafe_allow_html=True)

        to_remove = []
        updated_items = []

        for pid, qty in cart.items():
            product = PRODUCTS_BY_ID.get(pid)
            if not product:
                continue
            subtotal = product["price"] * qty

            st.markdown(f"""
<div class="cart-item-card">
  <img src="{product['image']}" class="cart-item-img" alt="{product['name']}" loading="lazy">
  <div style="flex:1;min-width:0;">
    <div class="cart-item-scent">{product['scent']}</div>
    <div class="cart-item-name">{product['name']}</div>
    <div style="font-size:0.82rem;color:#8B5E3C;margin-top:0.2rem;">{product['weight']}</div>
  </div>
  <div style="display:flex;flex-direction:column;align-items:flex-end;gap:0.6rem;flex-shrink:0;">
    <div class="cart-item-price">${subtotal:.2f}</div>
    <div style="font-size:0.78rem;color:#8B5E3C;">${product['price']:.2f} each</div>
  </div>
</div>
""", unsafe_allow_html=True)

            q_col, r_col, _ = st.columns([1, 1, 2])
            with q_col:
                new_qty = st.number_input(
                    "Qty",
                    min_value=1,
                    max_value=20,
                    value=qty,
                    step=1,
                    key=f"qty_{pid}",
                    label_visibility="collapsed",
                )
                if new_qty != qty:
                    updated_items.append((pid, new_qty))

            with r_col:
                if st.button("🗑  Remove", key=f"remove_{pid}"):
                    to_remove.append(pid)

        for pid in to_remove:
            remove_from_cart(pid)
        for pid, new_qty in updated_items:
            update_qty(pid, new_qty)

        if to_remove or updated_items:
            st.rerun()

        st.markdown('<div style="height:1rem;"></div>', unsafe_allow_html=True)
        if st.button("← Continue Shopping", key="cont_shop"):
            st.switch_page("pages/Shop.py")

    with summary_col:
        total = cart_total()
        shipping = 0.00 if total >= 45 else 5.99
        order_total = total + shipping

        st.markdown(f"""
<div class="order-box">
  <div class="order-box-title">🍯 Order Summary</div>
  <div class="order-row"><span>Subtotal ({cart_count()} items)</span><span>${total:.2f}</span></div>
  <div class="order-row">
    <span>Shipping</span>
    <span>{"FREE 🎉" if shipping == 0 else f"${shipping:.2f}"}</span>
  </div>
  {"" if shipping == 0 else f'<div style="font-size:0.78rem;color:rgba(255,248,238,0.5);margin-top:-0.4rem;margin-bottom:0.6rem;">Add ${45-total:.2f} more for free shipping</div>'}
  <div class="order-row"><span>Estimated Tax</span><span>Calculated at checkout</span></div>
  <div class="order-total">
    <span>Order Total</span>
    <span>${order_total:.2f}</span>
  </div>
</div>
""", unsafe_allow_html=True)

        st.markdown('<div style="margin-top:1.2rem;"></div>', unsafe_allow_html=True)

        # Checkout form
        if "show_checkout" not in st.session_state:
            st.session_state.show_checkout = False
        if "order_placed" not in st.session_state:
            st.session_state.order_placed = False

        if st.session_state.order_placed:
            st.markdown("""
<div style="background:#FFF8EE;border:2px solid #C9922A;border-radius:18px;padding:2rem;text-align:center;">
  <div style="font-size:2.5rem;margin-bottom:0.8rem;">🎉</div>
  <div style="font-family:'Playfair Display',serif;font-size:1.2rem;color:#2C1A0E;margin-bottom:0.5rem;">Order Placed!</div>
  <p style="font-size:0.86rem;color:#6B4226;line-height:1.65;margin:0;">
    Thank you for your order! You'll receive a confirmation email shortly.
    Your soaps will ship within 2–3 business days. 🐝
  </p>
</div>
""", unsafe_allow_html=True)

        elif not st.session_state.show_checkout:
            if st.button("🛒  Proceed to Checkout", key="checkout_btn"):
                st.session_state.show_checkout = True
                st.rerun()

            st.markdown("""
<div style="margin-top:1rem;text-align:center;">
  <div style="font-size:0.78rem;color:#8B5E3C;line-height:1.65;">
    🔒 &nbsp;Secure checkout &nbsp;·&nbsp; 30-day returns &nbsp;·&nbsp; Free shipping on $45+
  </div>
  <div style="margin-top:0.8rem;font-size:1.2rem;">💳 🍎 📱</div>
</div>
""", unsafe_allow_html=True)

        else:
            st.markdown('<div class="checkout-form">', unsafe_allow_html=True)
            st.markdown('<h3>🏡 &nbsp;Shipping Details</h3>', unsafe_allow_html=True)

            with st.form("checkout_form"):
                n1, n2 = st.columns(2)
                with n1:
                    fname = st.text_input("First Name *", placeholder="Jasmine")
                with n2:
                    lname = st.text_input("Last Name *", placeholder="Taylor")

                cemail = st.text_input("Email *", placeholder="jasmine@email.com")
                addr = st.text_input("Street Address *", placeholder="123 Honey Lane")

                c1, c2 = st.columns(2)
                with c1:
                    city = st.text_input("City *", placeholder="Atlanta")
                with c2:
                    state = st.text_input("State *", placeholder="GA")

                zip_code = st.text_input("ZIP Code *", placeholder="30301")

                st.markdown('<div style="margin-top:1rem;border-top:1px solid #E8D5B0;padding-top:1rem;">', unsafe_allow_html=True)
                st.markdown('<h3 style="font-family:\'Playfair Display\',serif;font-size:1rem;color:#2C1A0E;margin-bottom:1rem;">💳 &nbsp;Payment</h3>', unsafe_allow_html=True)

                card_num = st.text_input("Card Number *", placeholder="•••• •••• •••• ••••")
                exp_col, cvv_col = st.columns(2)
                with exp_col:
                    expiry = st.text_input("Expiry *", placeholder="MM / YY")
                with cvv_col:
                    cvv = st.text_input("CVV *", placeholder="•••")

                st.markdown("</div>", unsafe_allow_html=True)

                place_order = st.form_submit_button(f"🐝  Place Order — ${order_total:.2f}")

                if place_order:
                    if not fname or not cemail or not addr or not city or not zip_code:
                        st.error("Please fill in all required shipping fields.")
                    elif not card_num or not expiry or not cvv:
                        st.error("Please fill in your payment details.")
                    else:
                        st.session_state.cart = {}
                        st.session_state.show_checkout = False
                        st.session_state.order_placed = True
                        st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

render_footer()
