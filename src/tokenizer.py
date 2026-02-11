from janome.tokenizer import Tokenizer

t = Tokenizer()

def tokenize(text):
    words = []

    for token in t.tokenize(text):
        pos = token.part_of_speech.split(',')[0]

        if pos in ["名詞", "動詞", "形容詞"]:
            words.append(token.surface)

    return words
