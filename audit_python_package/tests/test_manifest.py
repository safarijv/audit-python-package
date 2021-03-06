# encoding: utf-8
# Created by Jeremy Bowman on Thu Apr 23 10:36:32 EDT 2015
# Copyright (c) 2015 Safari Books Online. All rights reserved.

from __future__ import unicode_literals

import os

import pytest

from audit_python_package import get_file_lines


@pytest.fixture(scope='module')
def manifest():
    """Fixture that provides a list of the entries in MANIFEST.in"""
    return get_file_lines('MANIFEST.in')


class TestManifest(object):
    """
    Tests related to the MANIFEST.in file.  Configuring this file correctly is
    the best way to create a package that builds cleanly as both a wheel and
    a source distribution.
    """

    def test_exists(self):
        """There should be a MANIFEST.in file in the project's root directory"""
        assert os.path.exists('MANIFEST.in')

    def test_readme(self, manifest):
        """There should be an entry for README.rst in MANIFEST.in"""
        assert 'include README.rst' in manifest

    def test_requirements(self, manifest):
        """There should be a recursive-include in MANIFEST.in for requirements files"""
        assert 'recursive-include requirements *.txt' in manifest
