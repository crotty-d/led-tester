#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `LEDtester` package."""

#ximport os
import sys
sys.path.append('.')

import pytest

from click.testing import CliRunner

from LEDtester import LEDsimulator
from LEDtester import cli
from LEDtester import utils


# @pytest.fixture
# def response():
#     """
#     Test uri request
#     """
#     import requests
#     return requests.get('https://github.com/audreyr/cookiecutter-pypackage')
# 
# 
# def test_content(response):
#     """Test content from response from uri (fixture)"""
#     from bs4 import BeautifulSoup
#     assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'LEDtester.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
 
def test_parse_file(): # TODO possibly add @fixture and input to test_LEDsimulator? Independence?
    ifile = "./data/test_data.txt"
    L, instructions = utils.parseFile(ifile)
    assert L == 10
    assert instructions == ['turn on 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'switch 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'turn on 2,2 through 7,7']
    
def test_LEDconstruct():
    L = 10
    grid = LEDsimulator.LEDgrid(L)
    assert grid.shape == (L, L)
    assert grid.sum == 0
    
def test_LEDcount():
    L = 10
    grid = LEDsimulator.LEDgrid(L)
    assert grid.count() == 0
    grid[2:5, 1:3] = 1
    assert grid.count() == 6 

# def test_LEDon():
#     L = 10
#     ledgrid = LEDsimulator.LEDgrid(L)
#     instruction = 'turn on 0,0 through 9,9\n'
#     ledgrid.apply(instruction)
#     assert ledgrid.count() == L

    
if __name__ == '__main__':
    sys.exit()
    #xprint(os.getcwd())
