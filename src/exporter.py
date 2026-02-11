import pandas as pd

def export_freq(freq, path):
    df = pd.DataFrame(freq, columns=["word", "count"])
    df.to_csv(path + "_freq.csv", index=False)
    df.to_excel(path + "_freq.xlsx", index=False)


def export_tfidf(tfidf, path):
    df = pd.DataFrame(tfidf, columns=["word", "score"])
    df.to_csv(path + "_tfidf.csv", index=False)
    df.to_excel(path + "_tfidf.xlsx", index=False)
