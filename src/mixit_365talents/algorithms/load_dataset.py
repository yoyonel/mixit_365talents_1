"""
3. Chargement du dataset
"""
from pathlib import Path

import pandas as pd
from pandas import DataFrame


def load_dataset(path_to_dataset: Path) -> DataFrame:
    """
    Pandas DataFrame doc : https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

    :param path_to_dataset:
    :return:
    """
    df_wiki = pd.read_csv(path_to_dataset, header=None, sep="noWayYouFindThisSentence268346315618", engine='python')
    return df_wiki
