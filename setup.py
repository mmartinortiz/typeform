# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='typeform',
      version='0.2',
      description='A Python Wrapper for the Typeform API',
      url='http://github.com/WarmongeR1/typeform',
      author='Robert Banks, Alexander Sapronov',
      license='MIT',
      packages=['typeform'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      install_requires=['requests'])
