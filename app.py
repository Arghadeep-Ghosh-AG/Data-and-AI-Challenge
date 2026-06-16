import streamlit as st

st.title("AI Candidate Ranking System")

jd = st.text_area("Paste Job Description")

if st.button("Rank Candidates"):
    st.success("Ranking started!")

    # Later call your ranking pipeline here
    st.write("Top candidates will appear here.")
    
from src.main import rank_candidates_from_jd

st.title("AI Candidate Ranking System")

jd = st.text_area(
    "Paste Job Description"
)

if st.button("Rank Candidates"):

    if jd.strip():

        results = rank_candidates_from_jd(
            jd
        )

        st.subheader(
            "Top Candidates"
        )

        st.dataframe(results)

        st.success(
            "Ranking completed successfully!"
        )

    else:

        st.warning(
            "Please enter a Job Description."
        )

