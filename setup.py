from setuptools import setup, find_packages
from typing import List


# Declaring variables for setup function
PROJECT_NAME='Housing Predictor'
VERSION="0.0.3"
AUTHOR='Akshay Sen'
DESCRIPTION='My First FSDS Project'
REQUIREMENTS_FILE_NAME='requirements.txt'



def get_requirements_list()->List[str]:  # func will return list with string
    """
    Description: This function will return the list of requirements 
    mentioned in requirements.txt file

    return This function will return name of required libraries.
    """
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        return requirements_file.readlines().remove("-e .")


setup(
name=PROJECT_NAME,
version=VERSION,
author=VERSION,
description=DESCRIPTION,
packages=find_packages(),
license='Apache',
install_requires=get_requirements_list()

)
