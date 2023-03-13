import abc
from typing import Dict, Any
import pandas as pd

class DataAccessObject:
    
    filter_params: Dict[str, Any]
    
    @abc.abstractmethod
    def get_data(self) -> None:
        raise NotImplementedError
    
class DataAccessObjectImpl1(DataAccessObject):
    
    def get_data(self) -> pd.DataFrame:
        from sklearn import datasets
        random_data_temp:pd.DataFrame = datasets.load_iris()
        return random_data_temp
    
# TODO : mention the risk of underlying data changing.