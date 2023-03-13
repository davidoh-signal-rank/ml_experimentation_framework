import sys
import os

# Add the parent directory of the cloned repository to the module search path
parent_directory = os.path.dirname(os.path.abspath(__file__))
module_directory = os.path.join(parent_directory, "repo-7f6d29a8f93a269b49ef38b70ac0bc4e8abd33ce")
print(f"parent_directory: {parent_directory}")
print(f"module_directory: {module_directory}")

alias = "abcdefg"  # Use a unique name as an alias
# sys.path.insert(0, (module_directory, alias))
# print("path added")
# print(sys.path)

path_with_alias = {alias: module_directory}
sys.path.append(path_with_alias)
print(sys.path)


