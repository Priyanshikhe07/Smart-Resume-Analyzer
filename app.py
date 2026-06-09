import streamlit as st
from parser import extract_text
from ats import calculate_score
from skills import extract_skills

st.title("📄 Smart Resume Analyzer")

st.write("Upload your resume and get ATS insights.")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)
job_description = st.text_area(
    "Paste Job Description Here"
)

if uploaded_file and job_description:

    st.success("✅ Resume Uploaded Successfully!")

    resume_text = extract_text(uploaded_file)
    resume_skills = extract_skills(resume_text)

    st.subheader("Detected Skills")

    for skill in resume_skills:
        st.write("✅", skill)

    ats_score = calculate_score(
        resume_text,
        job_description
    )


    jd_skills = extract_skills(job_description)

    skill_score = (
        len(set(resume_skills) & set(jd_skills))
        / len(jd_skills)
    ) * 100

# Final ATS Score

    final_score = (skill_score * 0.7) + (ats_score * 0.3)
    jd_skills = extract_skills(job_description)
    st.write("JD Skills:", jd_skills)
    st.write("Resume Skills:", resume_skills)

    missing_skills = []

    for skill in jd_skills:
        if skill not in resume_skills:
            missing_skills.append(skill)

    st.subheader("Missing Skills")

    for skill in missing_skills:
        st.write("❌", skill)
    st.subheader("ATS Score")

    st.progress(int(final_score))

    st.success(f"{final_score:.2f}% Match")
    
    st.subheader("Extracted Resume Text")
    st.write(resume_text)