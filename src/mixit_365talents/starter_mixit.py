import logging
from pathlib import Path

import pkg_resources
from tqdm import tqdm

from mixit_365talents.algorithms.cleaning_dataset import cleaning_dataset
from mixit_365talents.algorithms.evaluate_model import evaluate_model
from mixit_365talents.algorithms.load_dataset import load_dataset
from mixit_365talents.algorithms.training_model import training_model
from mixit_365talents.tools.fct_logger import init_logger

logger = logging.getLogger('mixit_365talents.starter_mixit')


def process():
    path_to_data = Path(pkg_resources.resource_filename(__name__, 'data/'))
    assert path_to_data.exists()
    assert path_to_data.is_dir()

    path_to_dataset = path_to_data / "en_wiki_SMALL.txt"
    assert path_to_dataset.exists()
    #
    df_wiki = load_dataset(path_to_dataset)

    #
    wiki_clean = cleaning_dataset(df_wiki[0])

    #
    # # You may change min_count hyperparameter
    #
    # #### THIRD ITERATION ####
    #
    # You may change window hyperparameter
    w2v_window = 5
    # You may change size hyperparameter
    w2v_size = 100
    # You may change sg hyperparameter
    w2v_sg = 0

    w2v = training_model(wiki_clean, window=w2v_window, size=w2v_size, sg=w2v_sg)

    evaluation_path_file = path_to_data / "questions-words.txt"
    assert evaluation_path_file.exists()
    #
    evaluate_model(w2v, str(evaluation_path_file))


def main():
    tqdm.pandas()

    # set logger(s) levels
    init_logger('debug')
    logging.getLogger('gensim.models').setLevel(logging.INFO)
    logging.getLogger('smart_open.smart_open_lib').setLevel(logging.ERROR)

    process()


if __name__ == '__main__':
    main()
