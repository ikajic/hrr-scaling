from setuptools import find_packages, setup

setup(
    name="hrr-scaling",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        'nengo',
        'numpy',
        'scipy',
        'matplotlib'
    ]
)
