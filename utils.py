import streamlit as st

# ══════════════════════════════════════════════════════════════════
#  PRODUCT CATALOG
# ══════════════════════════════════════════════════════════════════

PRODUCTS = [
    {
        "id": 1,
        "name": "Golden Honey Oat Bar",
        "tagline": "Gentle nourishment for sensitive skin",
        "price": 12.00,
        "description": (
            "Our signature bar blends raw wildflower honey with colloidal oatmeal "
            "and creamy shea butter for a soap that feels like a warm hug. "
            "The oatmeal gently exfoliates while honey seals in moisture, leaving "
            "skin soft, balanced, and delicately sweet-scented."
        ),
        "scent": "Warm Honey & Vanilla",
        "scent_family": "Sweet",
        "skin_types": ["Sensitive", "All Types"],
        "weight": "4.5 oz",
        "ingredients": [
            "Saponified Olive Oil", "Coconut Oil", "Shea Butter",
            "Raw Wildflower Honey", "Colloidal Oatmeal", "Cocoa Butter",
            "Vanilla Extract", "Vitamin E",
        ],
        "image": "https://images.unsplash.com/photo-1600857062241-98e5dba7f025?auto=format&fit=crop&w=600&q=80",
        "badge": "Best Seller",
        "rating": 4.9,
        "reviews": 284,
    },
    {
        "id": 2,
        "name": "Lavender Beeswax Dream",
        "tagline": "Calming florals for a restful evening",
        "price": 14.00,
        "description": (
            "Infused with French lavender essential oil and golden beeswax, this bar "
            "transforms your evening routine into a bedtime ritual. Naturally soothing "
            "properties calm your mind while beeswax conditions your skin overnight."
        ),
        "scent": "French Lavender",
        "scent_family": "Floral",
        "skin_types": ["Dry", "Normal"],
        "weight": "4.5 oz",
        "ingredients": [
            "Saponified Olive Oil", "Coconut Oil", "Beeswax",
            "Lavender Essential Oil", "Shea Butter", "Lavender Buds",
        ],
        "image": "https://images.unsplash.com/photo-1611241893603-3c359704e0ee?auto=format&fit=crop&w=600&q=80",
        "badge": "Staff Pick",
        "rating": 4.8,
        "reviews": 196,
    },
    {
        "id": 3,
        "name": "Citrus Honey Glow",
        "tagline": "Brighten & energize your morning routine",
        "price": 13.00,
        "description": (
            "Wake up your senses with a burst of sweet orange, lemon zest, and grapefruit, "
            "grounded by a touch of raw honey. Your daily dose of sunshine in a bar — "
            "brightening, refreshing, and naturally cleansing."
        ),
        "scent": "Sweet Orange & Lemon Zest",
        "scent_family": "Citrus",
        "skin_types": ["All Types", "Oily"],
        "weight": "4.5 oz",
        "ingredients": [
            "Saponified Olive Oil", "Coconut Oil", "Sweet Orange Essential Oil",
            "Lemon Essential Oil", "Raw Honey", "Castor Oil", "Grapefruit Peel",
        ],
        "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?auto=format&fit=crop&w=600&q=80",
        "badge": "New",
        "rating": 4.7,
        "reviews": 98,
    },
    {
        "id": 4,
        "name": "Rose Petal & Honey",
        "tagline": "Luxurious romance in every lather",
        "price": 15.00,
        "description": (
            "Real rose petals and rose absolute blend with wildflower honey in a rich, "
            "creamy bar that leaves skin soft and delicately scented. A little romance "
            "for your skin, every single morning."
        ),
        "scent": "Rose Absolute",
        "scent_family": "Floral",
        "skin_types": ["Normal", "Dry"],
        "weight": "4.5 oz",
        "ingredients": [
            "Saponified Olive Oil", "Coconut Oil", "Rose Absolute",
            "Shea Butter", "Raw Honey", "Rose Petals", "Rosehip Oil",
        ],
        "image": "https://images.unsplash.com/photo-1582731478119-6f59f7ac01b7?auto=format&fit=crop&w=600&q=80",
        "badge": "Fan Favorite",
        "rating": 4.9,
        "reviews": 312,
    },
    {
        "id": 5,
        "name": "Peppermint Refresh",
        "tagline": "Invigorating cool for your daily cleanse",
        "price": 11.00,
        "description": (
            "A tingle of peppermint essential oil in a base of neem and coconut oil "
            "creates the ultimate refreshing cleanse. Perfect for mornings when you need "
            "to wake up fast and feel alive."
        ),
        "scent": "Peppermint & Eucalyptus",
        "scent_family": "Fresh",
        "skin_types": ["Oily", "Normal", "All Types"],
        "weight": "4.5 oz",
        "ingredients": [
            "Saponified Coconut Oil", "Olive Oil", "Peppermint Essential Oil",
            "Eucalyptus Essential Oil", "Castor Oil", "Shea Butter",
        ],
        "image": "https://images.unsplash.com/photo-1547592180-85f173d888a4?auto=format&fit=crop&w=600&q=80",
        "badge": None,
        "rating": 4.7,
        "reviews": 143,
    },
    {
        "id": 6,
        "name": "Vanilla Amber Luxe",
        "tagline": "Warm & indulgent for ultra-dry skin",
        "price": 16.00,
        "description": (
            "Our most luxurious bar — warm vanilla bean, amber resin, and a generous "
            "helping of cocoa butter create a soap that moisturizes as much as it cleanses. "
            "Skin feels impossibly soft after every use."
        ),
        "scent": "Vanilla Bean & Amber",
        "scent_family": "Sweet",
        "skin_types": ["Dry", "Very Dry"],
        "weight": "4.5 oz",
        "ingredients": [
            "Saponified Olive Oil", "Cocoa Butter", "Coconut Oil",
            "Vanilla Extract", "Amber Fragrance Oil", "Castor Oil", "Vitamin E",
        ],
        "image": "https://images.unsplash.com/photo-1607001486043-2b4e2db7d8b5?auto=format&fit=crop&w=600&q=80",
        "badge": "Luxury",
        "rating": 5.0,
        "reviews": 67,
    },
    {
        "id": 7,
        "name": "Tea Tree Clarify",
        "tagline": "Clear skin starts with clean skin",
        "price": 13.00,
        "description": (
            "Tea tree and activated charcoal work together to deep-cleanse pores "
            "and clarify skin. This powerhouse bar fights breakouts while keeping "
            "skin balanced — no over-stripping, no dryness."
        ),
        "scent": "Tea Tree & Mint",
        "scent_family": "Fresh",
        "skin_types": ["Oily", "Acne-Prone", "Combination"],
        "weight": "4.5 oz",
        "ingredients": [
            "Saponified Coconut Oil", "Olive Oil", "Tea Tree Essential Oil",
            "Activated Charcoal", "Peppermint Essential Oil", "Castor Oil",
        ],
        "image": "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?auto=format&fit=crop&w=600&q=80",
        "badge": None,
        "rating": 4.6,
        "reviews": 178,
    },
    {
        "id": 8,
        "name": "Coconut Milk & Honey",
        "tagline": "Tropical moisture for parched skin",
        "price": 14.00,
        "description": (
            "Creamy coconut milk and wildflower honey combine in this ultra-moisturizing bar. "
            "It lathers into a rich, silky foam that leaves skin dewy, plump, and "
            "smelling like paradise."
        ),
        "scent": "Coconut & Sweet Honey",
        "scent_family": "Sweet",
        "skin_types": ["Dry", "Sensitive"],
        "weight": "4.5 oz",
        "ingredients": [
            "Saponified Coconut Oil", "Olive Oil", "Coconut Milk",
            "Raw Wildflower Honey", "Shea Butter", "Cocoa Butter",
        ],
        "image": "https://images.unsplash.com/photo-1601004890684-d8cbf643f5f2?auto=format&fit=crop&w=600&q=80",
        "badge": "New",
        "rating": 4.8,
        "reviews": 89,
    },
]

PRODUCTS_BY_ID = {p["id"]: p for p in PRODUCTS}

# ══════════════════════════════════════════════════════════════════
#  CART UTILITIES
# ══════════════════════════════════════════════════════════════════

def init_cart():
    if "cart" not in st.session_state:
        st.session_state.cart = {}

def add_to_cart(product_id: int, qty: int = 1):
    init_cart()
    st.session_state.cart[product_id] = st.session_state.cart.get(product_id, 0) + qty

def remove_from_cart(product_id: int):
    init_cart()
    if product_id in st.session_state.cart:
        del st.session_state.cart[product_id]

def update_qty(product_id: int, qty: int):
    init_cart()
    if qty <= 0:
        remove_from_cart(product_id)
    else:
        st.session_state.cart[product_id] = qty

def cart_count() -> int:
    init_cart()
    return sum(st.session_state.cart.values())

def cart_total() -> float:
    init_cart()
    return sum(
        PRODUCTS_BY_ID[pid]["price"] * qty
        for pid, qty in st.session_state.cart.items()
        if pid in PRODUCTS_BY_ID
    )

# ══════════════════════════════════════════════════════════════════
#  SHARED CSS
# ══════════════════════════════════════════════════════════════════

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&display=swap');

/* ─── RESETS ─────────────────────────────────────────────────── */
#MainMenu, footer, header { visibility: hidden !important; }
.stDeployButton { display: none !important; }
[data-testid="stSidebarNav"] { display: none !important; }
[data-testid="stSidebar"] { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }

html, body { scroll-behavior: smooth; }

.stApp {
    background-color: #FFF8EE !important;
    font-family: 'DM Sans', sans-serif;
    color: #2C1A0E;
}

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

div[data-testid="stVerticalBlock"] > div {
    width: 100%;
}

/* ─── NAV ────────────────────────────────────────────────────── */
.bee-nav {
    background: #1A0E05;
    padding: 1rem 4rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 9999;
    box-shadow: 0 2px 24px rgba(0,0,0,0.35);
}
.bee-logo {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: #F0C060;
    letter-spacing: 0.04em;
    text-decoration: none;
    white-space: nowrap;
}
.bee-logo span { color: #C9922A; }
.bee-nav-links {
    display: flex;
    gap: 2.5rem;
    list-style: none;
    margin: 0;
    padding: 0;
    align-items: center;
}
.bee-nav-links a {
    color: rgba(255,248,238,0.82);
    text-decoration: none;
    font-size: 0.88rem;
    font-weight: 500;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    transition: color 0.2s;
}
.bee-nav-links a:hover { color: #F0C060; }
.cart-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: #C9922A;
    color: white;
    border-radius: 50%;
    width: 20px;
    height: 20px;
    font-size: 0.7rem;
    font-weight: 700;
    margin-left: 0.3rem;
    vertical-align: middle;
}

/* ─── HERO ───────────────────────────────────────────────────── */
.bee-hero {
    background: linear-gradient(155deg, #0F0600 0%, #2C1006 30%, #5C2810 62%, #C9922A 100%);
    min-height: 90vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 7rem 2rem 6rem;
    position: relative;
    overflow: hidden;
}
.bee-hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: radial-gradient(circle at 70% 40%, rgba(201,146,42,0.12) 0%, transparent 60%),
                      radial-gradient(circle at 20% 80%, rgba(201,146,42,0.08) 0%, transparent 50%);
    pointer-events: none;
}
.bee-hero::after {
    content: '⬡';
    font-size: 28rem;
    color: rgba(240,192,96,0.04);
    position: absolute;
    right: -6rem;
    top: -8rem;
    line-height: 1;
    pointer-events: none;
    font-family: sans-serif;
}
.hero-inner { position: relative; z-index: 1; max-width: 780px; margin: 0 auto; }
.hero-badge {
    display: inline-block;
    background: rgba(201,146,42,0.18);
    border: 1px solid rgba(240,192,96,0.35);
    color: #F0C060;
    padding: 0.45rem 1.4rem;
    border-radius: 50px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    margin-bottom: 2rem;
}
.hero-headline {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3rem, 6.5vw, 5.8rem);
    font-weight: 700;
    color: #FFF8EE;
    line-height: 1.08;
    margin: 0 0 1.6rem;
    letter-spacing: -0.01em;
}
.hero-headline em { color: #F0C060; font-style: italic; }
.hero-sub {
    font-size: 1.12rem;
    color: rgba(255,248,238,0.7);
    max-width: 520px;
    margin: 0 auto 3rem;
    line-height: 1.75;
    font-weight: 300;
}
.hero-cta-row {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
}
.btn-honey {
    background: #C9922A;
    color: #FFF8EE;
    padding: 0.95rem 2.6rem;
    border-radius: 50px;
    font-family: 'DM Sans', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    text-decoration: none;
    border: none;
    cursor: pointer;
    transition: all 0.25s;
    letter-spacing: 0.03em;
    display: inline-block;
    box-shadow: 0 4px 24px rgba(201,146,42,0.3);
}
.btn-honey:hover {
    background: #B07A1F;
    transform: translateY(-3px);
    box-shadow: 0 10px 32px rgba(201,146,42,0.45);
    color: white;
}
.btn-ghost {
    background: transparent;
    color: rgba(255,248,238,0.88);
    padding: 0.95rem 2.6rem;
    border-radius: 50px;
    font-family: 'DM Sans', sans-serif;
    font-size: 1rem;
    font-weight: 500;
    text-decoration: none;
    border: 1.5px solid rgba(255,248,238,0.3);
    cursor: pointer;
    transition: all 0.25s;
    display: inline-block;
}
.btn-ghost:hover {
    border-color: #F0C060;
    color: #F0C060;
}

/* ─── SCENT MARQUEE ──────────────────────────────────────────── */
.scent-strip {
    background: #C9922A;
    padding: 1rem 0;
    display: flex;
    gap: 0;
    overflow: hidden;
}
.scent-track {
    display: flex;
    gap: 3rem;
    padding: 0 3rem;
    align-items: center;
    white-space: nowrap;
    animation: marquee 28s linear infinite;
    flex-shrink: 0;
}
@keyframes marquee {
    from { transform: translateX(0); }
    to { transform: translateX(-50%); }
}
.scent-item {
    color: rgba(255,248,238,0.92);
    font-size: 0.82rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
}
.scent-dot {
    color: rgba(255,248,238,0.35);
    font-size: 1.2rem;
}

/* ─── SECTION LAYOUT ─────────────────────────────────────────── */
.section {
    padding: 5.5rem 4rem;
    max-width: 1200px;
    margin: 0 auto;
}
.section-wide { padding: 5.5rem 4rem; }
.section-center { text-align: center; }
.section-center .section-sub { margin: 0 auto; }
.section-tag {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #C9922A;
    margin-bottom: 0.7rem;
}
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2rem, 3.5vw, 2.9rem);
    font-weight: 700;
    color: #2C1A0E;
    line-height: 1.18;
    margin: 0 0 0.9rem;
}
.section-title em { color: #C9922A; font-style: italic; }
.honey-rule {
    width: 56px;
    height: 3px;
    background: linear-gradient(90deg, #C9922A, #F0C060);
    border-radius: 2px;
    margin: 0.8rem 0 1.5rem;
}
.section-center .honey-rule { margin: 0.8rem auto 1.5rem; }
.section-sub {
    font-size: 0.98rem;
    color: #6B4226;
    line-height: 1.75;
    max-width: 580px;
}

/* ─── PRODUCT CARDS ──────────────────────────────────────────── */
.product-card {
    background: #FFFFFF;
    border-radius: 22px;
    overflow: hidden;
    box-shadow: 0 4px 28px rgba(44,26,14,0.08);
    transition: transform 0.32s ease, box-shadow 0.32s ease;
}
.product-card:hover {
    transform: translateY(-7px);
    box-shadow: 0 16px 48px rgba(44,26,14,0.16);
}
.product-img-wrap {
    position: relative;
    overflow: hidden;
    height: 270px;
    background: linear-gradient(135deg, #F5EDD9, #EDE0C4);
}
.product-img-wrap img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.45s ease;
    display: block;
}
.product-card:hover .product-img-wrap img { transform: scale(1.07); }
.product-badge {
    position: absolute;
    top: 14px;
    left: 14px;
    background: #C9922A;
    color: white;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    padding: 0.32rem 0.85rem;
    border-radius: 50px;
    box-shadow: 0 2px 8px rgba(201,146,42,0.4);
}
.product-body { padding: 1.5rem 1.6rem 1rem; }
.product-scent-tag {
    font-size: 0.7rem;
    color: #C9922A;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}
.product-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.18rem;
    font-weight: 600;
    color: #2C1A0E;
    margin: 0 0 0.4rem;
    line-height: 1.3;
}
.product-tagline {
    font-size: 0.86rem;
    color: #8B5E3C;
    line-height: 1.55;
    margin-bottom: 1.1rem;
}
.product-meta {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 0.2rem;
}
.product-price {
    font-size: 1.28rem;
    font-weight: 700;
    color: #2C1A0E;
    font-family: 'DM Sans', sans-serif;
}
.product-rating { font-size: 0.8rem; color: #8B5E3C; }
.product-rating .stars { color: #C9922A; }

/* ─── STREAMLIT BUTTON OVERRIDES ────────────────────────────── */
.stButton > button {
    background: linear-gradient(135deg, #C9922A 0%, #D4A544 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 50px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    padding: 0.65rem 1.5rem !important;
    letter-spacing: 0.04em !important;
    transition: all 0.22s !important;
    width: 100% !important;
    box-shadow: 0 2px 12px rgba(201,146,42,0.22) !important;
    cursor: pointer !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #B07A1F 0%, #C9922A 100%) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(201,146,42,0.38) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ─── WHY CHOOSE US ──────────────────────────────────────────── */
.why-band {
    background: linear-gradient(160deg, #1A0E05 0%, #2C1A0E 60%, #3D2010 100%);
    padding: 5.5rem 4rem;
}
.why-card { text-align: center; padding: 2rem 1.5rem; }
.why-icon { font-size: 3rem; margin-bottom: 1.2rem; display: block; }
.why-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
    font-weight: 600;
    color: #F0C060;
    margin-bottom: 0.7rem;
}
.why-text {
    font-size: 0.87rem;
    color: rgba(255,248,238,0.65);
    line-height: 1.7;
}
.why-band .section-title { color: #FFF8EE; }
.why-band .section-title em { color: #F0C060; }
.why-band .section-tag { color: rgba(240,192,96,0.75); }

/* ─── TESTIMONIALS ───────────────────────────────────────────── */
.testimonial-band {
    background: linear-gradient(135deg, #F5E8CC 0%, #FFF8EE 50%, #F5E8CC 100%);
    padding: 5.5rem 4rem;
}
.testimonial-card {
    background: white;
    border-radius: 22px;
    padding: 2rem 1.8rem;
    box-shadow: 0 4px 28px rgba(44,26,14,0.07);
    height: 100%;
    border-bottom: 4px solid #C9922A;
}
.testimonial-stars { color: #C9922A; font-size: 1rem; margin-bottom: 1.1rem; }
.testimonial-text {
    font-family: 'Playfair Display', serif;
    font-size: 1.02rem;
    font-style: italic;
    color: #2C1A0E;
    line-height: 1.72;
    margin-bottom: 1.6rem;
}
.testimonial-author { display: flex; align-items: center; gap: 0.8rem; }
.t-avatar {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    background: linear-gradient(135deg, #C9922A, #F0C060);
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: 700;
    font-size: 1rem;
    flex-shrink: 0;
}
.t-name { font-weight: 600; font-size: 0.88rem; color: #2C1A0E; }
.t-loc { font-size: 0.78rem; color: #8B5E3C; }

/* ─── STORY SPLIT ────────────────────────────────────────────── */
.story-img {
    border-radius: 24px;
    overflow: hidden;
    height: 520px;
    box-shadow: 0 12px 48px rgba(44,26,14,0.16);
}
.story-img img { width: 100%; height: 100%; object-fit: cover; display: block; }

/* ─── NEWSLETTER ─────────────────────────────────────────────── */
.newsletter-band {
    background: #C9922A;
    padding: 4.5rem 4rem;
    text-align: center;
}
.newsletter-band .section-title { color: white; }
.newsletter-band .section-title em { color: #FFF8EE; font-style: italic; }
.newsletter-band .section-sub { color: rgba(255,255,255,0.8); margin: 0 auto; }
.newsletter-band .honey-rule { background: linear-gradient(90deg, rgba(255,255,255,0.5), white); margin: 0 auto 1.5rem; }

/* ─── PAGE HEADER ────────────────────────────────────────────── */
.page-header {
    background: linear-gradient(150deg, #0F0600 0%, #2C1006 45%, #6B3515 100%);
    padding: 5rem 4rem 4.5rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.page-header::after {
    content: '⬡';
    font-size: 22rem;
    color: rgba(201,146,42,0.05);
    position: absolute;
    right: -4rem;
    top: -6rem;
    line-height: 1;
    pointer-events: none;
}
.page-header-tag { font-size: 0.72rem; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: rgba(240,192,96,0.75); margin-bottom: 0.7rem; }
.page-header-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.2rem, 4.5vw, 3.8rem);
    font-weight: 700;
    color: #FFF8EE;
    line-height: 1.15;
    position: relative; z-index: 1;
}
.page-header-title em { color: #F0C060; font-style: italic; }
.page-header-sub {
    font-size: 1rem;
    color: rgba(255,248,238,0.65);
    margin-top: 0.8rem;
    position: relative; z-index: 1;
}

/* ─── PRODUCT DETAIL EXPAND ──────────────────────────────────── */
.ingredient-chip {
    display: inline-block;
    background: #F5E6C8;
    color: #6B3515;
    padding: 0.3rem 0.85rem;
    border-radius: 50px;
    font-size: 0.8rem;
    font-weight: 500;
    margin: 0.25rem;
}
.skin-chip {
    display: inline-block;
    background: #E8F5EE;
    color: #2D6A4F;
    padding: 0.3rem 0.85rem;
    border-radius: 50px;
    font-size: 0.8rem;
    font-weight: 500;
    margin: 0.25rem;
}

/* ─── ABOUT PAGE ─────────────────────────────────────────────── */
.value-card {
    background: white;
    border-radius: 22px;
    padding: 2.2rem 1.8rem;
    text-align: center;
    box-shadow: 0 4px 28px rgba(44,26,14,0.07);
    height: 100%;
    transition: transform 0.28s ease;
}
.value-card:hover { transform: translateY(-5px); }
.value-icon { font-size: 2.8rem; margin-bottom: 1.1rem; display: block; }
.value-title { font-family: 'Playfair Display', serif; font-size: 1.12rem; font-weight: 600; color: #2C1A0E; margin-bottom: 0.6rem; }
.value-text { font-size: 0.87rem; color: #6B4226; line-height: 1.67; }
.process-step { display: flex; gap: 1.5rem; margin-bottom: 2.8rem; align-items: flex-start; }
.step-num {
    width: 52px; height: 52px;
    background: linear-gradient(135deg, #C9922A, #F0C060);
    color: white;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Playfair Display', serif;
    font-size: 1.25rem; font-weight: 700; flex-shrink: 0;
    box-shadow: 0 4px 16px rgba(201,146,42,0.3);
}
.step-body h4 { font-family: 'Playfair Display', serif; font-size: 1.08rem; color: #2C1A0E; margin: 0 0 0.4rem; }
.step-body p { font-size: 0.88rem; color: #6B4226; line-height: 1.67; margin: 0; }

/* ─── CONTACT PAGE ───────────────────────────────────────────── */
.contact-info-card {
    background: linear-gradient(155deg, #2C1A0E, #1A0E05);
    border-radius: 22px;
    padding: 2.5rem 2rem;
    color: #FFF8EE;
}
.contact-item { display: flex; gap: 1rem; margin-bottom: 2rem; align-items: flex-start; }
.contact-icon { font-size: 1.6rem; flex-shrink: 0; margin-top: 0.1rem; }
.contact-item-title { font-weight: 600; font-size: 0.92rem; color: #F0C060; margin-bottom: 0.2rem; }
.contact-item-val { font-size: 0.88rem; color: rgba(255,248,238,0.7); line-height: 1.6; }
.faq-item { background: white; border-radius: 16px; padding: 1.5rem 1.6rem; box-shadow: 0 2px 16px rgba(44,26,14,0.06); margin-bottom: 0.8rem; }
.faq-q { font-family: 'Playfair Display', serif; font-size: 0.98rem; font-weight: 600; color: #2C1A0E; margin-bottom: 0.5rem; }
.faq-a { font-size: 0.86rem; color: #6B4226; line-height: 1.67; margin: 0; }

/* ─── CART PAGE ──────────────────────────────────────────────── */
.cart-item-card {
    background: white;
    border-radius: 18px;
    padding: 1.4rem 1.6rem;
    box-shadow: 0 2px 20px rgba(44,26,14,0.07);
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 1.5rem;
}
.cart-item-img { width: 88px; height: 88px; border-radius: 12px; object-fit: cover; flex-shrink: 0; }
.cart-item-name { font-family: 'Playfair Display', serif; font-size: 1.05rem; font-weight: 600; color: #2C1A0E; margin-bottom: 0.25rem; }
.cart-item-scent { font-size: 0.78rem; color: #C9922A; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; }
.cart-item-price { font-size: 1.1rem; font-weight: 700; color: #2C1A0E; margin-left: auto; white-space: nowrap; }
.order-box {
    background: linear-gradient(155deg, #2C1A0E 0%, #1A0E05 100%);
    border-radius: 22px;
    padding: 2.2rem;
    color: #FFF8EE;
}
.order-box-title { font-family: 'Playfair Display', serif; font-size: 1.3rem; color: #F0C060; margin-bottom: 1.5rem; }
.order-row { display: flex; justify-content: space-between; font-size: 0.88rem; margin-bottom: 0.75rem; color: rgba(255,248,238,0.75); }
.order-total { border-top: 1px solid rgba(255,248,238,0.12); padding-top: 1rem; margin-top: 0.5rem; font-size: 1.1rem; font-weight: 700; color: #F0C060; display: flex; justify-content: space-between; }
.checkout-form { background: white; border-radius: 22px; padding: 2.2rem; box-shadow: 0 4px 28px rgba(44,26,14,0.08); margin-top: 1.5rem; }
.checkout-form h3 { font-family: 'Playfair Display', serif; font-size: 1.2rem; color: #2C1A0E; margin-bottom: 1.5rem; }
.empty-cart { text-align: center; padding: 5rem 2rem; color: #8B5E3C; }
.empty-cart-icon { font-size: 4rem; display: block; margin-bottom: 1rem; }
.empty-cart h3 { font-family: 'Playfair Display', serif; font-size: 1.6rem; color: #2C1A0E; margin-bottom: 0.6rem; }
.empty-cart p { font-size: 0.95rem; line-height: 1.65; }

/* ─── FOOTER ─────────────────────────────────────────────────── */
.bee-footer {
    background: #100802;
    color: rgba(255,248,238,0.65);
    padding: 5rem 4rem 2.5rem;
}
.footer-logo { font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 700; color: #F0C060; margin-bottom: 0.8rem; }
.footer-tagline { font-size: 0.86rem; line-height: 1.68; max-width: 250px; margin-bottom: 1.8rem; }
.footer-head { font-size: 0.7rem; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: #C9922A; margin-bottom: 1.2rem; }
.footer-links { list-style: none; padding: 0; margin: 0; }
.footer-links li { margin-bottom: 0.65rem; }
.footer-links a { color: rgba(255,248,238,0.58); text-decoration: none; font-size: 0.86rem; transition: color 0.2s; }
.footer-links a:hover { color: #F0C060; }
.footer-social { display: flex; gap: 0.75rem; margin-top: 0.5rem; }
.social-btn {
    width: 38px; height: 38px; border-radius: 50%;
    background: rgba(201,146,42,0.12);
    border: 1px solid rgba(201,146,42,0.28);
    display: flex; align-items: center; justify-content: center;
    color: #C9922A; text-decoration: none; font-size: 1rem;
    transition: all 0.22s;
}
.social-btn:hover { background: #C9922A; color: white; border-color: #C9922A; }
.footer-bottom {
    border-top: 1px solid rgba(255,248,238,0.08);
    margin-top: 4rem; padding-top: 1.8rem;
    font-size: 0.78rem; color: rgba(255,248,238,0.32);
    text-align: center;
}

/* ─── FORM STYLES ────────────────────────────────────────────── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div > select {
    border: 1.5px solid #E8D5B0 !important;
    border-radius: 12px !important;
    background: #FEFAF4 !important;
    font-family: 'DM Sans', sans-serif !important;
    color: #2C1A0E !important;
    font-size: 0.95rem !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #C9922A !important;
    box-shadow: 0 0 0 3px rgba(201,146,42,0.12) !important;
}
.stTextInput label, .stTextArea label, .stSelectbox label, .stNumberInput label {
    font-family: 'DM Sans', sans-serif !important;
    color: #2C1A0E !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
}
.stNumberInput > div > div > input {
    border: 1.5px solid #E8D5B0 !important;
    border-radius: 12px !important;
    background: #FEFAF4 !important;
    font-family: 'DM Sans', sans-serif !important;
    color: #2C1A0E !important;
    text-align: center !important;
}

/* ─── DIVIDER / MISC ─────────────────────────────────────────── */
hr { border-color: #E8D5B0 !important; }
.stSuccess { border-radius: 12px !important; }

/* ─── STREAMLIT COLUMN PADDING ───────────────────────────────── */
div[data-testid="column"] { padding: 0.6rem !important; }

/* ─── SHOP SIDEBAR ───────────────────────────────────────────── */
.filter-panel {
    background: white;
    border-radius: 18px;
    padding: 1.8rem 1.5rem;
    box-shadow: 0 4px 24px rgba(44,26,14,0.07);
}
.filter-title { font-family: 'Playfair Display', serif; font-size: 1.1rem; font-weight: 600; color: #2C1A0E; margin-bottom: 1.4rem; display: flex; align-items: center; gap: 0.5rem; }
.stRadio > label { font-family: 'DM Sans', sans-serif !important; color: #2C1A0E !important; font-weight: 500 !important; }
.stRadio div[role="radiogroup"] { gap: 0.5rem !important; }
.stCheckbox > label { font-family: 'DM Sans', sans-serif !important; color: #2C1A0E !important; }
.stSlider { padding: 0.5rem 0 !important; }
</style>
"""


def load_css():
    st.markdown(CSS, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
#  NAVIGATION
# ══════════════════════════════════════════════════════════════════

def render_nav():
    count = cart_count()
    badge = f'<span class="cart-badge">{count}</span>' if count > 0 else ""
    st.markdown(f"""
<nav class="bee-nav">
  <a class="bee-logo" href="/" target="_self">🐝&nbsp;THEE&nbsp;<span>BEE</span>&nbsp;BOUTIQUE</a>
  <ul class="bee-nav-links">
    <li><a href="/" target="_self">Home</a></li>
    <li><a href="/Shop" target="_self">Shop</a></li>
    <li><a href="/About" target="_self">About</a></li>
    <li><a href="/Contact" target="_self">Contact</a></li>
    <li><a href="/Cart" target="_self">🛒 Cart{badge}</a></li>
  </ul>
</nav>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
#  FOOTER
# ══════════════════════════════════════════════════════════════════

def render_footer():
    st.markdown("""
<div class="bee-footer">
  <div style="max-width:1200px;margin:0 auto;display:grid;grid-template-columns:2.2fr 1fr 1fr 1fr;gap:3.5rem;">
    <div>
      <div class="footer-logo">🐝 Thee Bee Boutique</div>
      <p class="footer-tagline">Handcrafted with love, raw honey, and botanicals. Small-batch soaps made for skin that deserves better.</p>
      <div class="footer-social">
        <a href="#" class="social-btn">📷</a>
        <a href="#" class="social-btn">📌</a>
        <a href="#" class="social-btn">🐦</a>
        <a href="#" class="social-btn">📘</a>
      </div>
    </div>
    <div>
      <div class="footer-head">Shop</div>
      <ul class="footer-links">
        <li><a href="/Shop" target="_self">All Soaps</a></li>
        <li><a href="/Shop" target="_self">Best Sellers</a></li>
        <li><a href="/Shop" target="_self">New Arrivals</a></li>
        <li><a href="/Shop" target="_self">Gift Sets</a></li>
      </ul>
    </div>
    <div>
      <div class="footer-head">Info</div>
      <ul class="footer-links">
        <li><a href="/About" target="_self">Our Story</a></li>
        <li><a href="/About" target="_self">Ingredients</a></li>
        <li><a href="/Contact" target="_self">FAQ</a></li>
        <li><a href="/Contact" target="_self">Shipping</a></li>
      </ul>
    </div>
    <div>
      <div class="footer-head">Connect</div>
      <ul class="footer-links">
        <li><a href="#">hello@thebeeboutique.com</a></li>
        <li><a href="#">@thebeeboutique</a></li>
        <li><a href="#">Returns Policy</a></li>
        <li><a href="#">Privacy Policy</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    © 2025 Thee Bee Boutique &nbsp;·&nbsp; Handcrafted with 🐝 love &nbsp;·&nbsp; All rights reserved
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
#  PRODUCT CARD HELPER
# ══════════════════════════════════════════════════════════════════

def render_product_card(product: dict):
    badge_html = (
        f'<span class="product-badge">{product["badge"]}</span>'
        if product.get("badge") else ""
    )
    stars = "★" * 5
    st.markdown(f"""
<div class="product-card">
  <div class="product-img-wrap">
    <img src="{product['image']}" alt="{product['name']}" loading="lazy">
    {badge_html}
  </div>
  <div class="product-body">
    <div class="product-scent-tag">{product['scent']}</div>
    <h3 class="product-name">{product['name']}</h3>
    <p class="product-tagline">{product['tagline']}</p>
    <div class="product-meta">
      <span class="product-price">${product['price']:.2f}</span>
      <span class="product-rating"><span class="stars">{stars}</span> {product['rating']} ({product['reviews']})</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
