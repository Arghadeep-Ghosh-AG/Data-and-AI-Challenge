import streamlit as st
from src.main import rank_candidates_from_jd

# ---------------------------
# Page Configuration
# ---------------------------

st.set_page_config(
    page_title="AI Candidate Ranking System",
    page_icon="🎯",
    layout="wide"
)

# ---------------------------
# Header
# ---------------------------

st.title("🎯 AI Candidate Ranking System")

st.markdown("""
### Intelligent AI-Powered Candidate Ranking

This system helps recruiters identify the best-fit candidates using:

✅ Semantic Search  
✅ BGE Embeddings  
✅ Cosine Similarity Scoring  
✅ AI-Powered Candidate Ranking  
✅ Recruiter-Friendly Explanations  

Paste a Job Description below and receive an instant ranked shortlist.
""")

st.markdown("---")

# ---------------------------
# Job Description Input
# ---------------------------

jd = st.text_area(
    "📄 Paste Job Description",
    height=250,
    placeholder="""
Example:

Senior Data Scientist

Requirements:
- Python
- Machine Learning
- NLP
- Deep Learning
- SQL

Responsibilities:
- Build ML models
- Analyze data
- Deploy AI solutions
""",
    key="job_description_input"
)

# ---------------------------
# Rank Button
# ---------------------------

if st.button(
    "🚀 Rank Candidates",
    key="rank_button"
):

    if jd.strip():

        with st.spinner(
            "Analyzing candidates..."
        ):

            results = rank_candidates_from_jd(jd)

        st.success(
            "Ranking completed successfully!"
        )

        st.markdown("---")

        # ---------------------------
        # Metrics
        # ---------------------------

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Candidates Ranked",
                len(results)
            )

        with col2:
            st.metric(
                "Top Match Score",
                round(
                    results["final_score"].max(),
                    3
                )
            )

        with col3:
            st.metric(
                "Embedding Model",
                "BGE"
            )

        st.markdown("---")

        # ---------------------------
        # Results Table
        # ---------------------------

        st.subheader(
            "🏆 Top Ranked Candidates"
        )

        st.dataframe(
            results,
            use_container_width=True
        )

        st.markdown("---")

        # ---------------------------
        # Candidate Insights
        # ---------------------------

        st.subheader(
            "📋 Candidate Insights"
        )

        for _, row in results.head(5).iterrows():

            with st.container():

                st.markdown(
                    f"""
### 🏅 Rank #{row['rank']}

**Candidate ID:** {row['candidate_id']}

**Match Score:** {row['final_score']:.3f}

**Reason:** {row['reason']}
"""
                )

                st.divider()

        # ---------------------------
        # Download CSV
        # ---------------------------

        csv = results.to_csv(index=False)

        st.download_button(
            label="📥 Download Results CSV",
            data=csv,
            file_name="submission.csv",
            mime="text/csv"
        )

    else:

        st.warning(
            "Please enter a Job Description."
        )

# ---------------------------
# Footer
# ---------------------------

st.markdown("---")

st.subheader(
    "⚙️ System Architecture"
)

st.markdown("""
### Workflow

Job Description  
⬇️  
Text Processing  
⬇️  
BGE Embeddings  
⬇️  
Cosine Similarity  
⬇️  
Candidate Ranking  
⬇️  
Reason Generation  
⬇️  
Top Candidate Recommendations
""")

st.markdown("---")

st.caption(
    "Built for The Data & AI Challenge 🚀"
)
