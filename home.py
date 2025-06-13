import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SkillMatch.AI", layout="centered")

# Inject custom animated background
components.html("""
<canvas id="canvas" style="position: fixed; z-index: -1; top: 0; left: 0; width: 100vw; height: 100vh;"></canvas>
<script>
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
var particles = [];

for (let i = 0; i < 90; i++) {
    particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        radius: Math.random() * 2 + 1,
        dx: (Math.random() - 0.5) * 0.7,
        dy: (Math.random() - 0.5) * 0.7
    });
}

function animate() {
    requestAnimationFrame(animate);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => {
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2, false);
        ctx.fillStyle = 'rgba(255, 182, 193, 0.4)';
        ctx.fill();
        p.x += p.dx;
        p.y += p.dy;
        if (p.x < 0 || p.x > canvas.width) p.dx = -p.dx;
        if (p.y < 0 || p.y > canvas.height) p.dy = -p.dy;
    });
}
animate();
</script>
""", height=0)

# CSS and Layout
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        height: 100%;
        margin: 0;
        padding: 0;
        background: linear-gradient(135deg, #dce4f7, #f3dce4, #f5f5f5);
        background-size: cover;
        color: #332f3d;
    }

    .main {
        background: rgba(255, 255, 255, 0.0);
    }

    .glass-box {
        background: rgba(255, 255, 255, 0.22);
        box-shadow: 0 12px 50px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        border-radius: 25px;
        padding: 60px 40px;
        text-align: center;
        margin-top: 80px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        animation: fadeIn 2.5s ease-out;
    }

    .title {
        font-size: 3.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #cbd5f0, #ebc4d2, #eaeaea);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: glow 4s ease-in-out infinite alternate;
    }

    .subtext {
        font-size: 1.35rem;
        margin-top: 25px;
        color: #3d344d;
        line-height: 1.6;
    }

    div[data-testid="stLinkButton"] button {
        background: linear-gradient(135deg, #ff9a9e, #fad0c4);
        color: white;
        font-weight: 600;
        font-size: 18px;
        padding: 0.75em 2.2em;
        border-radius: 14px;
        margin-top: 3em;
        box-shadow: 0 6px 20px rgba(255, 140, 160, 0.4);
        transition: all 0.3s ease;
        border: none;
    }

    div[data-testid="stLinkButton"] button:hover {
        background: linear-gradient(135deg, #ff758c, #ff7eb3);
        box-shadow: 0 12px 30px rgba(255, 100, 120, 0.5);
        transform: scale(1.06);
    }

    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(30px);}
        to {opacity: 1; transform: translateY(0);}
    }

    @keyframes glow {
        from { text-shadow: 0 0 6px rgba(255,255,255,0.3); }
        to { text-shadow: 0 0 18px rgba(255,255,255,0.8); }
    }
    </style>

    <div class="glass-box">
        <div style="font-size: 2.5rem;"> 🎯</div>
        <div class="title">Welcome to SkillMatch.AI</div>
        <div class="subtext">
            Your personalized internship assistant<br>
            Let AI bring your dream internship closer with precision and charm 
        </div>
    </div>
""", unsafe_allow_html=True)

# Pretty centered button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.page_link("pages/internships.py", label="🔎 Start Internship Finder", icon="🌟")
