import streamlit as st
from skill_extractor import extract_skills
from category_mapper import map_skills_to_category
from PyPDF2 import PdfReader
import streamlit.components.v1 as components

st.set_page_config(page_title="Internship Finder", page_icon="🧠", layout="centered")

# 💫 Inject animated particles background
components.html("""
<canvas id="bg" style="position: fixed; top: 0; left: 0; z-index: -1; width: 100vw; height: 100vh;"></canvas>
<script>
var canvas = document.getElementById("bg");
var ctx = canvas.getContext("2d");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
let particles = [];
for (let i = 0; i < 60; i++) {
  particles.push({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    r: Math.random() * 1.8 + 1,
    dx: (Math.random() - 0.5) * 0.3,
    dy: (Math.random() - 0.5) * 0.3
  });
}
function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  particles.forEach(p => {
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
    ctx.fillStyle = 'rgba(173, 216, 230, 0.2)';
    ctx.fill();
    p.x += p.dx;
    p.y += p.dy;
    if (p.x < 0 || p.x > canvas.width) p.dx *= -1;
    if (p.y < 0 || p.y > canvas.height) p.dy *= -1;
  });
  requestAnimationFrame(draw);
}
draw();
</script>
""", height=0)

# 💅 Stylish Interface
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Manrope', sans-serif;
        background: linear-gradient(135deg, #f5f7fa, #e4ecf5, #fdfbfb);
        background-size: cover;
        color: #1f2937;
    }

    .container {
        text-align: center;
        padding: 3rem 1.5rem;
        max-width: 750px;
        margin: auto;
        border-radius: 20px;
        background-color: rgba(255, 255, 255, 0.92);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
        animation: fadeIn 1s ease-in-out;
    }

    .title {
        font-size: 2.8em;
        font-weight: 800;
        background: linear-gradient(90deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: popIn 0.8s ease-in-out;
    }

    .subtitle {
        font-size: 1.25em;
        color: #4b5563;
        margin-top: 0.5rem;
        margin-bottom: 2rem;
    }

    .internship-link {
        background: #f4f8ff;
        padding: 14px 22px;
        margin: 10px 0;
        border-radius: 12px;
        display: block;
        text-decoration: none;
        color: #3b82f6;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }

    .internship-link:hover {
        background-color: #e0eaff;
        transform: scale(1.03);
    }

    .btn-custom {
        padding: 14px 32px;
        font-size: 1.1em;
        background: linear-gradient(to right, #667eea, #764ba2);
        color: white;
        font-weight: 600;
        border-radius: 14px;
        border: none;
        margin-top: 30px;
        cursor: pointer;
        transition: background 0.3s ease, transform 0.2s ease;
    }

    .btn-custom:hover {
        background: linear-gradient(to right, #5a67d8, #6b46c1);
        box-shadow: 0px 8px 22px rgba(102, 126, 234, 0.3);
        transform: translateY(-2px);
    }

    .status {
        font-size: 1.1rem;
        margin-top: 1rem;
        color: #10b981;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px);}
        to { opacity: 1; transform: translateY(0);}
    }

    @keyframes popIn {
        0% { transform: scale(0.95); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
    </style>

    <div class="container">
        <div class="title">🔍 Internship Finder</div>
        <div class="subtitle">Upload your resume and let AI match you to the best internship categories! 🚀</div>
    </div>
""", unsafe_allow_html=True)

# 📎 Resume Upload
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("🧠 Analyzing your resume..."):
        if uploaded_file.type == "application/pdf":
            reader = PdfReader(uploaded_file)
            resume_text = "".join([page.extract_text() or "" for page in reader.pages])
        else:
            resume_text = uploaded_file.read().decode("utf-8")

        skills = extract_skills(resume_text)
        categories = map_skills_to_category(skills)

        if skills:
            st.markdown(f"<div class='status'> <strong>Skills Detected:</strong> {', '.join(skills)}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='status'> <strong>Matching Categories:</strong> {', '.join(categories)}</div>", unsafe_allow_html=True)

            st.markdown("### 🌐 Suggested Internships on Internshala")
            links = []
            for cat in categories:
                link = f"https://internshala.com/internships/{cat.lower().replace(' ', '-')}-internship"
                links.append(link)
                st.markdown(f"<a href='{link}' class='internship-link' target='_blank'>{cat} Internships 🔗</a>", unsafe_allow_html=True)

            st.markdown(f"<center><a href='{links[-1]}' target='_blank'><button class='btn-custom'>✨ Open Last Category</button></a></center>", unsafe_allow_html=True)
        else:
            st.warning("😕 We couldn’t find any clear skills in your resume. Try uploading a more detailed one.")
