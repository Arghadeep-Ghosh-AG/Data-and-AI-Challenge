import streamlit as st
from src.main import rank_candidates_from_jd

st.set_page_config(
    page_title="AI Candidate Ranking System",
    page_icon="🎯",
    layout="wide"
)

st.title("AI Candidate Ranking System")

st.write(
    "Paste a Job Description below and rank the best matching candidates."
)

jd = st.text_area(
    "Paste Job Description",
    height=200,
    key="job_description_input"
)

if st.button(
    "Rank Candidates",
    key="rank_button"
):

    if jd.strip():

        with st.spinner("Ranking candidates..."):

            results = rank_candidates_from_jd(jd)

        st.subheader("Top Candidates")

        st.dataframe(
            results,
            use_container_width=True
        )

        st.success(
            "Ranking completed successfully!"
        )

    else:

        st.warning(
            "Please enter a Job Description."
        )
