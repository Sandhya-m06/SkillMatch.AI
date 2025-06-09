import streamlit as st
from streamlit_lottie import st_lottie
import json

# -------------------- Page Config --------------------
st.set_page_config(page_title="SkillMatch.AI", page_icon="🚀", layout="centered")

# -------------------- Load Lottie Animation --------------------
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

animation = load_lottiefile("assets/animation.json")

# -------------------- Sidebar Navigation --------------------
st.sidebar.header("🔎 Navigate")
st.sidebar.markdown("Choose a page to get started:")

# Debug: Display session state to verify page availability
st.sidebar.write("Available session state:", st.session_state)

# Navigation Button
if st.sidebar.button("Go to Internship Finder"):
    st.switch_page("Internships")  # Must match file name in /pages/ exactly

# -------------------- Main Page Content --------------------
st_lottie(animation, speed=1, loop=True, quality="high", height=300)

st.markdown("<h1 style='text-align: center;'>Welcome to SkillMatch.AI 🚀</h1>", unsafe_allow_html=True)
st.markdown("### 👋 Discover internships tailored to your resume.")
st.markdown("Use the **sidebar** on the left to navigate to the Internship Finder and get started!")
