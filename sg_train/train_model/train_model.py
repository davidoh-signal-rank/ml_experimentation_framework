
from typing import Type, Dict, Any
from model.model import Model, ModelImpl1
from data_access_object import DataAccessObject, DataAccessObjectImpl1
from feature_generator.feature_generator import FeatureGenerator, FeatureGeneratorImpl1


def train_model(
    model_class: Type[Model],
    model_params: Dict[str, Any],
    feature_generator_class: Type[FeatureGenerator],
    dataset_class: Type[DataAccessObject],
    dataset_params: Dict[str, Any]
):
    ## -- Just want to try this for now -- ##
    
    print("Run Run RUn ")
    
    # Generate Model ID
    
train_model(
    model_class=ModelImpl1,
    model_params={},
    feature_generator_class=FeatureGeneratorImpl1,
    dataset_class=DataAccessObjectImpl1,
    dataset_params={},
)