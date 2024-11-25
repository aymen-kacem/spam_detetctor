class DataHandler:
    def __init__(self, path, data):
        self.path = path
        self.data = data

    def verif_nan(self):
        sum_nan = self.data.isna().sum()
        return sum_nan

    def supprime_nan(self):
        self.data = self.data.dropna(axis=1)
        return self.data

    def num_spam_ham(self):
        colonne = 'v1'
        num_spam = self.data[colonne].str.count("spam").sum()
        num_ham = self.data[colonne].str.count("ham").sum()
        return num_ham, num_spam

    def creat_colonne(self):
        colonne = 'v1'
        self.data['label'] = self.data[colonne].apply(lambda x: 0 if x == 'spam' else 1)
        return self.data
