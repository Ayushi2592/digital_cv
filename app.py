from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic_path = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Portfolio | Ayushi Singh"
PAGE_ICON = ":wave:"
NAME = "Ayushi Singh"
DESCRIPTION = """
Aspiring Software Engineer with a passion for developing innovative programs that expedite the efficiency and effectiveness of organizational success. I am enthusiastic about learning new technologies, with a particular interest in Flutter app development and problem-solving.
"""
EMAIL = "ayushisinghfl20@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/ayushisingh2592/",
    "GitHub": "https://github.com/Ayushi2592",
}
PROJECTS = {
    "🏆 ClothCrafted": " This platform primarily concentrates on the effective management of clothing waste by collaborating with various NGOs and individuals interested in participating in coordination efforts.",
    "🏆 SkillMatch": "This platform facilitates college students and individuals with various technical skills in finding the ideal collaborator for their projects",
}

# --- SET PAGE CONFIG ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic_path)

# --- HERO SECTION ---
st.container()
col1, col2 = st.columns([1, 2], gap="small")
with col1:
    st.image(profile_pic, width=230, use_column_width='auto')

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
        key="download_button"
    )
    st.write(f"📫 {EMAIL}")

# --- NAVIGATION LINKS ---
st.markdown(
    """
    <nav>
        <a href="#about">About</a>
        <a href="#projects">Projects</a>
        <a href="{}" target="_blank">LinkedIn</a>
        <a href="{}" target="_blank">GitHub</a>
    </nav>
    """.format(SOCIAL_MEDIA["LinkedIn"], SOCIAL_MEDIA["GitHub"]),
    unsafe_allow_html=True,
)

# --- ABOUT SECTION ---
st.write('\n')
st.write("---")
st.markdown("<h2 id='about'>About</h2>", unsafe_allow_html=True)
st.write(
    """
    I am an aspiring software engineer with a strong foundation in computer science and a passion for developing innovative solutions.
    I have experience in various programming languages and technologies, and I am always eager to learn and take on new challenges.
    """
)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Strong hands-on experience in C++, Dart, and Python
- ✔️ Proficient in app development (Flutter, Dart, and FireBase)
- ✔️ Worked with different databases and on cloud
- ✔️ Excellent teamwork and communication skills
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming: Python, C++, Dart, FireBase, NodeJS, MySQL 
- 🌐 App Development: Flutter, Dart, FireBase
- 🗄️ Databases: MySQL, PostgreSQL, MongoDB
"""
)

# --- EDUCATION ---
st.write('\n')
st.subheader("Education")
st.write("---")
st.write("🎓 *Computer Science and Engineering*")
st.write("Vellore Institute Of Technology, 2025")
st.write("Relevant Coursework: Algorithms, Data Structures, Computer Network, Database Management Systems, Operating System.")

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1 ---
st.write("🚧", "*App Developer | CodeAlpha*")
st.write(
    """
- ► Enhanced app performance by optimizing backend processes, achieving a 99.9% uptime and boosting user engagement by 25%; collaborated with design team to implement intuitive interfaces, significantly improving user satisfaction.
"""
)

# --- JOB 2 ---
st.write('\n')
st.write("🚧", "*Python Developer | InternArmy*")
st.write(
    """
- ► Drove the development of 5+ innovative projects, analyzing datasets with over 100,000 entries to extract actionable insights, improving project efficiency by 20% and enhancing user satisfaction by 25% through intuitive interfaces.
"""
)

# --- PROJECTS & ACCOMPLISHMENTS ---
st.write('\n')
st.write("---")
st.markdown("<h2 id='projects'>Projects & Accomplishments</h2>", unsafe_allow_html=True)
for project, description in PROJECTS.items():
    st.write(f"**{project}**")
    st.write(description)

# --- FOOTER ---
st.write('\n')
st.write("---")
st.write("Thank you for visiting my portfolio! Feel free to [contact me](mailto:{}) for any inquiries.".format(EMAIL))
