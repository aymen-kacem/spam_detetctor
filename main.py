import pandas as pd
from DataHandler import DataHandler

def main():
    path = r'C:\Users\User\Desktop\spam.csv'
    data = pd.read_csv(path)
    data_handler = DataHandler(path, data)
    print("import data", data)
    print("le nombre de valeur null", data_handler.verif_nan())
    print("data apres la lavage", data_handler.supprime_nan())

    print("data apres la creation du colonne", data_handler.creat_colonne())


if __name__ == "__main__":
    main()
