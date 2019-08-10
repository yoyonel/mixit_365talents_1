import logging
import string
from pathlib import Path

import pandas as pd
import pkg_resources
from gensim.models.word2vec import Word2Vec
from pandas import DataFrame
from tqdm import tqdm

from mixit_365talents.tools.fct_logger import init_logger

logger = logging.getLogger('mixit_365talents.starter_mixit')

# Stopwords data
stopwords_en = {"ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out",
                "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such",
                "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him",
                "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don",
                "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while",
                "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them",
                "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because",
                "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has", "just",
                "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if",
                "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than"}


def load_dataset(path_to_dataset: Path) -> DataFrame:
    """
    3. Chargement du dataset
    Pandas DataFrame doc : https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

    :param path_to_dataset:
    :return:
    """
    df_wiki = pd.read_csv(path_to_dataset, header=None, sep="noWayYouFindThisSentence268346315618", engine='python')
    return df_wiki


####
# AMELIORATION CONTINUE
####
####
# a) Définition de ma fonction de nettoyage
####
def clean(text):
    """
    You may call this function to clean your dataset

    :param text: a wikipedia article (string)
    :return: your clean wikipedia article, separated by tokens (list of string)
    """

    return text.split()


####
# d) Evaluation du Word2Vec
####
def evaluate_model(w2v, evaluation_path_file="questions-words.txt"):
    """
    Given a w2v, print scores for analogies evaluation.
    """
    score, sections = w2v.wv.evaluate_word_analogies(evaluation_path_file, dummy4unknown=False)
    logger.info("Within model vocab : %.2f%%", 100.0 * score)
    score, sections = w2v.wv.evaluate_word_analogies(evaluation_path_file, dummy4unknown=True)
    logger.info("Whole eval dataset : %.2f%%", 100.0 * score)

    ########################
    #### CLEANING TOOLS ####
    ########################


def remove_punctuation(text, punctuation=string.punctuation):
    """
    From string.punctuation, each character is replaced by None (the character is removed)
    """
    text = text.translate(str.maketrans('', '', punctuation))
    return text


def lowercase_text(text):
    """
    Each character is replaced by his lowercase version
    """
    text = text.lower()
    return text


def remove_stopwords(text, stopwords):
    """
    Remove every occurrence of the given stopwords set
    """
    text = " ".join([w for w in text.split() if w not in stopwords])
    return text


def compare_models(tokens, wvs, titles):
    """
    Pretty print for most_similar for multiple w2v
    """
    results = {}
    for wv, title in zip(wvs, titles):
        results.update({title: [i[0] for i in wv.most_similar(tokens)]})
    return pd.DataFrame(data=results)


def process():
    path_to_data = Path(pkg_resources.resource_filename(__name__, 'data/'))
    assert path_to_data.exists()
    assert path_to_data.is_dir()

    path_to_dataset = path_to_data / "en_wiki_SMALL.txt"
    assert path_to_dataset.exists()
    #
    df_wiki = load_dataset(path_to_dataset)

    ####
    # b) Nettoyage du dataset
    ####
    df_wiki["clean"] = df_wiki[0].progress_apply(lambda r: clean(r))

    ####
    # c) Entraînement du Word2Vec
    # Word2Vec doc : https://radimrehurek.com/gensim/models/word2vec.html
    # w2v = Word2Vec(
    #     df_wiki.clean,
    #     # min_count=None,
    #     # window=None,
    #     # size=None,
    #     # sg=None,
    # )

    evaluation_path_file = path_to_data / "questions-words.txt"
    assert evaluation_path_file.exists()
    #
    # evaluate_model(w2v, str(evaluation_path_file))

    #
    # #### FIRST ITERATION ####
    #
    #
    #
    tqdm.pandas(desc='cleaning tools (remove punctuations, lowercase, remove stopwords)')
    df_wiki["clean"] = df_wiki["clean"].progress_apply(
        lambda r: [
            remove_stopwords(lowercase_text(remove_punctuation(w)), stopwords_en)
            for w in r
        ]
    )

    w2v = Word2Vec(
        df_wiki.clean,
        # min_count=None,
        # window=None,
        # size=None,
        # sg=None,
    )
    evaluate_model(w2v, str(evaluation_path_file))

    #
    # #### SECOND ITERATION ####
    #
    # #  N-Grams function to call and generate new column in your DataFrame
    #
    # def build_ngrams(df, min_count=5, threshold=2):
    #     """
    #     This function builds bigram and ngrams.
    #     Please don't modify, it may explode.
    #     """
    #
    #     print("Building Bigrams")
    #     phrases = Phrases(tqdm(df.clean), min_count=min_count, threshold=threshold)
    #     bigrams = Phraser(phrases)  # Phrases -> Phraser: lighter/faster object, but can't be updated
    #     df['bigrams'] = df.clean.progress_apply(lambda r: bigrams[r])
    #
    #     print("Building Ngrams")
    #     phrases_2 = Phrases(tqdm(df.bigrams), min_count=min_count, threshold=threshold)
    #     ngrams = Phraser(phrases_2)
    #     df['ngrams'] = df.clean.progress_apply(lambda r: ngrams[r])
    #
    # # You may change min_count hyperparameter
    #
    # #### THIRD ITERATION ####
    #
    # # You may change window hyperparameter
    # # You may change size hyperparameter
    # # You may change sg hyperparameter


def main():
    tqdm.pandas()

    # set logger(s) levels
    init_logger('debug')
    logging.getLogger('gensim.models').setLevel(logging.INFO)
    logging.getLogger('smart_open.smart_open_lib').setLevel(logging.ERROR)

    process()


if __name__ == '__main__':
    main()
