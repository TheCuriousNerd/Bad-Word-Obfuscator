from os import name
from setuptools import find_packages, setup

setup(
    name='BadWordObfuscator',
    packages=find_packages(include=['BadWordObfuscator']),
    version='0.1.0',
    description='This code obfuscates naughty words by using a rot13 cipher to prevent them from being directly visible.',
    author='Alex Orid, The Curious Nerd',
    install_requires=[]
)