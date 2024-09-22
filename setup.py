from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."
REQUIRMENT = "requirments.txt"


def get_requirment_list()->List[str]:
  with open(REQUIRMENT) as requirment_file:
    requirment_list = requirment_file.readlines()
    requirment_list = [req_name.replace("\n", "") for req_name in requirment_list]

    if HYPEN_E_DOT in requirment_list:
      requirment_list.remove(HYPEN_E_DOT)
    
    return requirment_list

setup(
   name='foo',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.example',
   packages=find_packages(),
   install_requires=get_requirment_list(),
)
