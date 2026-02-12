from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    '''
    this  function will return of requirements
    '''
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            #read files from the file
            lines = file.readlines()
            # process the lines
            for line in lines:
                requirement = line.strip()
                #skip the emptyspace and -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Returning empty requirements list.")

    return requirement_lst

setup(
    name = "Network security project",
    version='0.0.1',
    author1 = "Navadeep goud",
    author1_email = "9deepgoud@gmail.com",
    author2 = "Abhilash",
    author2_email = "vadlaabhilash964@gmail.com",
    author3 = "Karthik reddy",
    author3_email = "karthikreddyvenna202@gmail.com",
    
    packages = find_packages(),
    install_requires = get_requirements(),
)