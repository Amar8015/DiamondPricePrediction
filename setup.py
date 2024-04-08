from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        file_obj.readlines()
        [req.replace("\n","")for req in requirements]
        return requirements


setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='amar',
    author_email='amar.gupta@mouser.com',
    install_requires=get_requirements('requirement.txt'),
    packages=find_packages()
)