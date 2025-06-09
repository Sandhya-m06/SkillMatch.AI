import streamlit as st
from skill_extractor import extract_skills
from category_mapper import map_skills_to_category
from PyPDF2 import PdfReader
import webbrowser

st.set_page_config(page_title="Internship Finder", page_icon="🧠", layout="centered")

st.markdown("<h1 style='text-align: center;'>🎯 Internship Finder</h1>", unsafe_allow_html=True)
st.markdown("Upload your resume and discover matching internships!")

uploaded_file = st.file_uploader("📄 Upload PDF/TXT Resume", type=["pdf", "txt"])

if uploaded_file:
    with st.spinner("🔍 Analyzing your resume..."):
        if uploaded_file.type == "application/pdf":
            reader = PdfReader(uploaded_file)
            resume_text = "".join([page.extract_text() or "" for page in reader.pages])
        else:
            resume_text = uploaded_file.read().decode("utf-8")

        skills = extract_skills(resume_text)
        categories = map_skills_to_category(skills)

        if skills:
            st.success(f"✅ Extracted Skills: {', '.join(skills)}")
            st.info(f"🎯 Predicted Categories: {', '.join(categories)}")

            st.markdown("### 🎯 Matching Internships on Internshala")
            links = []
            for cat in categories:
                link = f"https://internshala.com/internships/{cat.lower().replace(' ', '-')}-internship"
                links.append(link)
                st.markdown(f"🔗 [{cat} Internships on Internshala]({link})", unsafe_allow_html=True)

            def open_last_link():
                webbrowser.open(links[-1])  # Opens the last category's link

            st.button("🔎 Open Last Category in Browser", on_click=open_last_link)

        else:
            st.warning("❗ No relevant skills found. Try a more detailed resume.")
