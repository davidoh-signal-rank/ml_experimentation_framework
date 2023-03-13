import abc
import pandas as pd

class FeatureGenerator(abc.ABC):
    
    @abc.abstractmethod
    def generate_features(self, data: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError
    
class FeatureGeneratorImpl1(FeatureGenerator):
    
    def generate_features(self, data: pd.DataFrame) -> pd.DataFrame:
        return data