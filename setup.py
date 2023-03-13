#!/usr/bin/env python
import os
import setuptools

import versioneer


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def is_package_name(requirement_arg):
    invalid_prefixes = ("-", "#")
    return requirement_arg and not requirement_arg.startswith(invalid_prefixes)


def get_install_requires(filename):
    return [line.strip() for line in read(filename).split('\n') if is_package_name(line)]


setuptools.setup(
    install_requires=get_install_requires("requirements.txt"),
    tests_require=get_install_requires("requirements-test.txt"),
    packages=setuptools.find_packages(),
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass()
)
