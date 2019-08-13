"""
# #### SECOND ITERATION ####
#
# #  N-Grams function to call and generate new column in your DataFrame
"""
import logging

from gensim.models import Phrases
from gensim.models.phrases import Phraser
from pandas import Series
from tqdm import tqdm


logger = logging.getLogger('mixit_365talents.build_ngrams')


def build_ngrams(texts: Series, min_count=5, threshold=2) -> Series:
    """
    This function builds bigram and ngrams.
    Please don't modify, it may explode.
    """
    logger.info("Building Bigrams")
    phrases = Phrases(tqdm(texts), min_count=min_count, threshold=threshold)
    bigrams = Phraser(phrases)  # Phrases -> Phraser: lighter/faster object, but can't be updated
    bigrams = texts.progress_apply(lambda r: bigrams[r])

    logger.info("Building Ngrams")
    phrases_2 = Phrases(tqdm(bigrams), min_count=min_count, threshold=threshold)
    ngrams = Phraser(phrases_2)
    ngrams = texts.progress_apply(lambda r: ngrams[r])

    return ngrams
