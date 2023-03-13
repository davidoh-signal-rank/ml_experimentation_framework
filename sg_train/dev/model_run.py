
# ## Maybe this should turn into API!


import subprocess

# Clone the repository and checkout the appropriate Git hash
git_hash = "090ca730904f5e7f1c73fa331e0d6d211028784c"
# subprocess.check_call(['git', 'clone', 'https://github.com/davidoh-signal-rank/ml_experimentation_framework'])
# subprocess.check_call(['git', 'checkout', git_hash], cwd='sg_train')


import pkg_resources
import os

installed_packages = [pkg.key for pkg in pkg_resources.working_set]
print(installed_packages)

import git


repo_url = "https://github.com/davidoh-signal-rank/ml_experimentation_framework.git"
commit_hash = "090ca730904f5e7f1c73fa331e0d6d211028784c"  # specific commit hash

# Create a new directory with a unique name
directory_name = f'repo-{commit_hash}'
if not os.path.exists(directory_name):
    os.mkdir(directory_name)
    
print("directory created")
# Clone the repository for a specific commit hash to the new directory
git.Repo.clone_from(repo_url, directory_name, depth=1, branch=commit_hash)

# Open the cloned repository
repo = git.Repo(directory_name)

# Print the commit hash
print(repo.head.commit.hexsha)

# # Load the feature generator class and generate the features
# feature_generator_module = __import__('sg_train.model', fromlist=[ModelImpl1])
# feature_generator = getattr(feature_generator_module, feature_generator_class)()

