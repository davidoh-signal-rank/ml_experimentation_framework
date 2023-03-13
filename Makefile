MKFILE_PATH := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME := $(shell basename $(MKFILE_PATH))
PYTHON_VERSION := 3.7

# Create conda environment e.g. SUPER-000-env
create_environment:
	conda create --name $(PROJECT_NAME)-env python=$(PYTHON_VERSION)

# Install python dependencies
install:
	pip install -r requirements.txt

