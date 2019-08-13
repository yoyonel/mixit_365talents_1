"""
####
# b) Nettoyage du dataset
####
"""
from pandas import Series
from tqdm import tqdm

from mixit_365talents.algorithms.cleaning_tools import STOPWORDS_EN, clean, lowercase_text, remove_punctuation, remove_stopwords


def cleaning_dataset(raw_wiki: Series) -> Series:
    df_wiki_clean = raw_wiki.progress_apply(lambda r: clean(r))

    #
    # #### FIRST ITERATION ####
    #
    #
    #
    tqdm.pandas(desc='cleaning tools (remove punctuations, lowercase, remove stopwords)')
    df_wiki_clean = df_wiki_clean.progress_apply(
        lambda r: [
            remove_stopwords(lowercase_text(remove_punctuation(w)), STOPWORDS_EN)
            for w in r
        ]
    )

    return df_wiki_clean
