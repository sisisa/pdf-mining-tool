from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer

def word_frequency(words, top_n=20):
    return Counter(words).most_common(top_n)


def tfidf_analysis(texts):
    vec = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
    X = vec.fit_transform(texts)

    scores = X.toarray()[0]
    words = vec.get_feature_names_out()

    pairs = list(zip(words, scores))
    pairs.sort(key=lambda x: x[1], reverse=True)

    return pairs[:20]
