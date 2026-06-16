print("USING PREPROCESS:", __file__)
import json
import pandas as pd

def load_candidates(path):

    print("LOADING FILE:", path)

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    print("FIRST 200 CHARS:")
    print(content[:200])

    candidates = json.loads(content)

    return pd.DataFrame(candidates)


def create_text(row):

    profile = row.get("profile", {})

    return " ".join([
        str(profile.get("headline", "")),
        str(profile.get("summary", "")),
        str(profile.get("current_title", "")),
        str(profile.get("current_industry", ""))
    ])