import abc
from typing import Dict, Any
import pandas as pd
from sklearn.model_selection import train_test_split

class DataAccessObject(abc.ABC):
    
    filter_params: Dict[str, Any]
    
    @abc.abstractmethod
    def get_data(self) -> None:
        raise NotImplementedError
    
class DataAccessObjectImpl1(DataAccessObject):
    
    def get_data(self) -> pd.DataFrame:
        from sklearn import datasets
        data:pd.DataFrame = datasets.load_iris()

        X = data.data
        y = data.target

        # Split data into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                
        return df
    
# TODO : mention the risk of underlying data changing.


