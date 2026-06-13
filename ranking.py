def rank_candidates(df):

    df = df.sort_values(
        by="final_score",
        ascending=False
    )

    df["rank"] = range(
        1,
        len(df)+1
    )

    return df
