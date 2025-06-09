import streamlit as st
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="SkillMatch.AI", page_icon="🚀", layout="centered")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

animation = load_lottiefile("assets/animation.json")

st_lottie(animation, speed=1, loop=True, quality="high", height=300)

st.markdown("<h1 style='text-align: center;'>Welcome to SkillMatch.AI 🚀</h1>", unsafe_allow_html=True)
st.markdown("### 👋 Discover internships tailored to your resume. Start by navigating to **Internship Finder** from the sidebar.")
