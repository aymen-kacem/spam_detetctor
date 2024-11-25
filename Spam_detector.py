from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

class spam_detector:
    def __init__(self,model):
        self.model= LogisticRegression

    def tarin(self,X,y):
        X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=20,random_state=42)
        self.model.fit(X_train,Y_train)
        return self.model

    def val_accuracy(self,X,y):
        accuracy=self.model.score(X,y)
        return accuracy