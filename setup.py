# encoding: utf-8
# Created by Jeremy Bowman on Thu Apr 23 10:36:32 EDT 2015
# Copyright (c) 2015 Safari Books Online. All rights reserved.
"""
audit-python-package setup script
"""

from __future__ import unicode_literals

import os
from setuptools import find_packages, setup

version = '1.0.0'

install_requires = [
    'future',
    'pytest',
]

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    from pip.download import PipSession
    from pip.index import PackageFinder
    from pip.req import parse_requirements
    session = PipSession()
    root_dir = os.path.abspath(os.path.dirname(__file__))
    requirements_path = os.path.join(root_dir, 'requirements', 'documentation.txt')
    finder = PackageFinder([], [], session=session)
    requirements = parse_requirements(requirements_path, finder, session=session)
    install_requires.extend([str(r.req) for r in requirements])

setup(
    name='audit-python-package',
    version=version,
    author='Jeremy Bowman',
    author_email='jbowman@safaribooksonline.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
    ],
    description='Checks for compliance with current Python packaging best practices',
    url='http://github.com/safarijv/audit-python-package',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    scripts=[],
    zip_safe=True,
    install_requires=install_requires,
)