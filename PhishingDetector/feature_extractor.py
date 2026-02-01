import pandas as pd
import re

def extract_features(url):
    # Minimal example, we will expand this later
    features = {
        "length_url": len(url),
        "nb_dots": url.count("."),
        "nb_hyphens": url.count("-"),
        "nb_at": url.count("@"),
        "ip": 1 if re.match(r"\d+\.\d+\.\d+\.\d+", url) else 0
    }

    # Convert to DataFrame with 1 row
    return pd.DataFrame([features])
