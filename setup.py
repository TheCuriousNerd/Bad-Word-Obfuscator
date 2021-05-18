from os import name
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setup(
    name='BadWordObfuscator',
    packages=find_packages(include=['BadWordObfuscator']),
    version='0.1.2',
    description='A package that helps make naughty words less visible in code.',
    long_description=long_description,
    author='Alex Orid',
    author_email='inquiries@thecuriousnerd.com',
    url='https://github.com/TheCuriousNerd/Bad-Word-Obfuscator',
    install_requires=[],
    license='lgpl-3.0'
)