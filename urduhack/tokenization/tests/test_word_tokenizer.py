from ..word_tokenizer import UrduWordTokenizer


def test():
    """
    Tests the correctness of the words tokenized by UrduWordTokenizer object
    """
    tokenizer = UrduWordTokenizer()
    print(tokenizer.tokenize_words('میڈیاکے نمائندوں نےنیپال میں میڈیاکی صورت حال سےمتعلق آگاہ کیا'))


if __name__ == "__main__":
    test()
