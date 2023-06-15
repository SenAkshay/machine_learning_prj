from setuptools import setup, find_packages
from typing import List


# Declaring variables for setup function
PROJECT_NAME='Housing Predictor'
VERSION="0.0.3"
AUTHOR='Akshay Sen'
DESCRIPTION='My First FSDS Project'
REQUIREMENTS_FILE_NAME='requirements.txt'

HYPHEN_E_DOT = "-e ."


def get_requirements_list()->List[str]:  # func will return list with string
    """
    Description: This function will return the list of requirements 
    mentioned in requirements.txt file

    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file.
    """
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        requirement_list = requirements_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
license='Apache',
install_requires=get_requirements_list()

)
