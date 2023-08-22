from setuptools import setup, find_packages

# Informations sur votre package
PACKAGE_NAME = 'detection_services'
VERSION = '0.1.0'
DESCRIPTION = 'A detection extension for SONIC project'
AUTHOR = 'AHBAIZ MOUHCINE'
AUTHOR_EMAIL = 'Mouhcine.AHBAIZ-EXT@um6p.ma'
URL = 'https://github.com/Mouhc001/Extansion_Sonic.git'


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages(),  # Trouve automatiquement les packages
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
