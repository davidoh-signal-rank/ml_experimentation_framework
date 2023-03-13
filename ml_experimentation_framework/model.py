import abc
from typing import Any
import pandas as pd
from sklearn.linear_model import LogisticRegression


class Model(abc.ABC):

    model_class: Any
    
    @abc.abstractmethod
    def train(self) -> None:
        raise NotImplementedError
    
    @abc.abstractmethod
    def predict(self, X_test:pd.DataFrame) -> None:
        raise NotImplementedError
    
    @abc.abstractmethod
    def evaluate(self, y_test) -> None:
        raise NotImplementedError

class ModelImpl1(Model):
    
    model_class:LogisticRegression = LogisticRegression
    
    def train(self, X_train, y_train) -> None:
        self.model_class.fit(X_train, y_train)
    

    