from setuptools import setup
from typing import List


# Declaring variables for setup function
PROJECT_NAME='Housing Predictor'
VERSION="0.0.1"
AUTHOR='Akshay Sen'
DESCRIPTION='My First FSDS Project'
PACKAGES=['housing']
REQUIREMENTS_FILE_NAME='requirements.txt'



def get_requirements_list()->List[str]:  # func will return list with string
    """
    Description: This function will return the list of requirements 
    mentioned in requirements.txt file

    return This function will return name of required libraries.
    """
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        return requirements_file.readlines()


setup(
name=PROJECT_NAME,
version=VERSION,
author=VERSION,
description=DESCRIPTION,
packages=PACKAGES,
license='Apache',
install_requires=get_requirements_list()

)
