MKFILE_PATH := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME := $(shell basename $(MKFILE_PATH))
PYTHON_VERSION := 3.7

# Create conda environment e.g. SUPER-000-env
create_environment:
	conda create --name $(PROJECT_NAME)-env python=$(PYTHON_VERSION)

# Install python dependencies
install:
	pip install -r requirements.txt


# pip install -U pip setuptools wheel

# # Build Docker Image
# build:
# 	cd $(shell pwd)/source_validation_app && docker build -t source_validation_app .

# # Run Docker Image
# run:
# 	docker run -p 8505:8505 --restart unless-stopped -e FA_USERNAME=${FA_USERNAME} -e FA_SECRET=${FA_SECRET} source_validation_app

# # Delete all compiled Python files
# clean:
# 	find . -type f -name "*.py[co]" -delete
# 	find . -type d -name "__pycache__" -delete

# .PHONY: clean install create_environment
