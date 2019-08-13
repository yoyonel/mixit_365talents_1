"""
####
# d) Evaluation du Word2Vec
####
"""
import logging

logger = logging.getLogger('mixit_365talents.evaluate_model')


def evaluate_model(w2v, evaluation_path_file="questions-words.txt"):
    """
    Given a w2v, print scores for analogies evaluation.
    """
    score, sections = w2v.wv.evaluate_word_analogies(evaluation_path_file, dummy4unknown=False)
    logger.info("Within model vocab : %.2f%%", 100.0 * score)
    score, sections = w2v.wv.evaluate_word_analogies(evaluation_path_file, dummy4unknown=True)
    logger.info("Whole eval dataset : %.2f%%", 100.0 * score)
