import glob
from extractor import extract_text
from preprocess import clean_text
from tokenizer import tokenize
from mining import word_frequency, tfidf_analysis
from exporter import export_freq, export_tfidf

texts = []

for pdf in glob.glob("../input_pdf/*.pdf"):
    text = extract_text(pdf)
    text = clean_text(text)
    texts.append(text)

    words = tokenize(text)
    freq = word_frequency(words)

    export_freq(freq, "../output/result")

tfidf = tfidf_analysis(texts)
export_tfidf(tfidf, "../output/result")

print("完了")
