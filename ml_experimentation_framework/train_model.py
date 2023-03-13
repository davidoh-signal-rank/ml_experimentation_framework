
from typing import Type, Dict, Any
import pandas as pd
from model import Model, ModelImpl1
from data_access_object import DataAccessObject, DataAccessObjectImpl1
from feature_generator import FeatureGenerator, FeatureGeneratorImpl1


def train_model(
    model_class: Type[Model],
    model_params: Dict[str, Any],
    feature_generator_class: Type[FeatureGenerator],
    dataset_class: Type[DataAccessObject],
    dataset_params: Dict[str, Any]
):
    # Load the data
    data_access_object: DataAccessObject = dataset_class(**dataset_params)
    data: pd.DataFrame = data_access_object.get_data()

    # Generate the features
    feature_generator: FeatureGenerator = feature_generator_class()
    features: pd.DataFrame = feature_generator.generate_features(data)

    # Train the model
    model: Model = model_class(**model_params)
    model.train(features)

    return model
