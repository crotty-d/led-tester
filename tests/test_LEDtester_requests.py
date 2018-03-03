#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `LEDtester` package."""

import sys
sys.path.append('.')

import pytest
import requests
from bs4 import BeautifulSoup


from LEDtester import utils

@pytest.fixture
def response():
    """
    Test uri request
    """
    return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

 
def test_content(response):
    """Test content from response from uri (fixture)"""
    
    assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_parse_from_uri():
    uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    L, instructions = utils.parse_file(uri)
    assert L == 1000
    assert instructions[0:3] == ['turn off 660,55 through 986,197', 'turn off 341,304 through 638,850', 'turn off 199,133 through 461,193']
    assert instructions[-1] == 'switch 296,687 through 906,775'