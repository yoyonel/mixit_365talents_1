"""
####
# c) Entraînement du Word2Vec
# Word2Vec doc : https://radimrehurek.com/gensim/models/word2vec.html
"""
from gensim.models.word2vec import Word2Vec
from pandas import Series


def training_model(df_column: Series, min_count=5, window=5, size=100, sg=0) -> Word2Vec:
    """

    :param df_column:
    :param min_count:
    :param window:
    :param size:
    :param sg:
    :return:
    """
    w2v = Word2Vec(
        df_column,
        min_count=min_count,
        window=window,
        size=size,
        sg=sg,
    )
    return w2v
