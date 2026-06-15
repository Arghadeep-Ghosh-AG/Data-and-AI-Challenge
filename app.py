import streamlit as st

st.title("AI Candidate Ranking System")

jd = st.text_area("Paste Job Description")

if st.button("Rank Candidates"):
    st.success("Ranking started!")

    # Later call your ranking pipeline here
    st.write("Top candidates will appear here.")
