from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer


class ExtractionFeatures:
    def __init__(self):
        self.bog_of_words = CountVectorizer()
        self.tfidf_vertorizer = TfidfVectorizer()

    def bog(self,text):
        return self.bog_of_words.fit_transform(text)

    def tfidf(self,text):
        return self.tfidf_vertorizer.fit_transform(text)

