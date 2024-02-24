from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e'

def requirements(file_path: str) -> list:
    """
    This function will return a list of requirements
    """

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='Customer_Personality_Analysis',
    author='ABDIRAHMAN YSUF',
    author_email='amiirabdi31@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    install_requires=requirements('requirements.txt')
)



