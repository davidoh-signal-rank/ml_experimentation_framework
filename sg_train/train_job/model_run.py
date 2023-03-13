
# ## Maybe this should turn into API!


import subprocess

# Clone the repository and checkout the appropriate Git hash
# subprocess.check_call(['git', 'clone', 'https://github.com/davidoh-signal-rank/ml_experimentation_framework'])
# subprocess.check_call(['git', 'checkout', git_hash], cwd='sg_train')


import pkg_resources
import os

installed_packages = [pkg.key for pkg in pkg_resources.working_set]
print(installed_packages)

import shutil
import git

# Get the absolute path of the current file
current_file_path = os.path.abspath(__file__)

# Get the directory of the current file
current_directory = os.path.dirname(current_file_path)

repo_url = "https://github.com/davidoh-signal-rank/ml_experimentation_framework.git"
commit_hash = "7f6d29a8f93a269b49ef38b70ac0bc4e8abd33ce"  # specific commit hash

# Create a new directory with a unique name
directory_name = os.path.join(current_directory, f'repo-{commit_hash}')


# if not os.path.exists(directory_name):
#     os.mkdir(directory_name)

# if os.path.exists(directory_name):
#     shutil.rmtree(directory_name)
 
# # Clone the repository for a specific commit hash to the new directory
# git.Repo.clone_from(repo_url, directory_name)

# # Open the cloned repository
# repo = git.Repo(directory_name)
# repo.git.checkout(commit_hash)

# # Print the commit hash
# print(repo.head.commit.hexsha)

# Maybe I should have just gotten the artifact not the code base itself.
# But this is for the purpose of reproduction... I need the code base...

import sys
# Add the parent directory of the cloned repository to the module search path
parent_directory = os.path.dirname(os.path.abspath(__file__))
module_directory = os.path.join(parent_directory, "repo-7f6d29a8f93a269b49ef38b70ac0bc4e8abd33ce")
# alias = "abcdefg"  # Use a unique name as an alias
# # sys.path.append(module_directory)
# sys.path.insert(0, (module_directory, alias))
# print("path added")
# print(sys.path)

# from abcdefg.sg_train.model.model import ModelImpl1


import importlib

# # Load the module with the absolute path
# module = importlib.import_module(os.path.join(module_directory, 'sg_train', 'model', 'model'))

# print(f"module: {module}")
# # Access the class within the module
# MyClass = module.Model

# print(MyClass)

import pkgutil

# Set the directory path to search for modules
directory_path = os.path.join(module_directory, 'sg_train', 'model', 'model')

# List all available modules in the directory
module_names = [name for _, name, _ in pkgutil.iter_modules([directory_path])]

# Print the module names
print(module_names)



# import pkgutil
# # Use the alias to recursively find all modules in the cloned repository's module directory
# for importer, module_name, ispkg in pkgutil.walk_packages(path=[alias]):
#     print("herehere")
#     print(module_name)

# Import a module from the cloned repository
# from versioned.sg_train.model.model import ModelImpl1