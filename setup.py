#!/usr/bin/env python

from setuptools import find_packages, setup

with open("src/mojeto/version", "r") as f:
    version = f.read()

setup(name='mojeto',
      version=version,
      description='Mojeto',
      author='dejvidq',
      package_dir={"": "src"},
      packages=find_packages(
          where="src"
      ),
      entry_points={
          'console_scripts': [
              'mojeto = mojeto.mojeto:main',
          ],
      },
      install_requires=[
          "pyyaml"
      ],
      package_data={'mojeto': ['version']}
      )
