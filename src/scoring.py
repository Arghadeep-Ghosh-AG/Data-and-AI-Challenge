from sklearn.metrics.pairwise import cosine_similarity

def semantic_score(
    jd_embedding,
    candidate_embeddings
):

    return cosine_similarity(
        [jd_embedding],
        candidate_embeddings
    )[0]
