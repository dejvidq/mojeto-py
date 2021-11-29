#!/usr/bin/env python

from setuptools import find_packages, setup

setup(name='mojeto',
      version='0.0.1',
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
      )
