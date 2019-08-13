"""
"""
import pandas as pd


def compare_models(tokens, wvs, titles) -> pd.DataFrame:
    """
    Pretty print for most_similar for multiple w2v
    """
    results = {
        {title: [token_score[0] for token_score in wv.most_similar(tokens)]}
        for wv, title in zip(wvs, titles)
    }
    return pd.DataFrame(data=results)
