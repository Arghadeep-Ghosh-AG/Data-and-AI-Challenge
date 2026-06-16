from src.preprocess import *
from src.embeddings import *
from src.scoring import *
from src.ranking import *

import os


def generate_reason(row):

    reasons = []

    if row["semantic_score"] > 0.75:
        reasons.append(
            "Strong semantic match with job description"
        )

    if row["semantic_score"] > 0.70:
        reasons.append(
            "Relevant skills and experience detected"
        )

    if not reasons:
        reasons.append(
            "Moderate fit based on profile information"
        )

    return "; ".join(reasons)


def rank_candidates_from_jd(jd_text):

    # Load candidate dataset
    df = load_candidates(
        "data/sample_candidates.json"
    )

    # Create candidate text representation
    df["candidate_text"] = df.apply(
        create_text,
        axis=1
    )

    # Generate JD embedding
    jd_embedding = generate_embeddings(
        [jd_text]
    )[0]

    # Generate candidate embeddings
    candidate_embeddings = generate_embeddings(
        df["candidate_text"].tolist()
    )

    # Semantic similarity
    df["semantic_score"] = semantic_score(
        jd_embedding,
        candidate_embeddings
    )

    # Final score
    df["final_score"] = df["semantic_score"]

    # Generate recruiter reasoning
    df["reason"] = df.apply(
        generate_reason,
        axis=1
    )

    # Rank candidates
    ranked = rank_candidates(df)

    # Create output directory if missing
    os.makedirs(
        "output",
        exist_ok=True
    )

    # Save top 100 ranked candidates
    ranked[
        [
            "candidate_id",
            "final_score",
            "rank",
            "reason"
        ]
    ].head(100).to_csv(
        "output/submission.csv",
        index=False
    )

    # Return top 100 for Streamlit display
    return ranked[
        [
            "candidate_id",
            "final_score",
            "rank",
            "reason"
        ]
    ].head(100)
