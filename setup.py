import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "requirements.txt"), 'r') as f:
    requirements = [r.strip() for r in f.read().splitlines()]

setup(
    name='wiki_gendersort',
    version='0.1',
    packages=[],
    url='https://github.com/nicolasberube/Wiki-Gendersort',
    author='Nicolas Bérubé',
    author_email='nicolas.berube.3@umontreal.ca',
    description='Wiki-Gendersort: automatic gender detection using first names in Wikipedia',
    include_package_data=True,
    install_requires=requirements
)
