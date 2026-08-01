import random
import streamlit as st

st.set_page_config(
    page_title="Diptyque — Adiba & Faheed",
    page_icon="🕯️",
    layout="centered"
)

# Diptyque Vintage Oval SVG & Aesthetic CSS
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,400&display=swap');

    /* Creamy off-white Background */
    .stApp {
        background-color: #FBF9F5;
        color: #1A1A1A;
        font-family: 'Cormorant Garamond', serif;
    }

    h1, h2, h3, p, div, span, button {
        font-family: 'Cormorant Garamond', serif !important;
    }

    /* Diptyque Signature Oval Frame Container */
    .diptyque-oval-card {
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 420'%3E%3Cpath d='M150,10 C220,10 280,70 280,210 C280,350 220,410 150,410 C80,410 20,350 20,210 C20,70 80,10 150,10 Z' fill='none' stroke='%231A1A1A' stroke-width='2'/%3E%3Cpath d='M150,18 C213,18 272,75 272,210 C272,345 213,402 150,402 C87,402 28,345 28,210 C28,75 87,18 150,18 Z' fill='none' stroke='%231A1A1A' stroke-width='0.8' stroke-dasharray='3 3'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-position: center top;
        background-size: contain;
        padding: 50px 40px;
        text-align: center;
        max-width: 420px;
        margin: 0 auto;
    }

    .brand-header {
        font-size: 0.75rem;
        letter-spacing: 0.35em;
        text-transform: uppercase;
        color: #555555;
        margin-top: 15px;
    }

    .brand-title {
        font-size: 2rem;
        letter-spacing: 0.25em;
        text-transform: uppercase;
        font-weight: 400;
        margin: 10px 0;
        border-bottom: 1px solid #1A1A1A;
        display: inline-block;
        padding-bottom: 5px;
    }

    .brand-subtitle {
        font-size: 0.8rem;
        letter-spacing: 0.2em;
        font-style: italic;
        color: #444444;
        margin-bottom: 25px;
    }

    /* Minimalist Transparent Buttons */
    .stButton>button {
        background: transparent !important;
        color: #1A1A1A !important;
        border: 1px solid #1A1A1A !important;
        border-radius: 0px !important;
        letter-spacing: 0.2em !important;
        text-transform: uppercase !important;
        font-size: 0.85rem !important;
        transition: all 0.3s ease !important;
    }

    .stButton>button:hover {
        background-color: #1A1A1A !important;
        color: #FBF9F5 !important;
    }

    /* Game Output Styles */
    .choice-text {
        font-size: 1.1rem;
        letter-spacing: 0.1em;
        margin: 15px 0 5px 0;
    }

    .result-text {
        font-size: 1.5rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        font-weight: 600;
        margin: 15px 0;
    }

    .score-banner {
        text-align: center;
        margin-top: 30px;
        font-size: 0.85rem;
        letter-spacing: 0.25em;
        text-transform: uppercase;
        border-top: 1px solid #E0E0E0;
        padding-top: 15px;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# Game Rules & Setup
EMOJIS = {'r': '🪨', 'p': '📜', 's': '✂️'}
NAMES = {'r': 'ROCK', 'p': 'PAPER', 's': 'SCISSORS'}
WINNING_RULES = {'r': 's', 'p': 'r', 's': 'p'}

if 'adiba_score' not in st.session_state:
    st.session_state.adiba_score = 0
if 'faheed_score' not in st.session_state:
    st.session_state.faheed_score = 0
if 'last_game' not in st.session_state:
    st.session_state.last_game = None

def play(adiba_choice):
    faheed_choice = random.choice(list(EMOJIS.keys()))
    
    if adiba_choice == faheed_choice:
        result = "EQUAL MATCH"
    elif WINNING_RULES[adiba_choice] == faheed_choice:
        result = "ADIBA VICTORIOUS"
        st.session_state.adiba_score += 1
    else:
        result = "FAHEED VICTORIOUS"
        st.session_state.faheed_score += 1

    st.session_state.last_game = {
        'adiba': adiba_choice,
        'faheed': faheed_choice,
        'result': result
    }

def reset_game():
    st.session_state.last_game = None

def reset_all():
    st.session_state.adiba_score = 0
    st.session_state.faheed_score = 0
    st.session_state.last_game = None

# --- DIPTYQUE EMBLEM CONTAINER ---
st.markdown(
    """
    <div class="diptyque-oval-card">
        <div class="brand-header">DHAKA, BANGLADESH</div>
        <div class="brand-title">ADIBA × FAHEED</div>
        <div class="brand-subtitle">EAU DE GAME</div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- PLAY CONTROLS ---
if st.session_state.last_game is None:
    st.markdown("<p style='text-align:center; letter-spacing:0.15em; font-size:0.9rem;'>MAKE YOUR CHOICE</p>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("ROCK", use_container_width=True):
            play('r')
            st.rerun()
    with c2:
        if st.button("PAPER", use_container_width=True):
            play('p')
            st.rerun()
    with c3:
        if st.button("SCISSORS", use_container_width=True):
            play('s')
            st.rerun()
else:
    # --- GAME RESULT & PLAY AGAIN SECTION ---
    game = st.session_state.last_game
    
    st.markdown(
        f"""
        <div style="text-align:center;">
            <div class="choice-text">
                ADIBA: <b>{NAMES[game['adiba']]}</b> &nbsp;—&nbsp; FAHEED: <b>{NAMES[game['faheed']]}</b>
            </div>
            <div class="result-text">{game['result']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.write("")
    col_again, col_reset = st.columns(2)
    with col_again:
        if st.button("PLAY AGAIN ↺", use_container_width=True):
            reset_game()
            st.rerun()
    with col_reset:
        if st.button("RESET SCORE", use_container_width=True):
            reset_all()
            st.rerun()

# --- SCOREBOARD FOOTER ---
st.markdown(
    f"""
    <div class="score-banner">
        SCORE &nbsp;&bull;&nbsp; ADIBA: <b>{st.session_state.adiba_score}</b> &nbsp;|&nbsp; FAHEED: <b>{st.session_state.faheed_score}</b>
    </div>
    """,
    unsafe_allow_html=True
)
