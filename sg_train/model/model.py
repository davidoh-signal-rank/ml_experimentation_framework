import abc
from typing import Any

@abc
class Model:

    model: Any
    
    @abc.abstractmethod
    def train(self) -> None:
        raise NotImplementedError

class ModelImpl1(Model):
    def train(self) -> None:
        self.model = "Trained Model"
    
    # def train(self, data: Data) -> Model:
    #     pass
    