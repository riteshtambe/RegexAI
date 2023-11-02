from setuptools import setup, find_packages
import codecs
import os

with open('Readme.md', 'r', encoding='utf-8') as file:
    long_description = file.read()


VERSION = '0.0.13'
DESCRIPTION = 'Tranform regex into regexai'
LONG_DESCRIPTION = long_description

# Setting up
setup(
    name="regexai",
    version='0.0.13',
    author="Shreyash Rote , Ritesh Tambe, Rameshwar Adhikar",
    author_email="shreyashrote321@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['openai',spacy],
    keywords=['openai', 'regex', 'pattern', 'text_analysis','text_preprocessing'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
