import streamlit as st
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="SkillMatch.AI", page_icon="🚀", layout="centered")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

animation = load_lottiefile("assets/animation.json")

st_lottie(animation, speed=1, loop=True, quality="high", height=300)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    body {
        background-color: #0F2027;
        font-family: 'Poppins', sans-serif;
    }

    .hero-container {
        text-align: center;
        padding: 50px 20px;
        color: white;
    }

    .hero-title {
        font-size: 3em;
        font-weight: 600;
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: glow 2s ease-in-out infinite alternate;
    }

    .hero-subtext {
        font-size: 1.2em;
        margin-top: 20px;
        color: #bbbbbb;
    }

    .cta {
        margin-top: 30px;
        display: inline-block;
        padding: 12px 25px;
        font-size: 1em;
        background: #0072ff;
        color: white;
        border-radius: 8px;
        text-decoration: none;
        transition: background 0.3s ease;
    }

    .cta:hover {
        background: #005fdd;
        box-shadow: 0px 0px 10px 2px #0072ff;
    }

    @keyframes glow {
        from {
            text-shadow: 0 0 10px #00c6ff, 0 0 20px #0072ff;
        }
        to {
            text-shadow: 0 0 20px #00c6ff, 0 0 40px #0072ff;
        }
    }
    </style>

    <div class="hero-container">
        <div class="hero-title">Welcome to SkillMatch.AI 🚀</div>
        <div class="hero-subtext">Discover internships tailored to your resume.<br>Navigate to <b>Internship Finder</b> from the top menu.</div>
        <a href="#" class="cta">Start Now</a>
    </div>
""", unsafe_allow_html=True)
