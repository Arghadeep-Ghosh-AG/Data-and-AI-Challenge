import pandas as pd
import json

def load_candidates(path):

    candidates = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            candidates.append(json.loads(line))

    return pd.DataFrame(candidates)


def create_text(row):

    return f"""
    Headline: {row.get('headline','')}
    Summary: {row.get('summary','')}
    Skills: {' '.join(row.get('skills',[]))}
    Experience: {row.get('experience','')}
    """
