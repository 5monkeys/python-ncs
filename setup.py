#!/usr/bin/env python
from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup(
    name='ncs',
    version='0.1.0',
    description="NCS<->RGB color database for Python",
    long_description=readme + '\n\n' + history,
    author="Christopher Rosell",
    author_email='chrippa@5monkeys.se',
    url='https://github.com/5monkeys/python-ncs',
    packages=[
        'ncs',
    ],
    package_dir={'ncs': 'ncs'},
    include_package_data=True,
    license="MIT license",
    zip_safe=False,
    keywords='ncs',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
)
