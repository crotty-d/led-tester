#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `LEDtester` package."""

import sys
sys.path.append('.')

import pytest
import requests


from LEDtester import utils
from LEDtester import LEDsimulator

def test_request():
    """
    Test uri request
    """
    return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_parse_valid_uri():
    uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    L, instructions = utils.parse_file(uri)
    assert L == 1000
    assert instructions[0:3] == ['turn off 660,55 through 986,197', 'turn off 341,304 through 638,850', 'turn off 199,133 through 461,193']
    assert instructions[-1] == 'switch 296,687 through 906,775'
    

def test_parse_invalid_uri():
    file = 'http://dsafdfghklk.hkh/file'
    L, instructions = utils.parse_file(file)
    assert L == 0
    assert instructions[0] == 'error'
    
    grid = LEDsimulator.LEDgrid(10)
    grid.lights[4,4] = 1
        
    for instruction in instructions:
        grid.apply(instruction)
        
    print(grid.lights)
        
    assert grid.count() == 1