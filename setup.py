from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirement=[]
    with open(file_path) as file_obj:
        file_obj.readlines()
        requirement=[req.replace("\n","")for req in requirement]
            
        return requirement


setup(
    name='src',
    version='0.0.1',
    author='amar',
    author_email='amar.gupta@mouser.com',
    install_requires=get_requirements('requirement.txt'),
    packages=find_packages(),
)