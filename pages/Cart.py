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
  <p class="page-header-sub">Review your bars and check out when you're ready.</p>
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
    You haven't added any soaps yet.<br>
    Head over to the shop and find your perfect bar!
  </p>
</div>
""", unsafe_allow_html=True)
    _, mid, _ = st.columns([2, 1, 2])
    with mid:
        if st.button("🛍️  Browse the Collection", key="goto_shop"):
            st.switch_page("pages/Shop.py")
else:
    cart_col, summary_col = st.columns([1.6, 1], gap="large")

    with cart_col:
        st.markdown("""
<div style="margin-bottom:1.5rem;">
  <div class="section-tag">🧴 Your Soaps</div>
  <h2 style="font-family:'Cormorant Garamond',serif;font-size:1.6rem;color:#1A0808;margin:0.3rem 0 1.5rem;">
    Cart Items
  </h2>
</div>
""", unsafe_allow_html=True)

        to_remove = []
        updated_items = []

        for pid, qty in list(cart.items()):
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
    <div style="font-size:0.8rem;color:#8B4040;margin-top:0.2rem;">{product['weight']} · Paraben-free · Phthalate-free</div>
  </div>
  <div style="display:flex;flex-direction:column;align-items:flex-end;gap:0.5rem;flex-shrink:0;">
    <div class="cart-item-price">${subtotal:.2f}</div>
    <div style="font-size:0.76rem;color:#8B4040;">${product['price']:.2f} each</div>
  </div>
</div>
""", unsafe_allow_html=True)

            q_col, r_col, _ = st.columns([1, 1, 2])
            with q_col:
                new_qty = st.number_input(
                    "Qty",
                    min_value=1, max_value=20, value=qty, step=1,
                    key=f"qty_{pid}", label_visibility="collapsed",
                )
                if new_qty != qty:
                    updated_items.append((pid, new_qty))
            with r_col:
                if st.button("🗑  Remove", key=f"remove_{pid}"):
                    to_remove.append(pid)

        for pid in to_remove:
            remove_from_cart(pid)
        for pid, nq in updated_items:
            update_qty(pid, nq)
        if to_remove or updated_items:
            st.rerun()

        st.markdown('<div style="height:1rem;"></div>', unsafe_allow_html=True)
        if st.button("← Continue Shopping", key="cont_shop"):
            st.switch_page("pages/Shop.py")

    with summary_col:
        total = cart_total()
        shipping = 0.00 if total >= 35 else 5.99
        order_total = total + shipping

        remaining = max(0, 35 - total)
        free_ship_note = (
            '🎉 You\'ve unlocked free shipping!'
            if shipping == 0
            else f'Add ${remaining:.2f} more for free shipping'
        )

        st.markdown(f"""
<div class="order-box">
  <div class="order-box-title">🍯 Order Summary</div>
  <div class="order-row"><span>Subtotal ({cart_count()} items)</span><span>${total:.2f}</span></div>
  <div class="order-row">
    <span>Shipping</span>
    <span>{"FREE" if shipping == 0 else f"${shipping:.2f}"}</span>
  </div>
  <div style="font-size:0.76rem;color:rgba(255,248,238,0.48);margin-top:-0.4rem;margin-bottom:0.8rem;">{free_ship_note}</div>
  <div class="order-row"><span>Tax</span><span>Calculated at checkout</span></div>
  <div class="order-total">
    <span>Total</span>
    <span>${order_total:.2f}</span>
  </div>
</div>
""", unsafe_allow_html=True)

        st.markdown('<div style="margin-top:1.2rem;"></div>', unsafe_allow_html=True)

        if "show_checkout" not in st.session_state:
            st.session_state.show_checkout = False
        if "order_placed" not in st.session_state:
            st.session_state.order_placed = False

        if st.session_state.order_placed:
            st.markdown("""
<div style="background:#FFF8EE;border:2px solid #C9922A;border-radius:18px;padding:2rem;text-align:center;margin-top:1rem;">
  <div style="font-size:2.5rem;margin-bottom:0.8rem;">🎉</div>
  <div style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;color:#1A0808;margin-bottom:0.5rem;">Order Placed!</div>
  <p style="font-size:0.85rem;color:#6B3030;line-height:1.68;margin:0;">
    Thank you for shopping with Thee Bee Boutique!
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
  <div style="font-size:0.76rem;color:#8B4040;line-height:1.65;">
    🔒 Secure checkout &nbsp;·&nbsp; 30-day returns &nbsp;·&nbsp; Free shipping $35+
  </div>
</div>
""", unsafe_allow_html=True)

        else:
            st.markdown('<div style="background:white;border-radius:18px;padding:1.8rem;box-shadow:0 4px 24px rgba(26,8,8,0.08);margin-top:0.5rem;">', unsafe_allow_html=True)
            st.markdown('<h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.15rem;color:#1A0808;margin:0 0 1.2rem;">🏡 Shipping Details</h3>', unsafe_allow_html=True)

            with st.form("checkout_form"):
                n1, n2 = st.columns(2)
                with n1:
                    fname = st.text_input("First Name *", placeholder="Keisha")
                with n2:
                    lname = st.text_input("Last Name *", placeholder="Williams")
                cemail = st.text_input("Email *", placeholder="keisha@email.com")
                addr = st.text_input("Street Address *", placeholder="123 Honey Lane")
                c1, c2 = st.columns(2)
                with c1:
                    city = st.text_input("City *", placeholder="Atlanta")
                with c2:
                    state_val = st.text_input("State *", placeholder="GA")
                zip_code = st.text_input("ZIP *", placeholder="30301")

                st.markdown('<div style="border-top:1px solid #E8D0C0;padding-top:1rem;margin-top:0.5rem;">', unsafe_allow_html=True)
                st.markdown('<h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.05rem;color:#1A0808;margin:0 0 0.8rem;">💳 Payment</h3>', unsafe_allow_html=True)
                card_num = st.text_input("Card Number *", placeholder="•••• •••• •••• ••••")
                e_col, c_col = st.columns(2)
                with e_col:
                    expiry = st.text_input("Expiry *", placeholder="MM / YY")
                with c_col:
                    cvv = st.text_input("CVV *", placeholder="•••")
                st.markdown("</div>", unsafe_allow_html=True)

                place_order = st.form_submit_button(f"🐝  Place Order — ${order_total:.2f}")

                if place_order:
                    if not fname or not cemail or not addr or not city or not zip_code:
                        st.error("Please fill in all required shipping fields.")
                    elif not card_num or not expiry or not cvv:
                        st.error("Please enter your payment details.")
                    else:
                        st.session_state.cart = {}
                        st.session_state.show_checkout = False
                        st.session_state.order_placed = True
                        st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

render_footer()
