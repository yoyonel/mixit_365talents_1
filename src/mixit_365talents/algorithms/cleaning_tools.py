"""
####
# AMELIORATION CONTINUE
####
####
# a) Définition de ma fonction de nettoyage
####
"""
import string

# Stopwords data
STOPWORDS_EN = {
    "ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out",
    "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such",
    "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him",
    "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don",
    "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while",
    "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them",
    "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because",
    "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has", "just",
    "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if",
    "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than"
}


def clean(text):
    """
    You may call this function to clean your dataset

    :param text: a wikipedia article (string)
    :return: your clean wikipedia article, separated by tokens (list of string)
    """
    return text.split()


def remove_punctuation(text, punctuation=string.punctuation):
    """
    From string.punctuation, each character is replaced by None (the character is removed)
    """
    return text.translate(str.maketrans('', '', punctuation))


def lowercase_text(text):
    """
    Each character is replaced by his lowercase version
    """
    return text.lower()


def remove_stopwords(text, stopwords):
    """
    Remove every occurrence of the given stopwords set
    """
    return " ".join([w for w in text.split() if w not in stopwords])
