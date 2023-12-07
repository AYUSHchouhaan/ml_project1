from setuptools import find_packages,setup
from typing import List

hypon_dot = '-e .'
def get_requirments(file_path)->List[str]:
    

    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        
        if hypon_dot in requirements:
            requirements.remove(hypon_dot)

        return requirements



setup(
    name='ml_project1',
    version='0.1.0',
    author='ayush chouhan',
    author_email='ayush02jul@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirements.txt')
)