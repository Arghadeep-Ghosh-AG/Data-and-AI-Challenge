from preprocess import *
from embeddings import *
from scoring import *
from ranking import *

df = load_candidates(
    "data/candidates.jsonl"
)

df["candidate_text"] = df.apply(
    create_text,
    axis=1
)

with open(
    "data/job_description.txt",
    "r",
    encoding="utf-8"
) as f:
    jd_text = f.read()

jd_embedding = generate_embeddings(
    [jd_text]
)[0]

candidate_embeddings = generate_embeddings(
    df["candidate_text"].tolist()
)

df["semantic_score"] = semantic_score(
    jd_embedding,
    candidate_embeddings
)

df["final_score"] = df["semantic_score"]

ranked = rank_candidates(df)

ranked[
    ["candidate_id","rank"]
].to_csv(
    "output/submission.csv",
    index=False
)

print("Submission generated.")
