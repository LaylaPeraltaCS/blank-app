import streamlit as st

# ══════════════════════════════════════════════════════════════════
#  REAL PRODUCT CATALOG — Thee Bee Boutique
# ══════════════════════════════════════════════════════════════════

PRODUCTS = [
    {
        "id": 1,
        "name": "Black Cherry Merlot",
        "tagline": "Bold, rich, and irresistibly fruity",
        "price": 10.00,
        "description": (
            "Inspired by your favorite glass of wine. Dark, juicy cherry and warm merlot "
            "swirl together in a rich lather that leaves skin soft and subtly intoxicating. "
            "A full-bodied bar for people who like to indulge."
        ),
        "scent": "Dark Cherry & Wine",
        "scent_family": "Fruity",
        "skin_types": ["All Types"],
        "weight": "4 oz",
        "ingredients": [
            "Coconut Oil", "Palm Oil", "Safflower Oil", "Glycerin",
            "Shea Butter", "Black Cherry Fragrance", "Kaolin Clay",
        ],
        "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?auto=format&fit=crop&w=600&q=80",
        "badge": "Fan Favorite",
        "rating": 4.9,
        "reviews": 187,
        "color": "#7B1E2C",
    },
    {
        "id": 2,
        "name": "Bee Loved",
        "tagline": "Sweet honey from the hive to your skin",
        "price": 8.00,
        "description": (
            "Our signature honey bar — raw wildflower honey blended with almond oil and "
            "a touch of beeswax for a deeply nourishing cleanse. Every wash feels like a "
            "little reminder that your skin deserves love."
        ),
        "scent": "Raw Honey & Almond",
        "scent_family": "Sweet",
        "skin_types": ["All Types", "Sensitive"],
        "weight": "4 oz",
        "ingredients": [
            "Coconut Oil", "Olive Oil", "Raw Wildflower Honey", "Beeswax",
            "Sweet Almond Oil", "Shea Butter", "Vitamin E",
        ],
        "image": "https://images.unsplash.com/photo-1600857062241-98e5dba7f025?auto=format&fit=crop&w=600&q=80",
        "badge": "Signature",
        "rating": 5.0,
        "reviews": 243,
        "color": "#C9922A",
    },
    {
        "id": 3,
        "name": "Love Letter",
        "tagline": "A little romance for your everyday routine",
        "price": 8.00,
        "description": (
            "Soft florals and a hint of musk make this bar feel like receiving flowers "
            "every morning. Gentle enough for daily use, beautiful enough to give as a gift. "
            "Your skin will write back."
        ),
        "scent": "Floral Musk & Rose",
        "scent_family": "Floral",
        "skin_types": ["Normal", "Dry", "Sensitive"],
        "weight": "4 oz",
        "ingredients": [
            "Coconut Oil", "Olive Oil", "Shea Butter", "Rose Fragrance Oil",
            "Musk Fragrance", "Cocoa Butter", "Rose Kaolin Clay",
        ],
        "image": "https://images.unsplash.com/photo-1582731478119-6f59f7ac01b7?auto=format&fit=crop&w=600&q=80",
        "badge": "Gift Favorite",
        "rating": 4.8,
        "reviews": 156,
        "color": "#C47A8A",
    },
    {
        "id": 4,
        "name": "Be Still Queen",
        "tagline": "Regal. Grounding. Made for you.",
        "price": 10.00,
        "description": (
            "A sophisticated blend of warm wood, soft amber, and a kiss of vanilla. "
            "This bar was made for the woman who knows her worth. Cleanse with intention, "
            "step out glowing."
        ),
        "scent": "Amber, Sandalwood & Vanilla",
        "scent_family": "Woody",
        "skin_types": ["All Types", "Dry"],
        "weight": "4 oz",
        "ingredients": [
            "Coconut Oil", "Castor Oil", "Shea Butter", "Amber Fragrance",
            "Sandalwood Essential Oil", "Vanilla Extract", "Gold Mica",
        ],
        "image": "https://images.unsplash.com/photo-1607001486043-2b4e2db7d8b5?auto=format&fit=crop&w=600&q=80",
        "badge": "Best Seller",
        "rating": 4.9,
        "reviews": 312,
        "color": "#8B5E3C",
    },
    {
        "id": 5,
        "name": "Honey Almond",
        "tagline": "Soft, sweet, and impossibly creamy",
        "price": 7.50,
        "description": (
            "A classic combination that never gets old. Raw honey and sweet almond oil "
            "create a bar that lathers rich and rinses clean, leaving skin feeling "
            "nourished and smelling like a dream."
        ),
        "scent": "Sweet Honey & Almond",
        "scent_family": "Sweet",
        "skin_types": ["All Types", "Sensitive", "Dry"],
        "weight": "4 oz",
        "ingredients": [
            "Coconut Oil", "Olive Oil", "Raw Honey", "Sweet Almond Oil",
            "Shea Butter", "Almond Fragrance Oil", "Vitamin E",
        ],
        "image": "https://images.unsplash.com/photo-1601004890684-d8cbf643f5f2?auto=format&fit=crop&w=600&q=80",
        "badge": None,
        "rating": 4.8,
        "reviews": 198,
        "color": "#D4A030",
    },
    {
        "id": 6,
        "name": "Orange Turmeric",
        "tagline": "Brightening power meets citrus joy",
        "price": 8.00,
        "description": (
            "Turmeric has been a skin secret for centuries, and we brought it into your "
            "shower. Paired with zesty sweet orange, this bar brightens, evens skin tone, "
            "and energizes your entire morning."
        ),
        "scent": "Sweet Orange & Turmeric",
        "scent_family": "Citrus",
        "skin_types": ["All Types", "Oily", "Dull Skin"],
        "weight": "4 oz",
        "ingredients": [
            "Coconut Oil", "Olive Oil", "Turmeric Powder", "Sweet Orange Essential Oil",
            "Shea Butter", "Castor Oil", "Vitamin E",
        ],
        "image": "https://images.unsplash.com/photo-1547592180-85f173d888a4?auto=format&fit=crop&w=600&q=80",
        "badge": "Glow Getter",
        "rating": 4.7,
        "reviews": 134,
        "color": "#E07020",
    },
    {
        "id": 7,
        "name": "Lavender Unwind Bar",
        "tagline": "Your sign to slow down and breathe",
        "price": 5.00,
        "description": (
            "Pure lavender essential oil meets a gentle, creamy base to create the perfect "
            "wind-down bar. Use it at night to signal your body it's time to rest. "
            "Simple. Calming. Perfect."
        ),
        "scent": "True Lavender",
        "scent_family": "Floral",
        "skin_types": ["All Types", "Sensitive"],
        "weight": "3.5 oz",
        "ingredients": [
            "Coconut Oil", "Olive Oil", "Lavender Essential Oil",
            "Shea Butter", "Lavender Buds", "Castor Oil",
        ],
        "image": "https://images.unsplash.com/photo-1611241893603-3c359704e0ee?auto=format&fit=crop&w=600&q=80",
        "badge": None,
        "rating": 4.8,
        "reviews": 221,
        "color": "#8A6FAE",
    },
    {
        "id": 8,
        "name": "Vanilla Bourbon",
        "tagline": "Warm, smooth, and dangerously good",
        "price": 10.00,
        "description": (
            "Rich vanilla bean and a hint of bourbon create a bar that smells like "
            "your favorite cozy evening. Ultra-moisturizing and long-lasting, "
            "this one leaves your skin velvety smooth."
        ),
        "scent": "Vanilla Bean & Bourbon",
        "scent_family": "Sweet",
        "skin_types": ["Dry", "Normal"],
        "weight": "4 oz",
        "ingredients": [
            "Coconut Oil", "Castor Oil", "Cocoa Butter", "Vanilla Extract",
            "Bourbon Fragrance Oil", "Shea Butter", "Vitamin E",
        ],
        "image": "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?auto=format&fit=crop&w=600&q=80",
        "badge": None,
        "rating": 4.9,
        "reviews": 89,
        "color": "#7A3C20",
    },
    {
        "id": 9,
        "name": "Sangria Bar",
        "tagline": "Fruity, festive, and unforgettable",
        "price": 10.00,
        "description": (
            "Summer in a bar — bright citrus, deep berry, and a hint of wine. "
            "This vibrant soap is as fun to use as it sounds. Perfect for gifting "
            "or treating yourself."
        ),
        "scent": "Citrus, Berry & Wine",
        "scent_family": "Fruity",
        "skin_types": ["All Types"],
        "weight": "4 oz",
        "ingredients": [
            "Coconut Oil", "Olive Oil", "Sangria Fragrance Oil",
            "Kaolin Clay", "Shea Butter", "Castor Oil", "Red Mica",
        ],
        "image": "https://images.unsplash.com/photo-1576426863848-c21f53c60b19?auto=format&fit=crop&w=600&q=80",
        "badge": "Party Pick",
        "rating": 4.7,
        "reviews": 76,
        "color": "#922040",
    },
    {
        "id": 10,
        "name": "Apple & Spice",
        "tagline": "Cozy season all year long",
        "price": 10.00,
        "description": (
            "Crisp apple and warm spice come together in a bar that smells like "
            "the best parts of fall. Whether it's October or July, this soap makes "
            "every shower feel like a sweater and a warm mug."
        ),
        "scent": "Crisp Apple & Cinnamon",
        "scent_family": "Spiced",
        "skin_types": ["All Types", "Normal"],
        "weight": "4 oz",
        "ingredients": [
            "Coconut Oil", "Olive Oil", "Apple Fragrance Oil",
            "Cinnamon Fragrance", "Shea Butter", "Castor Oil",
        ],
        "image": "https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?auto=format&fit=crop&w=600&q=80",
        "badge": None,
        "rating": 4.8,
        "reviews": 103,
        "color": "#C04020",
    },
    {
        "id": 11,
        "name": "Pumpkin Spice",
        "tagline": "The one you've been waiting for all year",
        "price": 10.00,
        "description": (
            "Yes, we went there — and we're not sorry. Warm pumpkin, cinnamon, "
            "nutmeg, and clove in a creamy, skin-loving bar. The fall soap you "
            "didn't know you needed until right now."
        ),
        "scent": "Pumpkin, Cinnamon & Clove",
        "scent_family": "Spiced",
        "skin_types": ["All Types", "Normal"],
        "weight": "4 oz",
        "ingredients": [
            "Coconut Oil", "Olive Oil", "Pumpkin Puree", "Cinnamon",
            "Clove Bud Essential Oil", "Shea Butter", "Nutmeg",
        ],
        "image": "https://images.unsplash.com/photo-1508736793122-f516e3ba5569?auto=format&fit=crop&w=600&q=80",
        "badge": "Seasonal",
        "rating": 4.9,
        "reviews": 145,
        "color": "#C06018",
    },
    {
        "id": 12,
        "name": "Vanilla Snowflake",
        "tagline": "Pure, soft, and delicately sweet",
        "price": 5.00,
        "description": (
            "Light, creamy vanilla with the freshness of a clean winter day. "
            "A gentle everyday bar that's perfect for all skin types — especially "
            "soft-scent lovers who want something understated and beautiful."
        ),
        "scent": "Soft Vanilla & Clean Musk",
        "scent_family": "Sweet",
        "skin_types": ["All Types", "Sensitive"],
        "weight": "3.5 oz",
        "ingredients": [
            "Coconut Oil", "Olive Oil", "Vanilla Fragrance Oil",
            "Shea Butter", "Castor Oil", "White Kaolin Clay",
        ],
        "image": "https://images.unsplash.com/photo-1614930350659-51d9af07d1e2?auto=format&fit=crop&w=600&q=80",
        "badge": None,
        "rating": 4.7,
        "reviews": 88,
        "color": "#E8DECE",
    },
    {
        "id": 13,
        "name": "Brewski",
        "tagline": "Coffee + soap = the best morning ever",
        "price": 10.00,
        "description": (
            "Ground coffee, rich espresso fragrance, and a hint of dark chocolate "
            "make this bar a morning ritual. The coffee grounds gently exfoliate while "
            "the scent wakes you all the way up. No mug required."
        ),
        "scent": "Espresso & Dark Chocolate",
        "scent_family": "Earthy",
        "skin_types": ["All Types", "Oily"],
        "weight": "4 oz",
        "ingredients": [
            "Coconut Oil", "Olive Oil", "Ground Coffee", "Espresso Fragrance",
            "Cocoa Powder", "Shea Butter", "Castor Oil",
        ],
        "image": "https://images.unsplash.com/photo-1559715745-e1b33a271d2b?auto=format&fit=crop&w=600&q=80",
        "badge": "Morning Must",
        "rating": 4.8,
        "reviews": 211,
        "color": "#3C2010",
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
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400;1,600&display=swap');

/* ─── RESETS ─────────────────────────────────────────────────── */
#MainMenu, footer, header { visibility: hidden !important; }
.stDeployButton { display: none !important; }
[data-testid="stSidebarNav"] { display: none !important; }
[data-testid="stSidebar"] { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }

html, body { scroll-behavior: smooth; }

.stApp {
    background-color: #FAF5EE !important;
    font-family: 'DM Sans', sans-serif;
    color: #1A0808;
}

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ─── NAV ────────────────────────────────────────────────────── */
.bee-nav {
    background: #0F0505;
    padding: 1.1rem 4rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 9999;
    box-shadow: 0 2px 30px rgba(0,0,0,0.4);
    border-bottom: 1px solid rgba(201,146,42,0.15);
}
.bee-logo {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.65rem;
    font-weight: 600;
    color: #F0C060;
    letter-spacing: 0.06em;
    text-decoration: none;
    white-space: nowrap;
}
.bee-logo em { color: #C9922A; font-style: italic; }
.bee-nav-links {
    display: flex;
    gap: 2.8rem;
    list-style: none;
    margin: 0; padding: 0;
    align-items: center;
}
.bee-nav-links a {
    color: rgba(255,248,238,0.75);
    text-decoration: none;
    font-size: 0.82rem;
    font-weight: 500;
    letter-spacing: 0.1em;
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
    width: 19px; height: 19px;
    font-size: 0.68rem;
    font-weight: 700;
    margin-left: 0.3rem;
    vertical-align: middle;
}

/* ─── HERO ───────────────────────────────────────────────────── */
.bee-hero {
    background: linear-gradient(155deg, #0F0505 0%, #2C0A10 28%, #5C1A10 58%, #C9922A 100%);
    min-height: 92vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 8rem 2rem 7rem;
    position: relative;
    overflow: hidden;
}
.bee-hero::before {
    content: '';
    position: absolute; inset: 0;
    background-image:
        radial-gradient(circle at 75% 35%, rgba(139,26,44,0.18) 0%, transparent 55%),
        radial-gradient(circle at 20% 75%, rgba(201,146,42,0.1) 0%, transparent 50%);
    pointer-events: none;
}
.bee-hero::after {
    content: '⬡';
    font-size: 30rem;
    color: rgba(240,192,96,0.04);
    position: absolute;
    right: -5rem; top: -9rem;
    line-height: 1;
    pointer-events: none;
}
.hero-inner { position: relative; z-index: 1; max-width: 820px; margin: 0 auto; }
.hero-badge {
    display: inline-block;
    background: rgba(201,146,42,0.15);
    border: 1px solid rgba(240,192,96,0.3);
    color: #F0C060;
    padding: 0.45rem 1.5rem;
    border-radius: 50px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-bottom: 2.2rem;
}
.hero-headline {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(3.2rem, 7vw, 6.4rem);
    font-weight: 600;
    color: #FFF8EE;
    line-height: 1.05;
    margin: 0 0 1.8rem;
    letter-spacing: -0.01em;
}
.hero-headline em { color: #F0C060; font-style: italic; }
.hero-sub {
    font-size: 1.1rem;
    color: rgba(255,248,238,0.68);
    max-width: 540px;
    margin: 0 auto 2.8rem;
    line-height: 1.8;
    font-weight: 300;
}
.hero-pills {
    display: flex;
    gap: 0.75rem;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 3rem;
}
.hero-pill {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    color: rgba(255,248,238,0.7);
    padding: 0.35rem 1rem;
    border-radius: 50px;
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.06em;
}
.hero-cta-row { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
.btn-honey {
    background: #C9922A;
    color: #FFF8EE;
    padding: 1rem 2.8rem;
    border-radius: 50px;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.96rem;
    font-weight: 600;
    text-decoration: none;
    border: none;
    cursor: pointer;
    transition: all 0.25s;
    letter-spacing: 0.04em;
    display: inline-block;
    box-shadow: 0 4px 24px rgba(201,146,42,0.32);
}
.btn-honey:hover {
    background: #B07A1F;
    transform: translateY(-3px);
    box-shadow: 0 10px 32px rgba(201,146,42,0.48);
    color: white;
}
.btn-ghost {
    background: transparent;
    color: rgba(255,248,238,0.85);
    padding: 1rem 2.8rem;
    border-radius: 50px;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.96rem;
    font-weight: 500;
    text-decoration: none;
    border: 1.5px solid rgba(255,248,238,0.28);
    cursor: pointer;
    transition: all 0.25s;
    display: inline-block;
}
.btn-ghost:hover { border-color: #F0C060; color: #F0C060; }

/* ─── SCENT MARQUEE ──────────────────────────────────────────── */
.scent-strip {
    background: #C9922A;
    padding: 0.9rem 0;
    overflow: hidden;
    display: flex;
}
.scent-track {
    display: flex;
    gap: 3.5rem;
    padding: 0 3.5rem;
    align-items: center;
    white-space: nowrap;
    animation: marquee 30s linear infinite;
    flex-shrink: 0;
}
@keyframes marquee {
    from { transform: translateX(0); }
    to { transform: translateX(-50%); }
}
.scent-item {
    color: rgba(255,248,238,0.92);
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
}
.scent-dot { color: rgba(255,248,238,0.3); }

/* ─── SECTION LAYOUT ─────────────────────────────────────────── */
.section { padding: 5.5rem 4rem; max-width: 1200px; margin: 0 auto; }
.section-wide { padding: 5.5rem 4rem; }
.section-center { text-align: center; }
.section-center .section-sub { margin: 0 auto; }
.section-center .honey-rule { margin: 0.8rem auto 1.5rem; }
.section-tag {
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #C9922A;
    margin-bottom: 0.7rem;
}
.section-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2.1rem, 3.8vw, 3.1rem);
    font-weight: 600;
    color: #1A0808;
    line-height: 1.15;
    margin: 0 0 0.9rem;
}
.section-title em { color: #C9922A; font-style: italic; }
.honey-rule {
    width: 52px; height: 3px;
    background: linear-gradient(90deg, #8B1A2C, #C9922A, #F0C060);
    border-radius: 2px;
    margin: 0.8rem 0 1.5rem;
}
.section-sub { font-size: 0.96rem; color: #6B3030; line-height: 1.78; max-width: 580px; }

/* ─── PRODUCT CARDS ──────────────────────────────────────────── */
.product-card {
    background: #FFFFFF;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 4px 28px rgba(26,8,8,0.09);
    transition: transform 0.32s ease, box-shadow 0.32s ease;
}
.product-card:hover {
    transform: translateY(-7px);
    box-shadow: 0 16px 48px rgba(26,8,8,0.17);
}
.product-img-wrap {
    position: relative;
    overflow: hidden;
    height: 260px;
    background: linear-gradient(135deg, #F5EDD9, #EDE0C4);
}
.product-img-wrap img {
    width: 100%; height: 100%;
    object-fit: cover;
    transition: transform 0.45s ease;
    display: block;
}
.product-card:hover .product-img-wrap img { transform: scale(1.07); }
.product-badge {
    position: absolute;
    top: 14px; left: 14px;
    background: #8B1A2C;
    color: white;
    font-size: 0.66rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 0.3rem 0.85rem;
    border-radius: 50px;
    box-shadow: 0 2px 10px rgba(139,26,44,0.4);
}
.badge-gold { background: #C9922A !important; }
.product-body { padding: 1.4rem 1.5rem 1rem; }
.product-scent-tag {
    font-size: 0.68rem;
    color: #C9922A;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 0.35rem;
}
.product-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.25rem;
    font-weight: 600;
    color: #1A0808;
    margin: 0 0 0.4rem;
    line-height: 1.25;
}
.product-tagline { font-size: 0.84rem; color: #8B4040; line-height: 1.55; margin-bottom: 1.1rem; }
.product-meta { display: flex; align-items: center; justify-content: space-between; }
.product-price { font-size: 1.22rem; font-weight: 700; color: #1A0808; }
.product-rating { font-size: 0.78rem; color: #8B4040; }
.product-rating .stars { color: #C9922A; }

/* ─── STREAMLIT BUTTON ───────────────────────────────────────── */
.stButton > button {
    background: linear-gradient(135deg, #8B1A2C 0%, #C9922A 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 50px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.86rem !important;
    padding: 0.65rem 1.5rem !important;
    letter-spacing: 0.04em !important;
    transition: all 0.22s !important;
    width: 100% !important;
    box-shadow: 0 2px 14px rgba(139,26,44,0.22) !important;
    cursor: pointer !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #6B1020 0%, #B07A1F 100%) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 22px rgba(139,26,44,0.38) !important;
}

/* ─── WHY BAND ───────────────────────────────────────────────── */
.why-band {
    background: linear-gradient(160deg, #0F0505 0%, #1A0808 55%, #2C0A10 100%);
    padding: 5.5rem 4rem;
}
.why-card { text-align: center; padding: 2rem 1.5rem; }
.why-icon { font-size: 3rem; margin-bottom: 1.2rem; display: block; }
.why-title { font-family: 'Cormorant Garamond', serif; font-size: 1.2rem; font-weight: 600; color: #F0C060; margin-bottom: 0.7rem; }
.why-text { font-size: 0.86rem; color: rgba(255,248,238,0.6); line-height: 1.72; }
.why-band .section-title { color: #FFF8EE; }
.why-band .section-title em { color: #F0C060; }
.why-band .section-tag { color: rgba(240,192,96,0.7); }

/* ─── TESTIMONIALS ───────────────────────────────────────────── */
.testimonial-band {
    background: linear-gradient(135deg, #F5E0D0 0%, #FAF5EE 50%, #F5E0D0 100%);
    padding: 5.5rem 4rem;
}
.testimonial-card {
    background: white;
    border-radius: 20px;
    padding: 2rem 1.8rem;
    box-shadow: 0 4px 28px rgba(26,8,8,0.08);
    height: 100%;
    border-bottom: 4px solid #8B1A2C;
}
.testimonial-stars { color: #C9922A; font-size: 1rem; margin-bottom: 1.1rem; }
.testimonial-text {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.05rem; font-style: italic;
    color: #1A0808; line-height: 1.75; margin-bottom: 1.6rem;
}
.testimonial-author { display: flex; align-items: center; gap: 0.8rem; }
.t-avatar {
    width: 44px; height: 44px; border-radius: 50%;
    background: linear-gradient(135deg, #8B1A2C, #C9922A);
    display: flex; align-items: center; justify-content: center;
    color: white; font-weight: 700; font-size: 1rem; flex-shrink: 0;
}
.t-name { font-weight: 600; font-size: 0.88rem; color: #1A0808; }
.t-loc { font-size: 0.78rem; color: #8B4040; }

/* ─── STORY IMAGE ────────────────────────────────────────────── */
.story-img {
    border-radius: 24px;
    overflow: hidden; height: 520px;
    box-shadow: 0 14px 56px rgba(26,8,8,0.18);
}
.story-img img { width: 100%; height: 100%; object-fit: cover; display: block; }

/* ─── NEWSLETTER ─────────────────────────────────────────────── */
.newsletter-band {
    background: linear-gradient(135deg, #8B1A2C 0%, #C9922A 100%);
    padding: 5rem 4rem; text-align: center;
}
.newsletter-band .section-title { color: white; }
.newsletter-band .section-title em { color: rgba(255,248,238,0.9); }
.newsletter-band .section-sub { color: rgba(255,255,255,0.78); margin: 0 auto; }
.newsletter-band .honey-rule { background: linear-gradient(90deg, rgba(255,255,255,0.3), rgba(255,255,255,0.7)); margin: 0.8rem auto 1.5rem; }

/* ─── PAGE HEADER ────────────────────────────────────────────── */
.page-header {
    background: linear-gradient(150deg, #0F0505 0%, #2C0A10 40%, #6B1A10 100%);
    padding: 5.5rem 4rem 5rem;
    text-align: center;
    position: relative; overflow: hidden;
}
.page-header::after {
    content: '⬡';
    font-size: 24rem;
    color: rgba(201,146,42,0.05);
    position: absolute; right: -4rem; top: -7rem;
    line-height: 1; pointer-events: none;
}
.page-header-tag { font-size: 0.7rem; font-weight: 700; letter-spacing: 0.22em; text-transform: uppercase; color: rgba(240,192,96,0.72); margin-bottom: 0.7rem; }
.page-header-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2.4rem, 5vw, 4.2rem);
    font-weight: 600; color: #FFF8EE; line-height: 1.1;
    position: relative; z-index: 1;
}
.page-header-title em { color: #F0C060; font-style: italic; }
.page-header-sub { font-size: 0.98rem; color: rgba(255,248,238,0.6); margin-top: 0.8rem; position: relative; z-index: 1; }

/* ─── PRODUCT DETAIL ─────────────────────────────────────────── */
.ingredient-chip {
    display: inline-block;
    background: #F5E0D0; color: #6B2020;
    padding: 0.28rem 0.82rem;
    border-radius: 50px; font-size: 0.78rem; font-weight: 500; margin: 0.22rem;
}
.skin-chip {
    display: inline-block;
    background: #E8F5EE; color: #2D6A4F;
    padding: 0.28rem 0.82rem;
    border-radius: 50px; font-size: 0.78rem; font-weight: 500; margin: 0.22rem;
}

/* ─── ABOUT ──────────────────────────────────────────────────── */
.value-card {
    background: white; border-radius: 20px;
    padding: 2.2rem 1.8rem; text-align: center;
    box-shadow: 0 4px 28px rgba(26,8,8,0.07);
    height: 100%; transition: transform 0.28s;
}
.value-card:hover { transform: translateY(-5px); }
.value-icon { font-size: 2.8rem; margin-bottom: 1rem; display: block; }
.value-title { font-family: 'Cormorant Garamond', serif; font-size: 1.15rem; font-weight: 600; color: #1A0808; margin-bottom: 0.6rem; }
.value-text { font-size: 0.86rem; color: #6B3030; line-height: 1.7; }
.process-step { display: flex; gap: 1.5rem; margin-bottom: 2.8rem; align-items: flex-start; }
.step-num {
    width: 50px; height: 50px;
    background: linear-gradient(135deg, #8B1A2C, #C9922A);
    color: white; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Cormorant Garamond', serif; font-size: 1.25rem; font-weight: 700; flex-shrink: 0;
    box-shadow: 0 4px 16px rgba(139,26,44,0.3);
}
.step-body h4 { font-family: 'Cormorant Garamond', serif; font-size: 1.1rem; color: #1A0808; margin: 0 0 0.4rem; }
.step-body p { font-size: 0.87rem; color: #6B3030; line-height: 1.7; margin: 0; }

/* ─── CONTACT ────────────────────────────────────────────────── */
.contact-info-card {
    background: linear-gradient(155deg, #1A0808, #0F0505);
    border-radius: 20px; padding: 2.5rem 2rem; color: #FFF8EE;
}
.contact-item { display: flex; gap: 1rem; margin-bottom: 2rem; align-items: flex-start; }
.contact-icon { font-size: 1.5rem; flex-shrink: 0; margin-top: 0.1rem; }
.contact-item-title { font-weight: 600; font-size: 0.9rem; color: #F0C060; margin-bottom: 0.2rem; }
.contact-item-val { font-size: 0.86rem; color: rgba(255,248,238,0.65); line-height: 1.62; }
.faq-item { background: white; border-radius: 14px; padding: 1.4rem 1.6rem; box-shadow: 0 2px 16px rgba(26,8,8,0.06); margin-bottom: 0.75rem; }
.faq-q { font-family: 'Cormorant Garamond', serif; font-size: 1rem; font-weight: 600; color: #1A0808; margin-bottom: 0.45rem; }
.faq-a { font-size: 0.86rem; color: #6B3030; line-height: 1.7; margin: 0; }

/* ─── CART ───────────────────────────────────────────────────── */
.cart-item-card {
    background: white; border-radius: 16px;
    padding: 1.4rem 1.6rem; box-shadow: 0 2px 20px rgba(26,8,8,0.07);
    margin-bottom: 1rem; display: flex; align-items: center; gap: 1.5rem;
}
.cart-item-img { width: 86px; height: 86px; border-radius: 12px; object-fit: cover; flex-shrink: 0; }
.cart-item-name { font-family: 'Cormorant Garamond', serif; font-size: 1.08rem; font-weight: 600; color: #1A0808; margin-bottom: 0.25rem; }
.cart-item-scent { font-size: 0.72rem; color: #C9922A; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; }
.cart-item-price { font-size: 1.1rem; font-weight: 700; color: #1A0808; margin-left: auto; white-space: nowrap; }
.order-box {
    background: linear-gradient(155deg, #1A0808 0%, #0F0505 100%);
    border-radius: 20px; padding: 2.2rem; color: #FFF8EE;
}
.order-box-title { font-family: 'Cormorant Garamond', serif; font-size: 1.3rem; color: #F0C060; margin-bottom: 1.5rem; }
.order-row { display: flex; justify-content: space-between; font-size: 0.86rem; margin-bottom: 0.72rem; color: rgba(255,248,238,0.72); }
.order-total { border-top: 1px solid rgba(255,248,238,0.1); padding-top: 1rem; margin-top: 0.5rem; font-size: 1.05rem; font-weight: 700; color: #F0C060; display: flex; justify-content: space-between; }
.empty-cart { text-align: center; padding: 5rem 2rem; color: #8B4040; }
.empty-cart-icon { font-size: 4rem; display: block; margin-bottom: 1rem; }
.empty-cart h3 { font-family: 'Cormorant Garamond', serif; font-size: 1.7rem; color: #1A0808; margin-bottom: 0.6rem; }
.empty-cart p { font-size: 0.94rem; line-height: 1.68; }

/* ─── FOOTER ─────────────────────────────────────────────────── */
.bee-footer {
    background: #080202;
    color: rgba(255,248,238,0.58);
    padding: 5rem 4rem 2.5rem;
}
.footer-logo { font-family: 'Cormorant Garamond', serif; font-size: 1.6rem; font-weight: 600; color: #F0C060; margin-bottom: 0.8rem; }
.footer-tagline { font-size: 0.84rem; line-height: 1.7; max-width: 240px; margin-bottom: 1.8rem; }
.footer-head { font-size: 0.68rem; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: #C9922A; margin-bottom: 1.2rem; }
.footer-links { list-style: none; padding: 0; margin: 0; }
.footer-links li { margin-bottom: 0.65rem; }
.footer-links a { color: rgba(255,248,238,0.5); text-decoration: none; font-size: 0.84rem; transition: color 0.2s; }
.footer-links a:hover { color: #F0C060; }
.footer-social { display: flex; gap: 0.75rem; margin-top: 0.3rem; }
.social-btn {
    width: 38px; height: 38px; border-radius: 50%;
    background: rgba(139,26,44,0.15);
    border: 1px solid rgba(139,26,44,0.3);
    display: flex; align-items: center; justify-content: center;
    color: #C9922A; text-decoration: none; font-size: 0.95rem;
    transition: all 0.22s;
}
.social-btn:hover { background: #8B1A2C; color: white; border-color: #8B1A2C; }
.footer-bottom {
    border-top: 1px solid rgba(255,248,238,0.07);
    margin-top: 4rem; padding-top: 1.8rem;
    font-size: 0.76rem; color: rgba(255,248,238,0.28); text-align: center;
}

/* ─── FORMS ──────────────────────────────────────────────────── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    border: 1.5px solid #E8D0C0 !important;
    border-radius: 12px !important;
    background: #FEFAF6 !important;
    font-family: 'DM Sans', sans-serif !important;
    color: #1A0808 !important;
    font-size: 0.93rem !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #8B1A2C !important;
    box-shadow: 0 0 0 3px rgba(139,26,44,0.1) !important;
}
.stTextInput label, .stTextArea label, .stSelectbox label, .stNumberInput label {
    font-family: 'DM Sans', sans-serif !important;
    color: #1A0808 !important;
    font-weight: 500 !important;
    font-size: 0.88rem !important;
}
.stNumberInput > div > div > input {
    border: 1.5px solid #E8D0C0 !important;
    border-radius: 12px !important;
    background: #FEFAF6 !important;
    font-family: 'DM Sans', sans-serif !important;
    color: #1A0808 !important;
    text-align: center !important;
}

/* ─── FILTER PANEL ───────────────────────────────────────────── */
.filter-panel {
    background: white; border-radius: 18px;
    padding: 1.8rem 1.5rem;
    box-shadow: 0 4px 24px rgba(26,8,8,0.08);
}
.filter-title { font-family: 'Cormorant Garamond', serif; font-size: 1.12rem; font-weight: 600; color: #1A0808; margin-bottom: 1.4rem; }
.stRadio > label { font-family: 'DM Sans', sans-serif !important; color: #1A0808 !important; }

/* ─── MISC ───────────────────────────────────────────────────── */
hr { border-color: #E8D0C0 !important; }
div[data-testid="column"] { padding: 0.6rem !important; }
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
  <a class="bee-logo" href="/" target="_self">🐝 &nbsp;THEE &nbsp;<em>BEE</em> &nbsp;BOUTIQUE</a>
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
      <p class="footer-tagline">Pure handmade natural soaps — paraben-free, aluminum-free, phthalate-free. Made with love for every skin type.</p>
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
    © 2025 Thee Bee Boutique · Pure Handmade Natural Soaps · All rights reserved
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
#  PRODUCT CARD
# ══════════════════════════════════════════════════════════════════

def render_product_card(product: dict):
    badge_html = ""
    if product.get("badge"):
        cls = "badge-gold" if product["badge"] == "Signature" else ""
        badge_html = f'<span class="product-badge {cls}">{product["badge"]}</span>'
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
      <span class="product-rating"><span class="stars">★★★★★</span> {product['rating']} ({product['reviews']})</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
