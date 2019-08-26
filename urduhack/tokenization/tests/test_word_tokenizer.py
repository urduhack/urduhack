from ..word_tokenizer import UrduWordTokenizer
def test():
    tokenizer = UrduWordTokenizer()
    print(tokenizer.tokenize_words('میڈیاکے نمائندوں نےنیپال میں میڈیاکی صورت حال سےمتعلق آگاہ کیا'))
if __name__ == "__main__":
    test()