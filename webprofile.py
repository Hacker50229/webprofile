import streamlit as st

# Page configuration
st.set_page_config(page_title="Asawijak Sirivilat", page_icon="╰(*°▽°*)╯")

# Title
st.title("🔱 Whoami")

# Introduction
st.subheader("I'm Asawijak Sirivilat (Game)")
st.write("""
- 2021 - Present 🧑 Student in Debsirin school Mini english program (MEP)(https://www.debsirin.ac.th/index.php)
- 2024 - Present 🧑 Student in Debsirin school gifted (GSMP)(https://www.debsirin.ac.th/index.php)
- 2024 - Co-ops and internships LLM developer @ Bank for Agriculture and Agricultural Co-operatives ([BAAC](https://www.baac.or.th/en/))
""")

# Current Activities
st.subheader("🧑‍💻 What I'm Doing Now")
st.write("""
- 💻 Studying Computer
- 👨‍💻 For fun Rov game
- 🚩 ...
- 💬 Chat Gpt lover
- 🤖 Learning anything with Machine Learning
""")

# Tech Stack & Skills
st.subheader("📚 Tech Stack & Skills")

# Programming Languages
with st.expander("👨‍💻 Programming Languages"):
    st.image("https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54", use_column_width=True)
    st.image("https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/c%23-%23239120.svg?style=for-the-badge&logo=csharp&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E", use_column_width=True)
    st.image("https://img.shields.io/badge/php-%23777BB4.svg?style=for-the-badge&logo=php&logoColor=white", use_column_width=True)

# Frontend Development
with st.expander("🪟 Frontend Development"):
    st.image("https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white", use_column_width=True)

# Backend Development
with st.expander("☠️ Backend Development"):
    st.image("https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white", use_column_width=True)

# AI & ML
with st.expander("🤖 AI & ML"):
    st.image("https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black", use_column_width=True)
    st.image("https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white", use_column_width=True)
    st.image("https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white", use_column_width=True)

# Dev Tools
with st.expander("🐥 Dev Tools"):
    st.image("https://skillicons.dev/icons?i=git,github,gitlab,linux,ubuntu,neovim,raspberrypi,arduino", use_column_width=True)

# My Skills
st.subheader("🐥 My Skills")
st.image("https://skillicons.dev/icons?i=python,linux,cpp,js,java,php,anaconda", use_column_width=True)

# Future Plans
st.subheader("🔮 What in Future")
st.write("""
- [ ] Study Chulalongkorn University (2027)
- [ ] Working in ~~software development~~ AI&ML roles
""")

# Contact Information
st.subheader("📩 Connect with Me")
st.write("""
- 📩 hacker28459@gmail.com
- 🔗 ...
- 📖 ...
""")

# GitHub Stats
st.subheader("GitHub Stats")
st.image("https://github-readme-stats.vercel.app/api?username=JeerasakAnanta", use_column_width=True)

# Footer
st.write("Thank you krub for reading :) 💯💪")
