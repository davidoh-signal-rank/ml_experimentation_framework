
import pkg_resources
import os
import importlib
from model import Model
from typing import Type
from feature_generator import FeatureGenerator
from data_access_object import DataAccessObject
from train_model import train_model
installed_packages = [pkg.key for pkg in pkg_resources.working_set]
print(installed_packages)

import shutil
import git

# Get the absolute path of the current file
current_file_path = os.path.abspath(__file__)

# Get the directory of the current file
current_directory = os.path.dirname(current_file_path)

repo_url = "https://github.com/davidoh-signal-rank/ml_experimentation_framework.git"
commit_hash = "954ab4d3c06da92eda3693af8f15147dd643696a"  # specific commit hash
repo_hash = f'repo-{commit_hash}'  # specific commit hash
# Create a new directory with a unique name
directory_name = os.path.join(current_directory, repo_hash)

if os.path.exists(directory_name):
    shutil.rmtree(directory_name)
 
# Clone the repository for a specific commit hash to the new directory
git.Repo.clone_from(repo_url, directory_name)

# Open the cloned repository
repo = git.Repo(directory_name)
repo.git.checkout(commit_hash)

# Add the parent directory of the cloned repository to the module search path
parent_directory = os.path.dirname(os.path.abspath(__file__))
module_directory = os.path.join(parent_directory, repo_hash)



def get_model(model_name:str) -> Type[Model]:
    # Load the module with the absolute path
    module = importlib.import_module('model', os.path.join(module_directory))
    # Load the feature generator class and generate the features
    model = getattr(module, "ModelImpl1")
    return model

def get_feature_generator(feature_generator_name:str) -> Type[FeatureGenerator]:
    # Load the module with the absolute path
    module = importlib.import_module('feature_generator', os.path.join(module_directory))
    # Load the feature generator class and generate the features
    feature_generator = getattr(module, "FeatureGeneratorImpl1")
    return feature_generator

def get_data_access_object(data_access_object_name:str) -> Type[DataAccessObject]:
    # Load the module with the absolute path
    module = importlib.import_module('data_access_object', os.path.join(module_directory))
    # Load the feature generator class and generate the features
    data_access_object = getattr(module, "DataAccessObjectImpl1")
    return data_access_object


train_model(model_class = get_model("ModelImpl1"),
            model_params= {},
            feature_generator_class=get_feature_generator("FeatureGeneratorImpl1"),
            dataset_class=get_data_access_object("DataAccessObjectImpl1"),
            dataset_params={}
)
